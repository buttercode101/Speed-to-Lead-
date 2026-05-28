# Google Antigravity Step-by-Step Implementation Guide

## Purpose
Use this guide to build, test, and implement every project in this repository with Google Antigravity while deploying the production runtime on Modal.

## Current Antigravity Context
As of 2026-05-28, Google describes Antigravity as an agent-first development platform that helps developers move from an idea to a production-ready app. Google also announced Antigravity 2.0, Antigravity CLI, and Antigravity SDK at Google I/O 2026. The important implementation rule for this repository is:

- **Antigravity builds and maintains the code.**
- **Modal hosts the production webhooks, cron jobs, and background workers.**

Reference sources:
- Google I/O 2026 developer highlights: https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/
- Google Antigravity docs home: https://www.antigravity.google/docs/home
- Google Antigravity agent docs: https://antigravity.google/docs/agent

## Implementation Order
Build in this order so each project reuses the runtime pieces from the previous project.

1. InvoiceFlow Lite
2. Speed-to-Lead Lite
3. Follow-up & Nurture Lite
4. Document Processing shared workers
5. TenantDesk Lite
6. Real Estate Agent Lite
7. ClinicFlow Reminder Lite
8. FitGuard Gym Retention Lite
9. PropGuard modular suite

## Phase 1 - Open and Baseline the Repository
1. Open this repository in Antigravity Desktop or Antigravity CLI.
2. Tell the agent to read:
   - `complete-automation-suite-modal-plan.md`
   - `modal-automation-runtime/README.md`
   - `shared-docs/free-tier-cloud-strategy.md`
   - `shared-docs/popia-and-ai-safety-checklist.md`
   - `shared-docs/antigravity-prompt-pack.md`
3. Ask the agent for a short architecture recap before code changes.
4. Run baseline checks:

```bash
cd modal-automation-runtime
python3 -m pytest -q
python3 -m compileall automation_platform modal_app.py
python3 -m json.tool configs/client.example.json >/tmp/client.example.json
```

## Phase 2 - Build the Shared Runtime First
Ask Antigravity to complete these runtime building blocks before adding more product workflows:

1. `GoogleSheetsAdapter`
2. `GmailAdapter`
3. `GoogleDriveAdapter`
4. `EmailAdapter`
5. `PlainTextPdfExtractor`
6. `DryRunAdapter` fixtures for demos
7. Modal Secret setup docs
8. Client onboarding script

Success criteria:
- Unit tests run without real Google credentials.
- Production adapters are isolated behind interfaces.
- Demo adapters can run from local fixture data.
- No secrets are committed.

## Phase 3 - Build InvoiceFlow Lite End-to-End
1. Use the InvoiceFlow prompts from `shared-docs/antigravity-prompt-pack.md`.
2. Implement concrete adapters or dry-run adapters first.
3. Wire `InvoiceFlowWorkflow` into the Modal cron in `modal-automation-runtime/modal_app.py`.
4. Add sample fixture invoices and expected output rows.
5. Add tests for:
   - clean text invoice
   - missing vendor
   - duplicate invoice
   - VAT mismatch
   - future invoice date
   - category keyword match
6. Update `invoiceflow-email-invoice-processing-blueprint/docs/modal-deployment-guide.md` with any exact deployment steps that changed.

Success criteria:
- The workflow can run in dry-run mode without external credentials.
- The workflow can process a small fixture batch.
- It produces `Incoming`, `Processed`, and `Exceptions` outputs.
- It enforces all usage caps.

## Phase 4 - Build Speed-to-Lead Lite
1. Build a `LeadIntakeWorkflow` using Google Sheets and Email first.
2. Add a FastAPI endpoint in Modal for website/form lead capture.
3. Add phone normalization for South Africa.
4. Generate manual WhatsApp click-to-chat links instead of sending WhatsApp by default.
5. Add optional WhatsApp send adapter behind `whatsapp_enabled`.

Success criteria:
- A test payload creates a lead row.
- Owner alert is email-first.
- No WhatsApp send happens unless explicitly enabled.

## Phase 5 - Build Follow-up & Nurture Lite
1. Add a scheduled follow-up workflow.
2. Search Google Sheets for due leads.
3. Queue follow-up tasks or send owner email reminders in free mode.
4. Stop sequences if reply state is already marked.
5. Add WhatsApp reply webhook only after client-paid mode is configured.

Success criteria:
- Follow-ups are deterministic and rule-based.
- Reply detection stops the sequence.
- Message caps prevent runaway sends.

## Phase 6 - Build Shared Document Workers
Document workers should support both `document-processing-automation` and `InvoiceFlow`.

1. Add PDF text extraction.
2. Add OCR only as optional/client-paid or capped mode.
3. Add duplicate detection helpers.
4. Add archive helpers.
5. Add reusable exception routing.

Success criteria:
- Text PDFs are processed without AI.
- Scans route to exceptions if OCR is disabled.
- High-value or unclear documents route to human review.

## Phase 7 - Build WhatsApp-Heavy Products Carefully
For TenantDesk, Real Estate, ClinicFlow, FitGuard, and PropGuard:

1. Build email/Sheets-first mode.
2. Add WhatsApp inbound webhooks where useful.
3. Keep proactive WhatsApp sends disabled by default.
4. Add message templates and cost warnings to docs.
5. Add opt-out and handoff rules.

Success criteria:
- The workflow still provides value without WhatsApp automation.
- WhatsApp is a feature flag, not a hidden dependency.
- Human handoff exists for complaints, emergencies, legal/accounting/medical issues, and payment disputes.

## Phase 8 - Modal Deployment Procedure
For each client:

1. Create a client Google Sheet from the relevant template.
2. Create a client Google Drive folder.
3. Create or confirm Gmail labels and intake addresses.
4. Create a client config JSON from `modal-automation-runtime/configs/client.example.json`.
5. Add credentials to Modal Secrets.
6. Deploy the Modal app.
7. Run dry-run mode.
8. Review output rows and logs.
9. Enable real writes.
10. Enable paid channels only with client approval.

## Phase 9 - Antigravity Review Loop
After each workflow build, ask Antigravity to produce these artifacts:

1. Change summary.
2. Files changed.
3. Tests added.
4. Free-tier risk review.
5. POPIA/AI safety review.
6. Client demo script.
7. Known limitations.
8. Next steps.

## Done Definition for Any Blueprint
A blueprint is implementation-ready only when it has:

- Modal workflow code or a clear runtime mapping.
- Unit tests for core routing and validation.
- Dry-run demo mode.
- Client config example.
- Free-tier limits documented.
- POPIA/AI safety notes.
- Go-live checklist.
- Sales demo script.
