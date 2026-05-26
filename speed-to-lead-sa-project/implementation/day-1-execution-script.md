# Day-1 Execution Script (60-Minute Launch)

Use this exactly in order. Do not skip steps.

## 0) Inputs you must have before starting (3 min)
- Client business name
- Owner email
- Admin/backup email
- Primary + backup responder numbers
- SLA minutes (recommended 5)

---

## 1) Generate client package (2 min)
Run:
```bash
python3 tools/setup_assistant.py \
  --business-name "CLIENT NAME" \
  --owner-email "owner@client.co.za" \
  --admin-email "ops@client.co.za" \
  --primary-contact "+27XXXXXXXXX" \
  --backup-contact "+27XXXXXXXXX" \
  --response-sla-minutes 5
```

Expected output files in `generated/`:
- `<client>-lead-log-template.csv`
- `<client>-google-apps-script.js`
- `<client>-deployment-manifest.json`
- `<client>-operator-packet.md`
- `<client>-setup-summary.json`

---

## 2) Create Google Sheet (5 min)
1. Create Google Sheet: `Lead Log - <Client Name>`
2. File → Import → Upload `generated/<client>-lead-log-template.csv`
3. Ensure first row contains headers and one sample row.

Checkpoint:
- Sheet tab exists and is named `Lead Log`

---

## 3) Install Apps Script (8 min)
1. In Google Sheet: Extensions → Apps Script
2. Replace default code with `generated/<client>-google-apps-script.js`
3. Save
4. Run function: `install()`
5. Grant permissions

Checkpoint:
- `install()` succeeds with no runtime errors
- Status dropdown exists in column O
- Formula cells populated in A2/C2/G2/R2/S2

---

## 4) Verify triggers (2 min)
In Apps Script → Triggers, confirm:
- `escalationWatchdog` every 5 minutes
- `weeklyKpiDigest` Monday 08:00

Checkpoint:
- both triggers active

---

## 5) Create Google Form (6 min)
Create form: `New Client Inquiry`
Fields:
- Full Name
- Phone Number
- Service Needed
- Suburb / Area
- Message / Details
- Budget

Checkpoint:
- submit URL copied

---

## 6) Build Make Scenario A (15 min)
Follow `implementation/make-module-config-sheet.md` exactly:
1. Google Forms: Watch Responses
2. Set vars (`created_at_utc`, `source`, `raw_phone`)
3. Normalize phone
4. Search rows (dedupe)
5. Router (duplicate vs fresh)
6. Add row
7. Send owner alert
8. Update row health
9. Error handler on modules 6–8

Checkpoint:
- Scenario A ON

---

## 7) Build Make Scenario B (10 min)
1. Watch new rows in `Lead Log`
2. Filter `Status = New`
3. Router by business hours (in-hours/after-hours)
4. Send acknowledgement template
5. Update row notes

Checkpoint:
- Scenario B ON

---

## 8) 3-test smoke run (6 min)
Submit 3 test leads:
1. Normal lead
2. Duplicate lead (same phone within 4h)
3. Urgent keyword lead

Must pass:
- New lead inserted once
- Duplicate flagged (not duplicated)
- Owner alert email received
- Acknowledgement sent
- No silent failures

---

## 9) Go-live gate (3 min)
Run `implementation/go-live-checklist.md` and confirm all pre-go-live boxes checked.

If any box fails:
- do not go live
- fix and retest

---

## 10) End-of-Day deliverables to client (5 min)
Send client:
- Form link
- Lead sheet link
- SLA definition
- Escalation contacts
- First weekly KPI report schedule

Archive in your folder:
- `generated/<client>-operator-packet.md`
- `generated/<client>-setup-summary.json`
- screenshots of successful smoke tests

---


## 11) Build Client Dashboard (4 min)
1. Add Apps Script file from `implementation/dashboard-bootstrap.js`.
2. Run `createDashboard()` once.
3. Confirm Dashboard tab appears with KPI values.
4. Share Dashboard tab view-only with client stakeholders.

Checkpoint:
- Dashboard shows Total Leads, Contact Rate, Close Rate, Median Response, SLA Met.

---
## Red-line rules (non-negotiable)
- Never go live before duplicate test passes.
- Never go live before escalation trigger is confirmed.
- Never promise ROI before baseline week data exists.
