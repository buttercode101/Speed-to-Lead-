#!/usr/bin/env python3
"""One-command setup assistant that does as much as possible locally."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'generated'


def run_bootstrap(args: argparse.Namespace) -> None:
    cmd = [
        'python3',
        str(ROOT / 'tools/bootstrap_speed_to_lead.py'),
        '--business-name', args.business_name,
        '--owner-email', args.owner_email,
        '--admin-email', args.admin_email,
        '--primary-contact', args.primary_contact,
        '--backup-contact', args.backup_contact,
        '--response-sla-minutes', str(args.response_sla_minutes),
    ]
    subprocess.run(cmd, check=True)


def create_operator_packet(args: argparse.Namespace) -> Path:
    slug = ''.join(c.lower() if c.isalnum() else '-' for c in args.business_name).strip('-')
    packet = OUT / f'{slug}-operator-packet.md'
    content = f"""# Operator Packet — {args.business_name}

## What Codex prepared for you
- `generated/{slug}-lead-log-template.csv`
- `generated/{slug}-google-apps-script.js`
- `generated/{slug}-deployment-manifest.json`

## What *you* still need to do (cannot be automated by Codex)
1. Create/open the client Google Sheet.
2. Import `generated/{slug}-lead-log-template.csv`.
3. Paste `generated/{slug}-google-apps-script.js` into Apps Script and run `install()`.
4. Build Make scenario from `implementation/make-module-config-sheet.md`.
5. Connect live Google/Make accounts and authorize modules.
6. Run `implementation/go-live-checklist.md` before launch.

## Client config captured
- Business: {args.business_name}
- Owner email: {args.owner_email}
- Admin email: {args.admin_email}
- Primary contact: {args.primary_contact}
- Backup contact: {args.backup_contact}
- SLA minutes: {args.response_sla_minutes}
"""
    packet.write_text(content, encoding='utf-8')
    return packet


def write_summary(args: argparse.Namespace, packet: Path) -> Path:
    slug = ''.join(c.lower() if c.isalnum() else '-' for c in args.business_name).strip('-')
    path = OUT / f'{slug}-setup-summary.json'
    payload = {
        'business_name': args.business_name,
        'owner_email': args.owner_email,
        'admin_email': args.admin_email,
        'primary_contact': args.primary_contact,
        'backup_contact': args.backup_contact,
        'response_sla_minutes': args.response_sla_minutes,
        'operator_packet': str(packet.relative_to(ROOT)),
    }
    path.write_text(json.dumps(payload, indent=2), encoding='utf-8')
    return path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--business-name', required=True)
    parser.add_argument('--owner-email', required=True)
    parser.add_argument('--admin-email', required=True)
    parser.add_argument('--primary-contact', default='+27821234567')
    parser.add_argument('--backup-contact', default='+27831234567')
    parser.add_argument('--response-sla-minutes', type=int, default=5)
    args = parser.parse_args()

    OUT.mkdir(exist_ok=True)
    run_bootstrap(args)
    packet = create_operator_packet(args)
    summary = write_summary(args, packet)

    print('Setup assistant complete:')
    print(f'- {packet.relative_to(ROOT)}')
    print(f'- {summary.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
