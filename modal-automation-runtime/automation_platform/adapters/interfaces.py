from __future__ import annotations

from typing import Protocol, Iterable, Any

from automation_platform.models.invoice import IncomingAttachment


class GmailAdapter(Protocol):
    def search_invoice_attachments(self, query: str, limit: int) -> Iterable[IncomingAttachment]:
        """Return invoice-like attachments for processing."""


class DriveAdapter(Protocol):
    def archive_file(self, source_link: str, destination_path: str) -> str:
        """Move/copy a file and return the archive link."""


class SheetsAdapter(Protocol):
    def append_row(self, tab: str, row: dict[str, Any]) -> None:
        """Append a row to a Google Sheet tab."""

    def find_rows(self, tab: str, filters: dict[str, Any]) -> list[dict[str, Any]]:
        """Find rows matching simple filter values."""


class EmailAdapter(Protocol):
    def send_email(self, to: str, subject: str, body: str) -> None:
        """Send an email alert or report."""


class InvoiceExtractor(Protocol):
    def extract(self, text: str) -> dict[str, Any]:
        """Extract invoice JSON from document text."""
