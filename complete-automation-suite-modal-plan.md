# Complete Automation Suite Modal Plan

## Objective
Convert the repository from Make.com-only blueprints into a repeatable, version-controlled automation suite built with Google Antigravity and hosted on Modal.

## Architecture Decision
- **Google Antigravity:** build, refactor, test, and document the workflows.
- **Modal:** host Python webhooks, cron jobs, and background workers.
- **Google Sheets/Drive/Gmail/Calendar:** keep the free client-facing operating layer.
- **WhatsApp Business Platform:** optional and client-paid unless only inbound service-window replies are used.

## Product Build Priority
1. **InvoiceFlow Lite** - lowest cost, strongest ROI, no WhatsApp dependency.
2. **Speed-to-Lead Lite** - high demand, email/click-to-chat first, WhatsApp optional.
3. **TenantDesk Lite** - property inbound support and maintenance logging.
4. **Clinic Reminder Lite** - valuable but needs strict healthcare guardrails.
5. **Real Estate Agent Lite** - useful for high-volume agents.
6. **Gym Retention Lite** - best when tied to payment recovery.
7. **PropGuard Modules** - roll out only after smaller property workflows are proven.

## Shared Runtime Deliverables
- Modal app skeleton.
- Config loader with usage caps.
- Google/Email/WhatsApp adapter interfaces.
- InvoiceFlow workflow implementation.
- Unit tests for validation and routing.
- Free-tier strategy docs.
- POPIA/AI safety checklist.
- Antigravity prompt pack and implementation guide.

## Commercial Rule
Never sell these as "free forever." Sell them as low-cost V1 systems with client-owned accounts, usage caps, and paid upgrades for WhatsApp, AI, OCR, accounting integrations, and dashboards.
