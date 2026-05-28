# Free-Tier Cloud Strategy

## Core Principle
Design every automation to run safely at low volume before adding paid channels, AI, or integrations.

## Default Free Stack
- Modal Starter/included compute for Python cron jobs and webhooks.
- Google Sheets as the database and client-facing admin surface.
- Google Drive as the document archive.
- Gmail for intake and owner alerts.
- Google Forms for lead capture where possible.
- Google Calendar for bookings.

## Optional / Client-Paid Stack
- WhatsApp Business Platform for automated messaging.
- Gemini/OpenAI for extraction, summarization, and AI chat.
- OCR APIs for messy scanned documents.
- Xero/Sage integrations.
- Custom domains, dashboards, and long-term logging.

## Hard Guardrails to Implement
- `max_documents_per_batch`
- `max_ai_calls_per_day`
- `max_messages_per_day`
- `max_ocr_pages_per_batch`
- `dry_run`
- `whatsapp_enabled`
- `ai_enabled`

## What to Tell Clients
"The V1 is designed for free or included tiers at low volume. If usage grows, WhatsApp, AI, OCR, or accounting-system API costs may apply. We use client-owned accounts and hard caps so there are no surprise bills."
