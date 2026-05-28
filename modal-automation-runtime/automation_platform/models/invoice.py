from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal


@dataclass(frozen=True)
class IncomingAttachment:
    email_from: str
    subject: str
    attachment_name: str
    file_link: str
    extracted_text: str = ""
    received_at: datetime | None = None


@dataclass(frozen=True)
class ExtractedInvoice:
    vendor: str | None
    invoice_number: str | None
    invoice_date: date | None
    due_date: date | None
    amount_ex_vat: Decimal | None
    vat_amount: Decimal | None
    total_amount: Decimal | None
    description: str = ""
    currency: str = "ZAR"
    raw: dict = field(default_factory=dict)


@dataclass(frozen=True)
class InvoiceValidationResult:
    is_valid: bool
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class ProcessedInvoiceRow:
    timestamp: str
    vendor: str
    invoice_number: str
    invoice_date: str
    due_date: str
    amount_ex_vat: str
    vat_amount: str
    total: str
    category: str
    notes: str
    xero_sage_ref: str
    archive_link: str


@dataclass(frozen=True)
class ExceptionRow:
    timestamp: str
    file_link: str
    reason: str
    suggested_fix: str
    owner_notes: str = ""
    status: str = "Open"
