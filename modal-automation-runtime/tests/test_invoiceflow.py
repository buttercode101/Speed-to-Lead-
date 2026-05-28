from __future__ import annotations

from datetime import date
from decimal import Decimal

from automation_platform.core.config import ChannelConfig, ClientConfig, UsageLimits
from automation_platform.models.invoice import IncomingAttachment
from automation_platform.workflows.invoiceflow import InvoiceFlowWorkflow, choose_category, parse_invoice, validate_invoice


class FakeGmail:
    def __init__(self, attachments):
        self.attachments = attachments

    def search_invoice_attachments(self, query, limit):
        return self.attachments[:limit]


class FakeDrive:
    def archive_file(self, source_link, destination_path):
        return f"archive://{destination_path}/{source_link.split('/')[-1]}"


class FakeSheets:
    def __init__(self):
        self.rows = {"Incoming": [], "Processed": [], "Exceptions": [], "Chart of Accounts": [
            {"Category Name": "Office Supplies", "Keywords": "paper, printer, stationery"},
            {"Category Name": "Repairs & Maintenance", "Keywords": "repair, maintenance, plumber"},
        ]}

    def append_row(self, tab, row):
        self.rows.setdefault(tab, []).append(row)

    def find_rows(self, tab, filters):
        rows = self.rows.get(tab, [])
        if not filters:
            return rows
        return [row for row in rows if all(row.get(key) == value for key, value in filters.items())]


class FakeEmail:
    def __init__(self):
        self.sent = []

    def send_email(self, to, subject, body):
        self.sent.append({"to": to, "subject": subject, "body": body})


class FakeExtractor:
    def __init__(self, payload):
        self.payload = payload

    def extract(self, text):
        return self.payload


def valid_payload(**overrides):
    payload = {
        "vendor": "Printer Paper Co",
        "invoice_number": "INV-001",
        "invoice_date": "2026-05-01",
        "due_date": "2026-05-31",
        "amount_ex_vat": "100.00",
        "vat_amount": "15.00",
        "total_amount": "115.00",
        "description": "printer paper and stationery",
        "currency": "ZAR",
    }
    payload.update(overrides)
    return payload


def test_parse_invoice_normalizes_numbers_and_dates():
    invoice = parse_invoice(valid_payload(amount_ex_vat="1,000.00", vat_amount="150", total_amount="1150"))

    assert invoice.invoice_date == date(2026, 5, 1)
    assert invoice.amount_ex_vat == Decimal("1000.00")
    assert invoice.vat_amount == Decimal("150.00")
    assert invoice.total_amount == Decimal("1150.00")


def test_validate_invoice_accepts_valid_sa_vat_invoice():
    invoice = parse_invoice(valid_payload())
    result = validate_invoice(invoice, today=date(2026, 5, 2))

    assert result.is_valid
    assert result.reasons == ()


def test_validate_invoice_rejects_vat_mismatch():
    invoice = parse_invoice(valid_payload(vat_amount="30.00", total_amount="130.00"))
    result = validate_invoice(invoice, today=date(2026, 5, 2))

    assert not result.is_valid
    assert "VAT amount does not match 15% rate" in result.reasons


def test_choose_category_uses_keywords_before_ai():
    invoice = parse_invoice(valid_payload(description="Emergency plumber repair"))
    category = choose_category(invoice, [{"Category Name": "Repairs & Maintenance", "Keywords": "repair, plumber"}])

    assert category == "Repairs & Maintenance"


def test_workflow_routes_clean_invoice_to_processed():
    sheets = FakeSheets()
    email = FakeEmail()
    workflow = InvoiceFlowWorkflow(
        config=ClientConfig(client_name="Demo", owner_email="owner@example.com", channels=ChannelConfig(email_enabled=True)),
        gmail=FakeGmail([IncomingAttachment("supplier@example.com", "Invoice", "inv.pdf", "drive://inv.pdf", "text")]),
        drive=FakeDrive(),
        sheets=sheets,
        email=email,
        extractor=FakeExtractor(valid_payload()),
    )

    result = workflow.run_daily_batch()

    assert result == {"processed": 1, "exceptions": 0, "documents_seen": 1}
    assert len(sheets.rows["Incoming"]) == 1
    assert len(sheets.rows["Processed"]) == 1
    assert sheets.rows["Processed"][0]["category"] == "Office Supplies"
    assert email.sent == []


def test_workflow_routes_invalid_invoice_to_exception_and_alerts():
    sheets = FakeSheets()
    email = FakeEmail()
    workflow = InvoiceFlowWorkflow(
        config=ClientConfig(
            client_name="Demo",
            owner_email="owner@example.com",
            channels=ChannelConfig(email_enabled=True),
            limits=UsageLimits(max_messages_per_day=5),
        ),
        gmail=FakeGmail([IncomingAttachment("supplier@example.com", "Invoice", "inv.pdf", "drive://inv.pdf", "text")]),
        drive=FakeDrive(),
        sheets=sheets,
        email=email,
        extractor=FakeExtractor(valid_payload(vendor="", total_amount="")),
    )

    result = workflow.run_daily_batch()

    assert result == {"processed": 0, "exceptions": 1, "documents_seen": 1}
    assert len(sheets.rows["Exceptions"]) == 1
    assert "Missing vendor" in sheets.rows["Exceptions"][0]["reason"]
    assert len(email.sent) == 1
