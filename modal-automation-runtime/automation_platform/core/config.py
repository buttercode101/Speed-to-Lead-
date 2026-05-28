from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
import json


@dataclass(frozen=True)
class UsageLimits:
    """Per-run and per-day limits that prevent accidental free-tier overuse."""

    max_documents_per_batch: int = 25
    max_ai_calls_per_day: int = 10
    max_messages_per_day: int = 25
    max_ocr_pages_per_batch: int = 100


@dataclass(frozen=True)
class ChannelConfig:
    """Feature flags for paid or risky channels."""

    email_enabled: bool = True
    whatsapp_enabled: bool = False
    ai_enabled: bool = False
    dry_run: bool = True


@dataclass(frozen=True)
class ClientConfig:
    """Client-level runtime configuration.

    Keep secrets out of this object. Store credentials in Modal Secrets and refer to
    public identifiers such as sheet IDs, folder IDs, and feature flags here.
    """

    client_name: str
    timezone: str = "Africa/Johannesburg"
    google_sheet_id: str = ""
    drive_root_folder_id: str = ""
    invoice_gmail_query: str = "label:InvoiceFlow has:attachment"
    owner_email: str = ""
    channels: ChannelConfig = field(default_factory=ChannelConfig)
    limits: UsageLimits = field(default_factory=UsageLimits)


def load_client_config(path: str | Path) -> ClientConfig:
    """Load a minimal JSON client config.

    YAML is better for humans, but JSON keeps the zero-dependency runtime testable.
    A later production pass can add optional PyYAML support.
    """

    data: dict[str, Any] = json.loads(Path(path).read_text())
    channels = ChannelConfig(**data.get("channels", {}))
    limits = UsageLimits(**data.get("limits", {}))
    return ClientConfig(
        client_name=data["client_name"],
        timezone=data.get("timezone", "Africa/Johannesburg"),
        google_sheet_id=data.get("google_sheet_id", ""),
        drive_root_folder_id=data.get("drive_root_folder_id", ""),
        invoice_gmail_query=data.get("invoice_gmail_query", "label:InvoiceFlow has:attachment"),
        owner_email=data.get("owner_email", ""),
        channels=channels,
        limits=limits,
    )
