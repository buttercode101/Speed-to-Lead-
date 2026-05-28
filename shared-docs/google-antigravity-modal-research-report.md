# Google Antigravity + Modal Research Report for the Blueprint Suite

## Research Date
2026-05-28

## Sources Checked
- Google I/O 2026 developer highlights: https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/
- Modal pricing: https://modal.com/pricing
- Modal web endpoint docs: https://modal.com/docs/guide/webhooks
- Modal cron docs: https://modal.com/docs/guide/cron
- Modal secrets docs: https://modal.com/docs/guide/secrets
- WhatsApp Business Platform pricing: https://whatsappbusiness.com/products/platform-pricing/
- Google Apps Script quotas: https://developers.google.com/apps-script/guides/services/quotas
- Information Regulator South Africa: https://inforegulator.org.za/

## Main Conclusion
Use Google Antigravity as the build environment and Modal as the runtime. Antigravity helps generate, refactor, test, and maintain the automations. Modal hosts the Python webhooks, cron jobs, and background workers.

## Free-Tier Reality
The suite can be built with a no-budget posture only if usage is capped and client-owned accounts are used.

### Good Free-Fit Workflows
1. InvoiceFlow daily email invoice processing.
2. Email-based owner reports.
3. Google Sheets CRM/task automation.
4. Google Drive archiving.
5. Google Forms/web form intake.

### Risky Free-Fit Workflows
1. WhatsApp proactive reminders and follow-ups.
2. High-volume OCR.
3. High-volume AI extraction or chat.
4. Always-on dashboards.
5. Xero/Sage posting.

## Recommended Build Order
1. InvoiceFlow Lite.
2. Speed-to-Lead Lite without mandatory WhatsApp.
3. TenantDesk Lite.
4. Clinic Reminder Lite with strict compliance guardrails.
5. Real Estate Agent Lite.
6. Gym Retention Lite.
7. PropGuard modules after the smaller property workflows are proven.

## Required Repo Changes
1. Add a shared Modal runtime.
2. Add free-tier and compliance docs.
3. Add per-blueprint Modal deployment guides.
4. Add client config examples with hard usage caps.
5. Add tests for validation and routing logic.
6. Keep Make.com docs as legacy/no-code deployment option.
7. Use the Antigravity step-by-step guide and prompt pack to keep agents focused on one workflow slice at a time.
