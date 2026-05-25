# Make.com Module Configuration Sheet (Click-by-Click)

This is the exact build sheet for Scenario A and B.
Use this with `implementation/make-scenario-blueprint.md`.

---

## Scenario A — Intake → Log → Owner Alert

## Module 1: Google Forms — Watch Responses
- App: **Google Forms**
- Trigger: **Watch Responses**
- Connection: Client Google account
- Form: `New Client Inquiry`
- Limit: 1 (during testing), then 10+ in production

### Output fields expected
- Full Name
- Phone Number
- Service Needed
- Suburb / Area
- Message / Details
- Budget

---

## Module 2: Tools — Set Multiple Variables
Set these variables:
- `created_at_utc` = `{{now}}`
- `source` = `Form`
- `raw_phone` = `{{1.Phone Number}}`

---

## Module 3: Tools — Text Parser / Replace (Phone Normalization)
Goal: strip spaces/symbols and convert local `0XXXXXXXXX` into `27XXXXXXXXX`.

### Step 1
- Input: `{{raw_phone}}`
- Replace regex: `[^0-9+]`
- Replace with: empty
- Output variable: `phone_clean`

### Step 2 (rule)
- If starts with `+` => remove plus
- If starts with `0` => replace leading 0 with 27
- Else keep digits
- Output variable: `phone_normalized`

---

## Module 4: Google Sheets — Search Rows (De-duplication)
- App: **Google Sheets**
- Action: **Search Rows**
- Spreadsheet: `Lead Log - Client Name`
- Sheet: `Lead Log`
- Max returned rows: 1

### Search logic
Find row where:
- `Phone (normalized)` equals `{{phone_normalized}}`
- AND `Created At (UTC)` within last 4 hours

---

## Module 5: Router — Duplicate vs Insert
Create two branches:

### Branch A (Duplicate)
Filter name: `duplicate_found`
Condition:
- Search result exists (row count > 0)

Action on this branch:
- Update found row `Notes` with: `Duplicate lead received at {{created_at_utc}}`
- Stop branch

### Branch B (Fresh lead)
Filter name: `no_duplicate`
Condition:
- Search result is empty

Action on this branch:
- Continue to Add Row module

---

## Module 6: Google Sheets — Add Row
Map columns exactly:
- Lead ID => leave blank (sheet formula)
- Created At (UTC) => `{{created_at_utc}}`
- Local Time (SAST) => leave blank (sheet formula)
- Source => `{{source}}`
- Lead Name => `{{1.Full Name}}`
- Phone (raw) => `{{1.Phone Number}}`
- Phone (normalized) => `{{phone_normalized}}`
- Email => blank unless form has it
- Service Needed => `{{1.Service Needed}}`
- Area/Suburb => `{{1.Suburb / Area}}`
- Message => `{{1.Message / Details}}`
- Budget => `{{1.Budget}}`
- Consent Captured (Y/N) => `Y` (if consent checkbox is present)
- Consent Timestamp => `{{created_at_utc}}`
- Status => `New`
- Owner Assigned => client owner name
- Automation Health => `OK`

---

## Module 7: Gmail — Send Email (Owner Alert)
- To: owner email
- Subject: `🚨 New Lead: {{1.Full Name}} — {{1.Service Needed}} in {{1.Suburb / Area}}`
- Body:
  - Name
  - Phone
  - Service
  - Area
  - Message
  - Created time
  - Link to Lead Sheet

---

## Module 8: Google Sheets — Update Row Health
- Update inserted row
- Set `Automation Health` = `OK`
- Optional: set `Notes` = `Owner alert sent at {{now}}`

---

## Error Handler Route (mandatory)
Attach handler to modules 6–8:
- On error:
  - Send admin email with module name + error details
  - If row exists, set `Automation Health` = `Error`

---

## Scenario B — Instant Acknowledgement

## Module 1: Google Sheets — Watch New Rows
- Watch rows in `Lead Log`
- Filter later to `Status = New`

## Module 2: Router — Business Hours Split
Create boolean condition based on SAST time.

### Branch A: In-hours
Condition example:
- Monday–Friday and time between 08:00 and 17:00

Action:
- Send in-hours acknowledgement template

### Branch B: After-hours
Condition:
- Outside in-hours window

Action:
- Send after-hours acknowledgement template

## Module 3: Send Template Message
Channel options:
- WhatsApp provider (if configured)
- Email fallback (if WhatsApp unavailable)

Template source: `build-artifacts/03-message-packs.md`

## Module 4: Google Sheets — Update Row
- Update `Notes` with ack timestamp/channel
- Optional: set `Last Follow-up At` = `{{now}}`

---

## Smoke Test Matrix (must pass)
1. Fresh lead inserts once.
2. Duplicate lead is flagged, not reinserted.
3. Owner alert email arrives.
4. In-hours ack template sent.
5. After-hours ack template sent.
6. Forced error triggers admin notification.
