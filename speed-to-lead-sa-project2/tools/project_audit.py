#!/usr/bin/env python3
"""Project audit for Speed-to-Lead repo readiness."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'speed-to-lead-sa-project2-guide.md',
    'implementation/quick-start.md',
    'implementation/google-apps-script-template.js',
    'implementation/make-module-config-sheet.md',
    'implementation/go-live-checklist.md',
    'build-artifacts/01-client-proposal-template.md',
    'tools/bootstrap_speed_to_lead.py',
]

HONEST_FINDINGS = [
    'Strong documentation depth, but still depends on manual account-level configuration in Google and Make.',
    'No automated test harness for Apps Script logic; runtime validation must happen in Google environment.',
    'No CI checks for markdown/csv/template consistency yet.',
    'Generated artifacts are useful, but Make scenario is still pseudo-template (manual assembly required).',
    'Biggest delivery risk is operator inconsistency during first 2-3 client deployments.'
]

NEXT_ACTIONS = [
    'Use tools/setup_assistant.py for one-command client bootstrap package generation.',
    'Run pilot with one real client and record issues into an iteration log.',
    'Add CI lint checks (markdown, CSV schema, JSON validity).',
    'Version and export a real Make blueprint JSON once available from live account.',
]


def main() -> None:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    print('=== SPEED-TO-LEAD PROJECT AUDIT ===')
    print(f'Repository: {ROOT}')
    print('')
    print('Readiness:')
    print(f'- Required files present: {len(REQUIRED)-len(missing)}/{len(REQUIRED)}')
    if missing:
        for m in missing:
            print(f'  - MISSING: {m}')
    else:
        print('  - All required baseline files exist.')
    print('')
    print('Honest feedback:')
    for item in HONEST_FINDINGS:
        print(f'- {item}')
    print('')
    print('Minimal-effort path (recommended):')
    for item in NEXT_ACTIONS:
        print(f'- {item}')


if __name__ == '__main__':
    main()
