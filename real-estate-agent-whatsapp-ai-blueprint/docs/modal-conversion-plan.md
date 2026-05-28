# Modal Conversion Plan - Real Estate Agent WhatsApp AI Agent

## Goal
Convert the WhatsApp-first real estate assistant into a Modal webhook workflow with Sheets-backed listings and Google Calendar booking.

## Modal Endpoints and Jobs
1. `whatsapp_inbound_webhook` - receives buyer/tenant messages.
2. `pipeline_maintenance_cron` - follows up stalled leads and updates pipeline state.
3. `daily_pipeline_report_cron` - emails or WhatsApps the agent summary.

## Free V1 Mode
- Use inbound WhatsApp service-window replies only if the client has WhatsApp Business Platform configured.
- Use email alerts and click-to-chat links when WhatsApp is not enabled.
- Match properties with deterministic rules first: suburb, price range, bedrooms, rental/sale.
- Book viewings through Google Calendar links or manually queued tasks.

## Client-Paid Mode
- Enable proactive viewing reminders and follow-ups through approved WhatsApp templates.
- Add AI-assisted qualification and listing recommendations.
- Add owner/agent WhatsApp summaries.

## Required Guardrails
- Consent and opt-out tracking for nurture messages.
- Human handoff for complaints, finance/legal questions, and offer negotiation.
- Daily message caps to avoid accidental WhatsApp spend.
