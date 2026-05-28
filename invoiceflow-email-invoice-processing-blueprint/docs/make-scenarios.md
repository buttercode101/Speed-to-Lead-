# Make.com Scenarios - InvoiceFlow Email Invoice Processing

## Scenario 1 - Email Invoice Processor

### Goal
Process invoice-related email attachments in a daily batch, extract structured invoice data, validate the results, categorize the spend, archive clean files, and route exceptions to a human.

### Recommended Gmail Search
Use one of these approaches:

```text
label:InvoiceFlow has:attachment (invoice OR "tax invoice" OR receipt OR statement)
```

or, for a dedicated inbox:

```text
has:attachment (invoice OR "tax invoice" OR receipt OR statement OR supplier)
```

### Module-by-Module Build
1. **Gmail - Watch Emails**
   - Folder/label: `InvoiceFlow`
   - Batch schedule: every weekday morning or once daily
   - Only unread or unprocessed emails
2. **Tools - Iterator**
   - Iterate over email attachments
   - Continue if file extension is PDF, PNG, JPG, JPEG, or HEIC
3. **Gmail - Download Attachment**
   - Download the current attachment bundle
4. **Google Drive - Upload File**
   - Folder: `InvoiceFlow - [Client]/Incoming Attachments`
   - File name pattern: `{{formatDate(now; "YYYYMMDD-HHmm")}} - {{from_email}} - {{attachment_name}}`
5. **Google Sheets - Add Row to Incoming**
   - Timestamp
   - Email From
   - Subject
   - Attachment Name
   - File Link
   - Status = `Downloaded`
   - Processed Date blank
6. **Text Extraction**
   - Free-first option: Google Drive OCR/conversion or Make PDF tools if available on the account
   - AI option: OpenAI extraction from OCR text or supported file text
   - Store extracted text in a variable named `invoice_text`
7. **OpenAI - Create Chat Completion**
   - Use `Main Extraction Prompt` from `templates/openai-prompts.md`
   - Require valid JSON only
   - Parse JSON response in Make
8. **Google Sheets - Search Processed**
   - Check duplicate by `Vendor + Invoice Number` or `Invoice Number + Total`
9. **Google Sheets - Search Chart of Accounts**
   - Match keywords against vendor and description
   - If no confident keyword match, run the categorization prompt
10. **Router - Data Quality Check**
   - Clean path conditions:
     - `vendor` is not empty
     - `invoice_number` is not empty or client allows receipt-style records
     - `invoice_date` is valid
     - `total_amount` > 0
     - not a duplicate
     - VAT check passes or is not required for non-VAT receipt
   - Exception path conditions:
     - unreadable OCR text
     - missing amount/date/vendor
     - duplicate invoice
     - VAT mismatch
     - unknown category when category is mandatory
11. **Clean Path**
   - Add row to `Processed`
   - Move file to `Archive/YYYY/MM - Month/`
   - Optional paid V2: create supplier bill in Xero/Sage
   - Update `Incoming.Status` = `Archived`
   - Update `Incoming.Processed Date` = now
12. **Exception Path**
   - Add row to `Exceptions`
   - Move file to `Exceptions`
   - Send Gmail alert to owner/accountant
   - Update `Incoming.Status` = `Exception`
13. **Error Handler**
   - Send implementer alert with scenario name, module, email subject, attachment name, file link, and error text

### Data Quality Rules
- South African VAT is 15%.
- If `amount_ex_vat + vat_amount` differs from `total_amount` by more than R1.00, route to exception.
- If VAT is absent but total exists, allow it when the document appears to be a receipt from a non-VAT vendor.
- If the invoice date is in the future by more than 7 days, route to exception.
- If due date is blank, allow `null` and continue.

## Scenario 2 - Daily Summary

### Goal
Give the owner/accountant a short daily digest so they trust the automation and clear exceptions quickly.

### Module-by-Module Build
1. **Scheduler**
   - Weekdays at 16:30 SAST
2. **Google Sheets - Search Processed**
   - Filter rows where `Timestamp` is today
3. **Google Sheets - Search Exceptions**
   - Filter unresolved exceptions
4. **Tools - Aggregate**
   - Count processed invoices
   - Sum total amount
   - Sum VAT amount
   - Count exceptions
   - Group by category/vendor if practical
5. **OpenAI - Summary Writer**
   - Use the daily summary prompt from `templates/openai-prompts.md`
6. **Gmail - Send Email**
   - Subject: `InvoiceFlow Daily Summary - [Client] - {{formatDate(now; "YYYY-MM-DD")}}`
   - Send to owner/accountant
7. **Google Sheets - Optional Log Row**
   - Add summary event to an optional `Summary Log` tab if the client wants audit history

## Free-Tier Execution Tips
- Start with one active scenario if the Make plan is tight: run Scenario 1 daily and manually inspect the sheet.
- Use Gmail filters before Make to reduce watched emails.
- Start rule-based categorization before asking OpenAI to categorize every invoice.
- Batch process only the newest 10-25 emails during the first pilot.
- Keep Xero/Sage integration as a paid V2 upgrade after the extraction workflow is trusted.
