# Document Processing Automation (SA SME V1)

This project is designed as a digital admin assistant for South African SMEs handling invoices, receipts, POPs, and quotations.

## Goal
Automate document intake, extraction, validation, exception handling, and archiving with a practical rule-first approach.

## System Architecture
- Scenario 1: Document Intake Pipeline
- Scenario 2: Data Extraction & Validation
- Scenario 3: Exception & Approval Workflow
- Scenario 4: Archiving & Reporting

## Folder Structure
- `docs/`
  - `build-plan.md`
  - `make-scenarios.md`
  - `go-live-checklist.md`
  - `modal-conversion-plan.md`
- `templates/`
  - `document-processing-hub-template.csv`
  - `coa-template.csv`
  - `approval-message-pack.md`
- `make/`
  - `scenario-1-document-intake.json`
  - `scenario-2-extraction-validation.json`
  - `scenario-3-exceptions-approval.json`
  - `scenario-4-archiving-reporting.json`

## V1 Principles
- Rule-based validation first.
- AI only for structured extraction and summarization where it adds clear value.
- Avoid over-engineering (no full ERP integration in first release).
