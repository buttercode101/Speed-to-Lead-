# Complete Automation Suite Setup Guide (Start to Finish)

This guide walks you through **exactly** how to deploy the 3 systems in this repository:

1. `speed-to-lead-automation`
2. `follow-up-nurture-sequences`
3. `document-processing-automation`

It is written for a non-technical operations/admin user and is intended to be followed in order.

---

## 0) Before You Start (Prerequisites)

## Accounts you need
1. Google account (for Sheets, Forms, Drive, Calendar, Gmail).
2. Make.com account.
3. Meta/WhatsApp Business Cloud API account (with verified sender).
4. OpenAI API key (only required for document extraction phase and optional AI layers).

## Access you need from the client
1. Owner/manager WhatsApp number for alerts.
2. Business name, service list, and booking link.
3. Access to client Google Workspace assets (or permission to create new ones).
4. Approval threshold for document exceptions (example: R10,000).

## Folder assets in this repo
- Speed-to-Lead blueprint: `speed-to-lead-automation/`.
- Follow-up/Nurture blueprint: `follow-up-nurture-sequences/`.
- Document processing blueprint: `document-processing-automation/`.

---

## 1) Global Environment Setup (One-Time)

### Step 1.1 — Create Make connections
In Make.com, create and test these connections:
1. Google Sheets
2. Google Forms
3. Google Drive
4. Gmail
5. WhatsApp Business Cloud
6. OpenAI (for document extraction only)

**Success check:** each connection shows "Connected" in Make.

### Step 1.2 — Standard naming convention
Use this pattern everywhere:
- Scenario name: `[Client] - <Scenario Name>`
- Sheet name: `<Client> - Automation Hub`
- Drive root folder: `<Client>/2026/`

This avoids confusion when you scale to multiple clients.

### Step 1.3 — Timezone standardization
Set all scenarios to:
- `Africa/Johannesburg`

This keeps follow-up timings aligned with South African business hours.

### Step 1.4 — Phone normalization rule
Standardize all lead/customer numbers to E.164 SA format:
- Input: `0821234567`
- Output: `27821234567`

Apply this rule in **every** scenario that matches or sends by phone.

---

## 2) System 1 Setup — Speed-to-Lead Automation

Reference files:
- `speed-to-lead-automation/README.md`
- `speed-to-lead-automation/docs/make-scenarios.md`
- `speed-to-lead-automation/templates/leads-sheet-template.csv`
- `speed-to-lead-automation/templates/whatsapp-message-pack.md`

### Step 2.1 — Create Google Sheet (Leads CRM)
1. Create a new Google Sheet named: `<Client> - Lead Log`.
2. Create tab `Leads`.
3. Import columns from `templates/leads-sheet-template.csv`.
4. Freeze row 1.
5. Format timestamp columns (`Timestamp`, `Last Contacted`, `Next Follow-up`) as date-time.

### Step 2.2 — Create Google Form intake
1. Create Google Form: `<Client> - New Inquiry`.
2. Add fields:
   - Full Name
   - Phone
   - Email
   - Service Interest
   - Message
   - Budget
   - Timeline
3. Submit one test response.

### Step 2.3 — Build Scenario 1 in Make
Use module order from `docs/make-scenarios.md`:
1. Google Forms: Watch Responses
2. Tools: Set Lead ID (`LD-YYMMDD-random`)
3. Text transform: normalize phone
4. Google Sheets: Add row
5. Router: hot keyword filter
6. WhatsApp: send instant lead reply
7. WhatsApp: send owner alert
8. Google Sheets: update row (status/contacted/score)

### Step 2.4 — Configure defaults
For all new leads set:
- `Status = NEW`
- `Lead Score = 3`
- `Hot Lead = NO`
- `Booking Link Sent = YES`

### Step 2.5 — Configure hot keyword route
Use these keywords:
- urgent, today, asap, quote, pricing, ready, install, book now

If match:
- score 8–10, hot lead YES.
Else:
- score 3–5, hot lead NO.

### Step 2.6 — Test end-to-end (required)
Run 5 test submissions:
1. normal lead
2. hot keyword lead
3. phone with spaces and plus
4. missing optional email
5. long message text

**Pass criteria:**
- Row created every time.
- Lead receives WhatsApp reply.
- Owner receives alert.
- Status becomes CONTACTED.

---

## 3) System 2 Setup — Follow-up & Nurture Sequences

Reference files:
- `follow-up-nurture-sequences/docs/make-scenarios.md`
- `follow-up-nurture-sequences/templates/leads-sheet-upgrade.csv`
- `follow-up-nurture-sequences/templates/follow-up-message-pack.md`

### Step 3.1 — Upgrade Leads sheet columns
Add these columns to `Leads`:
- Sequence Active
- Sequence Stage
- Follow-up Count
- Last Reply Date
- Replied
- Next Follow-up Date
- Last Follow-up Sent
- Follow-up Outcome

Initialize defaults for existing open leads:
- Sequence Active = YES
- Sequence Stage = Day1
- Follow-up Count = 0
- Replied = NO

### Step 3.2 — Build Scenario 2 (Follow-up Engine)
1. Scheduler module.
2. Configure two weekday runs:
   - 09:00
   - 14:00
3. Search rows filter:
   - Sequence Active = YES
   - Replied != YES
   - Next Follow-up Date <= NOW
4. Iterator.
5. Router by stage (Day1 / Day3 / Day7 / Final).
6. WhatsApp send follow-up.
7. Update row:
   - Follow-up Count +1
   - Last Follow-up Sent = now
   - Sequence Stage -> next
   - Next Follow-up Date -> calculated

### Step 3.3 — Stage timing logic
- Day1 -> +24 hours
- Day3 -> +2 days
- Day7 -> +4 days
- Final -> +7 days (or close sequence based on your policy)

### Step 3.4 — Build Scenario 3 (Reply Detection Stopper)
1. WhatsApp watch incoming messages.
2. Normalize inbound phone.
3. Search lead by phone.
4. Update lead:
   - Replied = YES
   - Sequence Active = NO
   - Last Reply Date = now
5. Send owner alert with reply body.

### Step 3.5 — Validate stop behavior
Test cases:
1. lead replies after Day1 -> Day3 should not send.
2. lead never replies -> receives full sequence.
3. unknown inbound number -> route to review queue.

---

## 4) System 3 Setup — Document Processing Automation

Reference files:
- `document-processing-automation/docs/make-scenarios.md`
- `document-processing-automation/templates/document-processing-hub-template.csv`
- `document-processing-automation/templates/coa-template.csv`
- `document-processing-automation/templates/approval-message-pack.md`

### Step 4.1 — Create Document Processing Hub sheet
Create `<Client> - Document Processing Hub` with tabs:
1. Incoming Documents
2. Exceptions
3. Chart of Accounts
4. Archive Log

Load template headers from:
- `document-processing-hub-template.csv`
- `coa-template.csv`

### Step 4.2 — Create Drive folder structure
Create folders:
- `<Client>/2026/May/Invoices/`
- `<Client>/Processed/`

Use year/month hierarchy for scalability.

### Step 4.3 — Build Scenario 1 (Intake)
1. Trigger source (start with Gmail attachments).
2. Filter file types: PDF/JPG/PNG/DOC.
3. Upload to Drive intake folder.
4. Add row in Incoming Documents with:
   - Status = Pending Extraction
   - Source = Gmail/WhatsApp/Drive
   - File link

### Step 4.4 — Build Scenario 2 (Extraction & Validation)
1. Search pending rows (`Status = Pending Extraction`).
2. OCR extract text.
3. OpenAI structured extraction (JSON).
4. Validate rules:
   - missing VAT -> exception
   - duplicate invoice number -> exception
   - amount > threshold -> approval route
5. Categorize via keyword mapping from Chart of Accounts.
6. Update incoming row with extracted fields + final status.

### Step 4.5 — Build Scenario 3 (Exception & Approval)
1. Search `Exceptions` rows with Status = Exception.
2. Route by type: duplicate/missing data/unreadable/high value.
3. Send owner/accountant WhatsApp using templates.
4. Write back decision/action notes to Exceptions tab.

### Step 4.6 — Build Scenario 4 (Archiving & Reporting)
1. Move processed files to `Processed/<Vendor>/<Year>/`.
2. Add row in Archive Log.
3. Aggregate daily metrics.
4. Send daily summary to owner/accountant.

---

## 5) Production Hardening Checklist (All Systems)

### Logging
- Every action must update a Sheet row.
- No silent failures.

### Error handling
- Add fallback branch in each scenario:
  - on error -> notify owner/admin with module name and error message.

### Rate/cost control
- Avoid per-minute polling.
- Keep to scheduled batches where possible.
- Prevent duplicate lookups/searches.

### Security
- Store API keys in Make secure connections only.
- Restrict sheet access to client stakeholders.

### Change management
- Version your scenario names: `v1`, `v1.1`.
- Clone before major edits.

---

## 6) UAT Script (Client Acceptance Test)

Run this in one session with the client:
1. Submit new lead -> verify instant WhatsApp and owner alert.
2. Advance clock or adjust dates -> verify Day1 follow-up.
3. Reply from lead phone -> verify sequence stops and owner notified.
4. Email an invoice attachment -> verify intake row created.
5. Process pending docs -> verify extraction and validation.
6. Trigger exception (missing VAT/duplicate) -> verify alert.
7. Process success case -> verify archive path + summary entry.

Client signs off only after all steps pass.

---

## 7) Recommended Rollout Plan (Per Client)

Week 1:
- Deploy Speed-to-Lead only.

Week 2:
- Enable Follow-up/Nurture + reply stopper.

Week 3:
- Deploy Document Processing intake + validation.

Week 4:
- Add optional AI polish and daily management summaries.

This staggered approach reduces risk and support overhead.

---

## 8) Optional AI Layers (Only After Stability)

Use AI for:
- follow-up personalization
- document structuring
- daily summaries

Do **not** use AI for:
- core routing
- approval decisions
- deterministic status transitions

Rule-first architecture stays cheaper and more reliable.

---

## 9) Final Handover Package

Before go-live handover, provide client with:
1. Scenario list + purpose.
2. Google Sheet links.
3. Field dictionary (what each status means).
4. Error alert recipients.
5. SLA expectations (response/ops windows).
6. 1-page SOP: "What to do when a lead replies".
7. 1-page SOP: "What to do when an invoice is flagged".

This is what makes the automation operational, not just technical.
