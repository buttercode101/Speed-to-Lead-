# InvoiceFlow Hub - Beginner Setup (Copy/Paste + Click-by-Click)

## 1) Prerequisites
- Google account with Gmail, Google Sheets, and Google Drive access
- Make.com account
- Dedicated invoice mailbox or label, for example `invoices@[clientdomain].co.za` or Gmail label `InvoiceFlow`
- OpenAI API key if using AI extraction or category selection
- Owner/accountant email address for exception alerts
- Optional: Xero or Sage access for a later paid upgrade

## 2) Create the Google Sheet Data Hub
1. Create a new Google Sheet named `InvoiceFlow Hub - [Client Name]`.
2. Create these tabs exactly:
   - `Incoming`
   - `Processed`
   - `Chart of Accounts`
   - `Exceptions`
3. Import the matching headers from `templates/invoiceflow-hub-template.csv`.
4. Freeze row 1 on every tab.
5. Format date columns as `YYYY-MM-DD` and currency columns as South African Rand.
6. Add dropdowns:
   - `Incoming.Status`: `New`, `Downloaded`, `Processed`, `Exception`, `Archived`, `Error`
   - `Exceptions.Reason`: `Missing amount`, `Missing date`, `Unreadable file`, `Duplicate invoice`, `VAT mismatch`, `Unknown category`, `Other`

## 3) Create the Google Drive Archive
Create this folder structure:

```text
InvoiceFlow - [Client Name]/
  Incoming Attachments/
  Archive/
    2026/
      01 - January/
      02 - February/
  Exceptions/
```

## 4) Prepare Gmail Intake
Recommended low-cost setup:
1. Create a dedicated mailbox or Gmail label named `InvoiceFlow`.
2. Add a Gmail filter for emails with attachments and terms such as:
   - invoice
   - tax invoice
   - receipt
   - statement
   - supplier
   - purchase
3. Ask the client to forward supplier invoices to the dedicated mailbox.
4. For first launch, run this as a daily batch instead of real time to conserve Make operations.

## 5) Connect Apps in Make
Connect:
- Gmail
- Google Sheets
- Google Drive
- OpenAI (optional but recommended for extraction)
- Email/Gmail for alerts

Set all scenarios to timezone `Africa/Johannesburg`.

## 6) Scenario 1 - Email Invoice Processor
Scenario name: `[Client] - Email Invoice Processor`

### Module Flow
1. Gmail - Watch Emails using the `InvoiceFlow` label or invoice keyword search.
2. Iterator - iterate through attachments.
3. Gmail - download each attachment.
4. Google Drive - upload attachment to `Incoming Attachments`.
5. Google Sheets - add row to `Incoming` with status `Downloaded`.
6. Text extraction - use Make PDF/OCR tooling, Google Drive conversion, or OpenAI vision/PDF workflow depending on client volume and file type.
7. OpenAI - run the main extraction prompt from `templates/openai-prompts.md`.
8. Validation router:
   - Clean path if vendor, invoice number, invoice date, and total are present and amounts reconcile.
   - Exception path if required fields are missing, duplicate invoice number is found, file is unreadable, or VAT does not reconcile.
9. Category matching:
   - First attempt keyword lookup from `Chart of Accounts`.
   - If unclear, run the categorization prompt.
10. Clean path:
   - Add row to `Processed`.
   - Move file to monthly `Archive` folder.
   - Update `Incoming.Status` to `Archived`.
11. Exception path:
   - Add row to `Exceptions`.
   - Move file to `Exceptions` folder.
   - Send owner/accountant alert with file link and reason.
   - Update `Incoming.Status` to `Exception`.
12. Error handler - notify implementer and owner with module name, email subject, and attachment link.

## 7) Scenario 2 - Daily Summary
Scenario name: `[Client] - InvoiceFlow Daily Summary`

### Schedule
- Run once per weekday at 16:30 SAST.
- Search today's rows in `Processed` and unresolved rows in `Exceptions`.
- Summarize:
  - processed invoice count
  - total value processed
  - VAT total
  - exception count
  - top vendors/categories
  - urgent owner actions
- Send digest by email; optional WhatsApp can be added in paid V2.

## 8) UAT Tests
Run these before go-live:
1. One clean PDF tax invoice.
2. One receipt with no due date.
3. One invoice image/photo.
4. One statement that should route to exception or a separate statement category.
5. One duplicate invoice number.
6. One invoice with missing VAT or unclear VAT.
7. One email with two attachments.

Expected:
- Every attachment creates an `Incoming` row.
- Clean invoices create `Processed` rows.
- Problem invoices create `Exceptions` rows and alerts.
- Files are archived into the correct Drive folder.
- Daily summary totals match the sheet.

## 9) SA-Specific Setup Notes
- Use 15% VAT logic for South African invoices.
- Store VAT numbers if the client wants a V2 compliance upgrade.
- Do not promise accounting advice; position the system as capture, validation, and workflow assistance.
- Keep POPIA in mind: limit access to the Drive archive and remove unnecessary personal data from prompts.
