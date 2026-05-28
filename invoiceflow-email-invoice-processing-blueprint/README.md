# Expanded Blueprint #1: Automated Email Document & Invoice Processing (InvoiceFlow)

A production-ready Make.com + Gmail + Google Sheets automation blueprint for South African SMEs that receive invoices, receipts, statements, and supplier documents by email.

## Core Value Proposition
InvoiceFlow stops accountants, bookkeepers, property managers, and SME owners from manually opening emails, downloading attachments, typing invoice fields, and chasing exceptions. The automation reads invoice emails, extracts key data, validates it, categorizes it, archives the file, and only alerts a human when something needs review.

## Why This Wins in South Africa in 2026
- **Easy to sell:** admin-heavy teams feel the invoice capture pain every week.
- **Low-cost to execute:** V1 can run on Make.com free-tier principles with Gmail, Google Sheets, Google Drive, and optional OpenAI.
- **Clear ROI:** 150 invoices/month x 10 minutes saved = 25 hours saved, worth roughly R7,500-R10,000/month at R300-R400/hour.
- **Simple demo:** forward one invoice into the dedicated inbox and show the extracted row plus exception routing live.

## Target Clients
1. Accountants and bookkeepers (best-fit beachhead)
2. Property managers and landlords
3. Retail, spaza, and small wholesale businesses
4. Construction and trades companies
5. Small law firms and consultants

## Free-Tier Structure (2 Scenarios)
1. **Email Invoice Processor** - daily batch intake, extraction, validation, categorization, archiving, and exception alerts.
2. **Daily Summary** - daily owner/accountant digest with processed totals, exception count, and action list.

## InvoiceFlow Hub Tabs
- `Incoming` - intake log and processing status.
- `Processed` - clean invoice records ready for accounting action or Xero/Sage capture.
- `Chart of Accounts` - keyword-based reference table for category matching.
- `Exceptions` - unreadable, incomplete, duplicate, or invalid invoices that need review.

## SA Pricing Guidance
- **Build:** R5,500-R10,500 once-off
- **Retainer:** R1,200-R2,800/month for monitoring, improvements, prompt/category tuning, and monthly reporting

## Included Files
- `docs/step-by-step-setup.md`
- `docs/make-scenarios.md`
- `docs/go-live-checklist.md`
- `templates/invoiceflow-hub-template.csv`
- `templates/openai-prompts.md`
- `templates/client-pitch-and-roi.md`
- `make/scenario-1-email-invoice-processor.json`
- `make/scenario-2-daily-summary.json`
