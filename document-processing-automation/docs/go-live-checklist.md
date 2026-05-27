# Go-Live Checklist - Document Processing Automation

## Input Channels
- [ ] Gmail connection authorized and attachment filter tested
- [ ] WhatsApp media trigger connected (if used)
- [ ] Drive upload folder monitored and tested

## Data Model
- [ ] `Incoming Documents` tab created
- [ ] `Exceptions` tab created
- [ ] `Chart of Accounts` tab loaded
- [ ] `Archive Log` tab created

## Extraction & Validation
- [ ] OCR outputs readable text for sample PDF and photo receipt
- [ ] JSON extraction parses without errors
- [ ] Duplicate invoice detection tested
- [ ] Missing VAT route tested
- [ ] High-value approval threshold tested

## Workflow & Reporting
- [ ] Exception notifications delivered to owner
- [ ] Approval messages include vendor, amount, and reason
- [ ] Processed files moved to archive path
- [ ] Daily summary delivered successfully
