# InvoiceFlow Go-Live Checklist

## Client Readiness
- [ ] Dedicated invoice mailbox or Gmail label is active.
- [ ] Client has told suppliers/team where to send invoices.
- [ ] Owner/accountant alert email is confirmed.
- [ ] Google Drive archive permissions are limited to approved users.
- [ ] Chart of Accounts categories and keywords are approved.

## Google Sheet Readiness
- [ ] `Incoming` tab has the correct headers.
- [ ] `Processed` tab has the correct headers.
- [ ] `Chart of Accounts` tab has starter categories and keywords.
- [ ] `Exceptions` tab has the correct headers and owner notes column.
- [ ] Status and reason dropdowns are configured.
- [ ] Currency columns are formatted as ZAR.

## Make.com Readiness
- [ ] Gmail connection is authenticated.
- [ ] Google Sheets connection is authenticated.
- [ ] Google Drive connection is authenticated.
- [ ] OpenAI connection is authenticated if AI extraction is enabled.
- [ ] Scenario timezone is `Africa/Johannesburg`.
- [ ] Scenario 1 runs in daily batch mode for launch.
- [ ] Error handler sends alerts to implementer and owner.
- [ ] Operations usage is checked after a test batch.

## Validation Tests
- [ ] Clean PDF invoice routes to `Processed`.
- [ ] Image/photo invoice extracts or routes to a clear exception.
- [ ] Duplicate invoice is detected.
- [ ] Missing amount routes to `Exceptions`.
- [ ] VAT mismatch routes to `Exceptions`.
- [ ] Multiple attachments in one email are processed separately.
- [ ] Archive links open for the owner/accountant.
- [ ] Daily summary email totals match the sheet.

## Go-Live Rules
- [ ] Run a 3-5 day pilot before offering Xero/Sage posting.
- [ ] Review exceptions daily during week 1.
- [ ] Tune category keywords after the first 50-100 documents.
- [ ] Keep a manual backup process until the client signs off.
- [ ] Schedule a monthly optimization review for retainer value.
