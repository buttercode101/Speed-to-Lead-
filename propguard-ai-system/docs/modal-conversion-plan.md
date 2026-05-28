# Modal Conversion Plan - PropGuard AI System

## Goal
Split the broad PropGuard suite into smaller Modal modules so it can be sold and deployed without overrunning free-tier limits.

## Recommended Module Order
1. TenantDesk Lite - inbound tenant support and maintenance logging.
2. Maintenance workflow - ticket status updates and contractor assignment log.
3. Owner reporting - daily/weekly email summaries.
4. Rent reminders - client-paid WhatsApp or email-first reminders.
5. Prospect follow-up - lead nurture from the Leads & Prospects tab.
6. Document processing - reuse InvoiceFlow/document workers.

## Free V1 Mode
- Enable only one or two modules for the first client.
- Use email summaries before WhatsApp owner reports.
- Batch scheduled tasks once daily.
- Cap all AI and messaging usage.

## Client-Paid Mode
- Enable WhatsApp reminders and updates.
- Add OCR/AI document processing.
- Add advanced dashboards and Xero/Sage exports.

## Why Split It
The full PropGuard system has too many workflows for a true no-budget deployment. Modular rollout keeps the offer sellable, testable, and supportable.
