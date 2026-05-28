# Modal Automation Runtime

A Python-first runtime for converting the Make.com blueprint suite into deployable, low-cost cloud automations on Modal.

## Purpose
This runtime is the code layer that sits underneath the sales blueprints in this repository. It is designed to replace Make.com scenarios with version-controlled Python workflows while keeping the same low-cost data layer:

- Google Sheets as the client-visible CRM/data hub
- Google Drive as the archive/document store
- Gmail/Email as the default free alert channel
- WhatsApp Business Platform as an optional client-paid channel
- AI/OCR as optional and budget-capped add-ons

## What Google Antigravity Is Used For
Google Antigravity should be used as the agentic build environment, not the production host. Use it to:

1. Convert blueprint specs into workflow code.
2. Generate tests and client configs.
3. Refactor shared adapters.
4. Produce client-specific deployment manifests.
5. Maintain documentation and demo assets.

## What Modal Is Used For
Modal is the runtime/hosting layer for:

1. FastAPI webhook endpoints.
2. Cron/scheduled jobs.
3. Background workers for OCR/extraction/reporting.
4. Secure secret injection.
5. Small CPU-first automation jobs that fit within free/included usage.

## Free-Tier Operating Rules
- Prefer daily batches over real-time polling.
- Keep active cron jobs under the free Starter allowance.
- Keep endpoints minimal and shared across workflows.
- Default to email alerts before WhatsApp sends.
- Use rule-based extraction/validation before AI.
- Put client-specific API costs on client-owned accounts.
- Enforce per-client usage caps in config.

## Folder Structure
```text
automation_platform/
  adapters/      # Google, email, WhatsApp, OCR, and AI interfaces
  core/          # Config, validation, cost controls, logging helpers
  workflows/     # Product workflows such as InvoiceFlow and Speed-to-Lead
  models/        # Shared typed data structures
configs/         # Example client JSON configs
tests/           # Unit tests that do not require Modal credentials
modal_app.py     # Modal cron/webhook entrypoints
```

## Antigravity Build Guides
- `../shared-docs/antigravity-step-by-step-implementation-guide.md` - build sequence and implementation workflow.
- `../shared-docs/antigravity-prompt-pack.md` - copy/paste prompts for Antigravity agents.

## First Production Candidate
Start with `InvoiceFlow Lite` because it can deliver value without WhatsApp and can run as a daily scheduled batch.
