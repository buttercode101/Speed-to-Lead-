#!/usr/bin/env python3
"""
Speed-to-Lead bootstrap generator.

Generates client-specific deployment files from templates so setup is mostly copy/paste.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMPL = ROOT / "implementation"
OUT = ROOT / "generated"


def replace_tokens(text: str, mapping: dict[str, str]) -> str:
    for k, v in mapping.items():
        text = text.replace("{{" + k + "}}", v)
    return text


def generate_sheet_csv(client_name: str) -> Path:
    source = IMPL / "lead-log-template.csv"
    target = OUT / f"{client_name}-lead-log-template.csv"
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return target


def generate_apps_script(config: dict[str, str]) -> Path:
    source = IMPL / "google-apps-script-template.js"
    text = source.read_text(encoding="utf-8")

    replacements = {
        "owner@example.com": config["owner_email"],
        "admin@example.com": config["admin_email"],
        "Client Business": config["business_name"],
        "+27821234567": config["primary_contact"],
        "+27831234567": config["backup_contact"],
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    text = text.replace("RESPONSE_SLA_MINUTES: 5", f"RESPONSE_SLA_MINUTES: {config['response_sla_minutes']}")

    target = OUT / f"{config['client_slug']}-google-apps-script.js"
    target.write_text(text, encoding="utf-8")
    return target


def generate_deployment_manifest(config: dict[str, str], files: list[Path]) -> Path:
    target = OUT / f"{config['client_slug']}-deployment-manifest.json"
    manifest = {
        "client": config["business_name"],
        "created_files": [str(p.relative_to(ROOT)) for p in files],
        "next_steps": [
            "Import lead-log-template.csv into Google Sheets",
            "Paste generated Apps Script and run install()",
            "Build Make scenario using implementation/make-import-template.json",
            "Run implementation/go-live-checklist.md"
        ]
    }
    target.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return target


def validate_csv(path: Path) -> None:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows or len(rows[0]) < 20:
        raise ValueError("Lead template CSV is malformed or missing required columns")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--business-name", required=True)
    parser.add_argument("--owner-email", required=True)
    parser.add_argument("--admin-email", required=True)
    parser.add_argument("--primary-contact", default="+27821234567")
    parser.add_argument("--backup-contact", default="+27831234567")
    parser.add_argument("--response-sla-minutes", type=int, default=5)
    args = parser.parse_args()

    OUT.mkdir(exist_ok=True)
    client_slug = "".join(c.lower() if c.isalnum() else "-" for c in args.business_name).strip("-")

    config = {
        "business_name": args.business_name,
        "owner_email": args.owner_email,
        "admin_email": args.admin_email,
        "primary_contact": args.primary_contact,
        "backup_contact": args.backup_contact,
        "response_sla_minutes": str(args.response_sla_minutes),
        "client_slug": client_slug,
    }

    csv_path = generate_sheet_csv(client_slug)
    validate_csv(csv_path)
    script_path = generate_apps_script(config)
    manifest = generate_deployment_manifest(config, [csv_path, script_path])

    print("Generated:")
    print(f"- {csv_path.relative_to(ROOT)}")
    print(f"- {script_path.relative_to(ROOT)}")
    print(f"- {manifest.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
