# Complete Automation Suite Setup Guide (Beginner Edition)

> If you can copy/paste and click buttons, you can deploy this.
> This guide assumes **zero technical experience**.

---

## What You Are Building

You are setting up 3 ready-to-sell automation systems:

1. **Speed-to-Lead** (new lead gets instant WhatsApp reply)
2. **Follow-up & Nurture** (automatic Day1/Day3/Day7 follow-ups)
3. **Document Processing** (invoices/receipts intake, extraction, and alerts)

Everything uses:
- **Google Sheets** (your database)
- **Make.com** (your automation builder)
- **WhatsApp Business Cloud** (messaging)
- **Google Forms/Gmail/Drive** (inputs)

---

## Part A — 15-Minute Quick Start (Do This First)

### A1) Create a working folder in Google Drive
1. Open Google Drive.
2. Create folder: `Automation - Client Name`.
3. Inside it create:
   - `01 Leads`
   - `02 Documents`
   - `03 Archive`

### A2) Create your first Google Sheet
1. Create a Google Sheet named: `Client Name - Lead Log`.
2. Open this repo file: `speed-to-lead-automation/templates/leads-sheet-template.csv`.
3. In Google Sheets: **File -> Import -> Upload** that CSV.
4. Confirm row 1 has these headers (exact):
   - Lead ID, Timestamp, Source, Full Name, Phone, Email, Service Interest, Message, Budget, Timeline, Lead Score, Hot Lead, Status, Assigned To, Last Contacted, Next Follow-up, Booking Link Sent, Outcome, Notes

### A3) Create your intake form
1. Open Google Forms.
2. Create form: `Client Name - New Inquiry`.
3. Add questions:
   - Full Name
   - Phone
   - Email
   - Service Interest
   - Message
   - Budget
   - Timeline
4. Submit one test entry.

### A4) Create Make.com account + connections
In Make.com:
1. Go to **Connections**.
2. Add and authorize:
   - Google Sheets
   - Google Forms
   - WhatsApp Business Cloud
   - Google Drive
   - Gmail
   - OpenAI (optional until documents module)

✅ You are ready to build.

---

## Part B — How to Use Make.com (Super Simple)

## B1) What is a “Scenario”?
A Scenario is a flow chart:
- Trigger (something happens)
- Actions (do steps)

Example:
Google Form submitted -> save row -> send WhatsApp -> notify owner.

## B2) Golden rules in Make
1. Build **one scenario at a time**.
2. Click **Run once** before turning ON.
3. Map fields by clicking bubbles (don’t type random text).
4. Name every module clearly.
5. Keep timezone: `Africa/Johannesburg`.

## B3) Copy-paste expression blocks (you will use these)

### Lead ID
```make
LD-{{formatDate(now; "YYMMDD")}}-{{random}}
```

### Convert 0821234567 -> 27821234567
(Use in a Set Variable step named `normalized_phone`)
```make
{{if(startsWith(replace(replace(trim(Phone);" ";"");"+";"");"0");concat("27";substring(replace(replace(trim(Phone);" ";"");"+";"");1));replace(replace(trim(Phone);" ";"");"+";""))}}
```

### Current timestamp
```make
{{now}}
```

### Day-based follow-up dates
- +1 day
```make
{{addDays(now;1)}}
```
- +2 days
```make
{{addDays(now;2)}}
```
- +4 days
```make
{{addDays(now;4)}}
```
- +7 days
```make
{{addDays(now;7)}}
```

---

## Part C — System 1: Speed-to-Lead (Exact Click-by-Click)

Reference:
- `speed-to-lead-automation/docs/make-scenarios.md`
- `speed-to-lead-automation/templates/whatsapp-message-pack.md`

## C1) Create Scenario in Make
1. In Make, click **Create a new scenario**.
2. Name it: `[Client] - Incoming Leads Processor`.

## C2) Add Module 1 (Trigger)
1. Click `+`.
2. Search `Google Forms`.
3. Choose **Watch Responses**.
4. Connect your form `Client Name - New Inquiry`.
5. Save.

## C3) Add Module 2 (Lead ID)
1. Add module `Tools -> Set variable`.
2. Variable name: `lead_id`.
3. Value (copy/paste):
```make
LD-{{formatDate(now; "YYMMDD")}}-{{random}}
```
4. Save.

## C4) Add Module 3 (Phone Normalization)
1. Add module `Tools -> Set variable`.
2. Variable name: `normalized_phone`.
3. Value (copy/paste formula from Part B3 phone block).
4. Save.

## C5) Add Module 4 (Add row to Leads sheet)
1. Add `Google Sheets -> Add a Row`.
2. Choose spreadsheet: `Client Name - Lead Log`.
3. Sheet/tab: `Leads`.
4. Map fields:
   - Lead ID -> `lead_id`
   - Timestamp -> `now`
   - Full Name -> Form Full Name
   - Phone -> `normalized_phone`
   - Status -> `NEW`
   - Lead Score -> `3`
   - Hot Lead -> `NO`
   - Booking Link Sent -> `YES`
5. Save.

## C6) Add Module 5 (Router = hot lead check)
1. Add `Router`.
2. Create route `HOT` filter.
3. Filter condition on message text contains any:
   - urgent, today, asap, quote, pricing, ready, install, book now
4. Add second route `NORMAL` (no filter = fallback).

## C7) Add Module 6 (WhatsApp to lead)
1. On each route, add `WhatsApp Business Cloud -> Send Message`.
2. Recipient phone = `normalized_phone`.
3. Message: copy from `speed-to-lead-automation/templates/whatsapp-message-pack.md` (Instant Acknowledgment block).

## C8) Add Module 7 (WhatsApp owner alert)
1. Add second WhatsApp module after lead message.
2. Recipient = owner number (hardcoded once).
3. Message: use Owner Alert template.
4. For HOT route, prepend `🔥 NEW HOT LEAD`.

## C9) Add Module 8 (Update row status)
1. Add `Google Sheets -> Update a Row`.
2. Update same lead row:
   - Status = `CONTACTED`
   - Last Contacted = `{{now}}`
   - Lead Score = `8` if HOT else `3`
   - Hot Lead = `YES` if HOT else `NO`

## C10) Test it
1. Click **Run once**.
2. Submit test form.
3. Confirm:
   - row inserted,
   - lead got WhatsApp,
   - owner got alert,
   - row updated to CONTACTED.
4. Turn Scenario **ON**.

---

## Part D — System 2: Follow-up & Nurture (Copy/Paste Setup)

References:
- `follow-up-nurture-sequences/docs/make-scenarios.md`
- `follow-up-nurture-sequences/templates/leads-sheet-upgrade.csv`
- `follow-up-nurture-sequences/templates/follow-up-message-pack.md`

## D1) Add extra columns to Leads sheet
Add these columns exactly:
- Sequence Active
- Sequence Stage
- Follow-up Count
- Last Reply Date
- Replied
- Next Follow-up Date
- Last Follow-up Sent
- Follow-up Outcome

Default values for new leads:
- Sequence Active = YES
- Sequence Stage = Day1
- Follow-up Count = 0
- Replied = NO

## D2) Create Scenario 2: `[Client] - Follow-up Engine`

### Module 1: Scheduler
- Schedule 1: Weekdays 09:00
- Schedule 2: Weekdays 14:00
- Timezone: Africa/Johannesburg

### Module 2: Search rows
Use filter logic:
- Sequence Active = YES
- Replied != YES
- Next Follow-up Date <= now

### Module 3: Iterator
Process each result one by one.

### Module 4: Router by stage
Routes:
- Day1
- Day3
- Day7
- Final

### Module 5: Send WhatsApp follow-up
Copy messages from:
`follow-up-nurture-sequences/templates/follow-up-message-pack.md`

### Module 6: Update row after send
- Follow-up Count = +1
- Last Follow-up Sent = now
- Sequence Stage = next value
- Next Follow-up Date:
  - Day1 -> `{{addDays(now;2)}}`
  - Day3 -> `{{addDays(now;4)}}`
  - Day7 -> `{{addDays(now;7)}}`
  - Final -> Sequence Active = NO

## D3) Create Scenario 3: `[Client] - Reply Detection & Sequence Stopper`

### Module 1
WhatsApp Business Cloud -> Watch incoming messages

### Module 2
Normalize sender phone (same formula as Part B3)

### Module 3
Search lead by phone in Leads sheet

### Module 4
Update row:
- Replied = YES
- Sequence Active = NO
- Last Reply Date = now
- Follow-up Outcome = Interested

### Module 5
Send owner alert:
```
🔥 LEAD REPLIED
Name: {{name}}
Phone: {{phone}}
Reply: {{message}}
Follow up ASAP.
```

### D4) Test logic
- If lead replies: sequence must stop immediately.
- If no reply: sequence continues until Final.

---

## Part E — System 3: Document Processing (Beginner Mode)

References:
- `document-processing-automation/docs/make-scenarios.md`
- `document-processing-automation/templates/document-processing-hub-template.csv`
- `document-processing-automation/templates/coa-template.csv`
- `document-processing-automation/templates/approval-message-pack.md`

## E1) Create Google Sheet `Client Name - Document Processing Hub`
Tabs:
1. Incoming Documents
2. Exceptions
3. Chart of Accounts
4. Archive Log

Import template CSV headers from the two template files.

## E2) Scenario 1: `[Client] - Document Intake Pipeline`
1. Trigger: Gmail Watch Emails (has attachments)
2. Upload attachment to Drive folder `02 Documents`
3. Add row to Incoming Documents:
   - Source = Gmail
   - Status = Pending Extraction
   - File Link = uploaded file URL

## E3) Scenario 2: `[Client] - Data Extraction & Validation`
1. Search rows where Status = Pending Extraction
2. OCR extract text
3. OpenAI parse to JSON (use prompt in docs)
4. Validation router:
   - Missing VAT -> Exceptions
   - Duplicate invoice # -> Exceptions + alert
   - Amount above threshold -> Approval path
5. Categorize from Chart of Accounts keywords
6. Update Incoming Documents row with structured values

## E4) Scenario 3: `[Client] - Exception & Approval Workflow`
1. Search Exceptions rows
2. Route by type
3. Send WhatsApp message using templates:
   - Approval Needed
   - Duplicate Alert
   - OCR Failure Alert
4. Update exception status and notes

## E5) Scenario 4: `[Client] - Archiving & Reporting`
1. Move file to archive: `03 Archive/Processed/<Vendor>/<Year>/`
2. Add archive log row
3. Send daily summary WhatsApp to owner/accountant

---

## Part F — “Plugin-Style” Deployment Order (Copy This Checklist)

Use this exactly, top to bottom:

1. [ ] Import/create Leads sheet from template
2. [ ] Build Scenario: Incoming Leads Processor
3. [ ] Test 5 sample leads
4. [ ] Add follow-up columns
5. [ ] Build Scenario: Follow-up Engine
6. [ ] Build Scenario: Reply Detection Stopper
7. [ ] Test reply-stop behavior
8. [ ] Create Document Processing Hub sheet
9. [ ] Build Scenario: Document Intake Pipeline
10. [ ] Build Scenario: Extraction & Validation
11. [ ] Build Scenario: Exception & Approval
12. [ ] Build Scenario: Archiving & Reporting
13. [ ] Run UAT with client live
14. [ ] Turn all approved scenarios ON

---

## Part G — Troubleshooting (Most Common Problems)

## Problem 1: WhatsApp not sending
Check:
- phone is in `27XXXXXXXXX`
- WhatsApp connection token valid
- sender is approved in Meta

## Problem 2: Row not found during update
Check:
- you stored row ID when adding row
- update module is using that same row ID

## Problem 3: Follow-ups sending to replied leads
Check:
- Scenario 3 is ON
- Replied field is set to YES
- Scenario 2 filter excludes Replied = YES

## Problem 4: OCR output messy
Check:
- file quality (blurred photo?)
- use PDF where possible
- run OCR before OpenAI structuring

---

## Part H — What to Hand Over to Client

Give client:
1. Google Sheet links
2. Scenario names + what each does
3. Owner alert number configured
4. How to mark Won/Lost in Leads sheet
5. What to do when invoice flagged
6. Monthly support plan

---

## Final Note

Do not build extra complexity first.
Get this basic system live, stable, and producing results.
Then improve.
