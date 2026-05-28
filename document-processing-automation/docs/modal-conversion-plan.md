# Modal Conversion Plan - Document Processing Automation

## Goal
Convert the broad document-processing Make.com automation into reusable Modal workers that can support InvoiceFlow and later PropGuard document modules.

## Recommended Split
1. Intake worker - Gmail/Drive/Upload intake.
2. Extraction worker - PDF text extraction, OCR, optional AI extraction.
3. Validation worker - duplicates, VAT, high-value approval, missing fields.
4. Archive/report worker - Drive archive and daily report.

## Free V1 Mode
- Process daily batches only.
- Limit files per batch.
- Extract text PDFs before using OCR or AI.
- Route messy scans to exceptions instead of forcing expensive processing.

## Paid V2 Mode
- Add OCR APIs.
- Add Xero/Sage posting.
- Add WhatsApp approval messages.
- Add dashboard reporting.
