from __future__ import annotations

from dataclasses import asdict
from datetime import UTC, date, datetime
from decimal import Decimal, InvalidOperation
from typing import Any

from automation_platform.adapters.interfaces import DriveAdapter, EmailAdapter, GmailAdapter, InvoiceExtractor, SheetsAdapter
from automation_platform.core.config import ClientConfig
from automation_platform.core.usage import UsageCounter, assert_within_limits
from automation_platform.models.invoice import ExceptionRow, ExtractedInvoice, IncomingAttachment, InvoiceValidationResult, ProcessedInvoiceRow

VAT_RATE = Decimal("0.15")
AMOUNT_TOLERANCE = Decimal("1.00")


def _decimal(value: Any) -> Decimal | None:
    if value is None or value == "" or value == "unclear":
        return None
    try:
        return Decimal(str(value).replace(",", "")).quantize(Decimal("0.01"))
    except (InvalidOperation, ValueError):
        return None


def _date(value: Any) -> date | None:
    if value is None or value == "" or value == "unclear":
        return None
    if isinstance(value, date):
        return value
    try:
        return date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


def parse_invoice(payload: dict[str, Any]) -> ExtractedInvoice:
    """Normalize extractor output into typed invoice fields."""

    return ExtractedInvoice(
        vendor=payload.get("vendor") or None,
        invoice_number=payload.get("invoice_number") or None,
        invoice_date=_date(payload.get("invoice_date")),
        due_date=_date(payload.get("due_date")),
        amount_ex_vat=_decimal(payload.get("amount_ex_vat")),
        vat_amount=_decimal(payload.get("vat_amount")),
        total_amount=_decimal(payload.get("total_amount")),
        description=payload.get("description") or "",
        currency=payload.get("currency") or "ZAR",
        raw=payload,
    )


def validate_invoice(invoice: ExtractedInvoice, duplicate_found: bool = False, today: date | None = None) -> InvoiceValidationResult:
    """Validate core South African invoice capture rules."""

    reasons: list[str] = []
    today = today or datetime.now(UTC).date()

    if not invoice.vendor:
        reasons.append("Missing vendor")
    if invoice.total_amount is None or invoice.total_amount <= 0:
        reasons.append("Missing or invalid total")
    if invoice.invoice_date is None:
        reasons.append("Missing or invalid invoice date")
    elif (invoice.invoice_date - today).days > 7:
        reasons.append("Invoice date is more than 7 days in the future")
    if duplicate_found:
        reasons.append("Duplicate invoice")

    if invoice.amount_ex_vat is not None and invoice.vat_amount is not None and invoice.total_amount is not None:
        calculated_total = invoice.amount_ex_vat + invoice.vat_amount
        if abs(calculated_total - invoice.total_amount) > AMOUNT_TOLERANCE:
            reasons.append("VAT total mismatch")

        expected_vat = (invoice.amount_ex_vat * VAT_RATE).quantize(Decimal("0.01"))
        if invoice.vat_amount > 0 and abs(expected_vat - invoice.vat_amount) > AMOUNT_TOLERANCE:
            reasons.append("VAT amount does not match 15% rate")

    return InvoiceValidationResult(is_valid=not reasons, reasons=tuple(reasons))


def choose_category(invoice: ExtractedInvoice, chart_rows: list[dict[str, Any]]) -> str:
    """Rule-first category matching using Chart of Accounts keywords."""

    haystack = f"{invoice.vendor or ''} {invoice.description}".lower()
    for row in chart_rows:
        category = str(row.get("Category Name", "")).strip()
        keywords = str(row.get("Keywords", ""))
        if not category:
            continue
        for keyword in [part.strip().lower() for part in keywords.split(",") if part.strip()]:
            if keyword and keyword in haystack:
                return category
    return "Other"


def build_processed_row(invoice: ExtractedInvoice, category: str, archive_link: str) -> ProcessedInvoiceRow:
    now = datetime.now(UTC).isoformat()
    return ProcessedInvoiceRow(
        timestamp=now,
        vendor=invoice.vendor or "",
        invoice_number=invoice.invoice_number or "",
        invoice_date=invoice.invoice_date.isoformat() if invoice.invoice_date else "",
        due_date=invoice.due_date.isoformat() if invoice.due_date else "",
        amount_ex_vat=str(invoice.amount_ex_vat or ""),
        vat_amount=str(invoice.vat_amount or ""),
        total=str(invoice.total_amount or ""),
        category=category,
        notes=invoice.description,
        xero_sage_ref="",
        archive_link=archive_link,
    )


def build_exception_row(attachment: IncomingAttachment, validation: InvoiceValidationResult) -> ExceptionRow:
    reason = "; ".join(validation.reasons) or "Unknown exception"
    return ExceptionRow(
        timestamp=datetime.now(UTC).isoformat(),
        file_link=attachment.file_link,
        reason=reason,
        suggested_fix=f"Review the source document and correct: {reason}.",
    )


def duplicate_exists(sheets: SheetsAdapter, invoice: ExtractedInvoice) -> bool:
    if not invoice.invoice_number:
        return False
    matches = sheets.find_rows(
        "Processed",
        {
            "Vendor": invoice.vendor or "",
            "Invoice Number": invoice.invoice_number,
        },
    )
    return bool(matches)


class InvoiceFlowWorkflow:
    """Daily-batch InvoiceFlow workflow for Modal cron execution."""

    def __init__(
        self,
        config: ClientConfig,
        gmail: GmailAdapter,
        drive: DriveAdapter,
        sheets: SheetsAdapter,
        email: EmailAdapter,
        extractor: InvoiceExtractor,
    ) -> None:
        self.config = config
        self.gmail = gmail
        self.drive = drive
        self.sheets = sheets
        self.email = email
        self.extractor = extractor

    def run_daily_batch(self) -> dict[str, int]:
        counter = UsageCounter()
        processed = 0
        exceptions = 0

        attachments = self.gmail.search_invoice_attachments(
            self.config.invoice_gmail_query,
            limit=self.config.limits.max_documents_per_batch,
        )

        for attachment in attachments:
            counter.documents_processed += 1
            assert_within_limits(counter, self.config.limits)

            self.sheets.append_row(
                "Incoming",
                {
                    "Timestamp": datetime.now(UTC).isoformat(),
                    "Email From": attachment.email_from,
                    "Subject": attachment.subject,
                    "Attachment Name": attachment.attachment_name,
                    "File Link": attachment.file_link,
                    "Status": "Downloaded",
                    "Processed Date": "",
                },
            )

            raw_invoice = self.extractor.extract(attachment.extracted_text)
            if self.config.channels.ai_enabled:
                counter.ai_calls += 1
                assert_within_limits(counter, self.config.limits)

            invoice = parse_invoice(raw_invoice)
            validation = validate_invoice(invoice, duplicate_found=duplicate_exists(self.sheets, invoice))

            if validation.is_valid:
                chart_rows = self.sheets.find_rows("Chart of Accounts", {})
                category = choose_category(invoice, chart_rows)
                archive_link = self.drive.archive_file(attachment.file_link, "Archive/YYYY/MM - Month")
                row = build_processed_row(invoice, category, archive_link)
                self.sheets.append_row("Processed", asdict(row))
                processed += 1
            else:
                row = build_exception_row(attachment, validation)
                self.sheets.append_row("Exceptions", asdict(row))
                exceptions += 1
                if self.config.channels.email_enabled and self.config.owner_email:
                    self.email.send_email(
                        to=self.config.owner_email,
                        subject=f"InvoiceFlow exception - {self.config.client_name}",
                        body=f"{row.reason}\n\nFile: {row.file_link}\nSuggested fix: {row.suggested_fix}",
                    )
                    counter.messages_sent += 1
                    assert_within_limits(counter, self.config.limits)

        return {"processed": processed, "exceptions": exceptions, "documents_seen": counter.documents_processed}
