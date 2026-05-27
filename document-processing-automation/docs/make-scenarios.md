# Make.com Scenarios - Document Processing Automation

## Scenario 1 - Document Intake Pipeline
1. Trigger: Gmail Watch Emails (has attachment) OR WhatsApp Watch Media OR Drive Watch Folder
2. Save file to Google Drive path:
   `Client Name/YYYY/Month/Invoices/`
3. Add row to `Incoming Documents` tab with:
   - Status = Pending Extraction
   - Source = Gmail/WhatsApp/Drive
   - File Link

## Scenario 2 - Data Extraction & Validation
1. Search rows where `Status = Pending Extraction`
2. Extract text via OCR/PDF tooling
3. OpenAI structured extraction prompt (JSON fields only)
4. Router validations:
   - VAT missing -> Exceptions tab
   - Duplicate invoice number -> Exception + alert
   - Amount > threshold -> Approval workflow
5. Rule-based categorization using Chart of Accounts keyword map
6. Update `Incoming Documents` with extracted values and status

### Structured Extraction Prompt
Use this exact template:

```
Extract the following fields from this South African invoice.

Return valid JSON only.

Fields:
- Vendor Name
- Invoice Number
- Invoice Date
- Due Date
- Total Amount
- VAT Amount
- Currency
- Line Item Summary

Document Text:
{{ocr_text}}
```

## Scenario 3 - Exception & Approval Workflow
1. Search `Exceptions` where `Status = Exception`
2. Router by type: duplicate / missing data / unreadable / high-value
3. Send WhatsApp approval or action notification
4. Update exception status after owner action

## Scenario 4 - Archiving & Reporting
1. Move processed files to:
   `Processed/Vendor/Year/`
2. Write archive event to `Archive Log`
3. Send daily summary to owner/accountant with:
   - Processed count
   - Exception count
   - Duplicate warnings
   - Top categories
   - Total processed value
