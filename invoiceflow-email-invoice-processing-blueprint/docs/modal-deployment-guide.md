# InvoiceFlow Modal Deployment Guide

## Positioning
InvoiceFlow is the first blueprint that should be converted from Make.com to the shared Modal runtime because it can deliver value without WhatsApp. Gmail, Google Sheets, Google Drive, and a daily Modal cron are enough for a sellable V1.

## Runtime Mapping
| Make.com Step | Modal Runtime Equivalent |
|---|---|
| Gmail Watch Emails | Modal cron calls Gmail adapter with `invoice_gmail_query` |
| Iterator | Python loop over attachments with `max_documents_per_batch` |
| Download File | Gmail/Drive adapter downloads or references attachment |
| Extract Text | Local PDF/OCR extractor or optional AI extractor |
| OpenAI Completion | Optional `InvoiceExtractor` implementation behind `ai_enabled` |
| Google Sheets Add Row | `SheetsAdapter.append_row()` |
| Router | `validate_invoice()` and duplicate checks |
| Archive File | `DriveAdapter.archive_file()` |
| Exception Alert | `EmailAdapter.send_email()` |
| Daily Summary | Separate Modal cron or follow-up workflow method |

## Minimal Modal V1
1. Deploy one Modal app from `modal-automation-runtime/modal_app.py`.
2. Add client Google credentials as Modal Secrets.
3. Create `client.example.json` copy for the client.
4. Run in `dry_run` mode with 5-10 sample invoices.
5. Enable writes to the client's Google Sheet.
6. Enable owner email alerts.
7. Keep AI disabled until rule-based processing is stable.

## Free-Tier Settings
Recommended launch config:

```json
{
  "channels": {
    "email_enabled": true,
    "whatsapp_enabled": false,
    "ai_enabled": false,
    "dry_run": true
  },
  "limits": {
    "max_documents_per_batch": 25,
    "max_ai_calls_per_day": 5,
    "max_messages_per_day": 10,
    "max_ocr_pages_per_batch": 50
  }
}
```

## Sellable V1 Deliverables
- Daily invoice capture batch.
- Incoming/Processed/Exceptions tabs.
- Drive archive links.
- Duplicate detection.
- VAT reconciliation.
- Owner exception emails.
- Daily summary email.

## Paid V2 Upgrades
- OpenAI/Gemini extraction for messy invoices.
- OCR for photos/scans.
- Xero/Sage bill creation.
- WhatsApp owner alerts.
- Dashboard and monthly analytics.
