# Build Plan - Document Processing Automation

## Why this matters
South African SMEs often process invoices and supporting documents manually through email, WhatsApp, and shared folders. This automation reduces repetitive admin and improves financial visibility.

## Phase 1: Intake + Tracking
### Deliverables
- Ingest files from Gmail, WhatsApp, or Drive upload folder
- Save files into structured Drive paths
- Create rows in Incoming Documents tab

## Phase 2: Extraction + Validation
### Deliverables
- Process pending documents
- Run OCR/text extraction
- Use structured AI extraction prompt
- Apply validation rules (missing VAT, duplicates, high value)
- Categorize using rule-based keyword mapping

## Phase 3: Exception + Approval
### Deliverables
- Route exceptions to dedicated workflow
- Send high-value approvals to owner/accountant
- Alert on duplicates/unreadable docs

## Phase 4: Archive + Reporting
### Deliverables
- Move processed files into archive hierarchy
- Update archive log tab
- Send daily summary to stakeholders
