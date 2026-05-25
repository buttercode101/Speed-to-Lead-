# Quick Start (Do-as-little-as-possible Setup)

## 1) Google Sheet bootstrap (5 minutes)
1. Create a Google Sheet named `Lead Log - Client Name`.
2. Import `implementation/lead-log-template.csv` as the first sheet.
3. Open Extensions → Apps Script.
4. Paste `implementation/google-apps-script-template.js` contents.
5. Update `CONFIG` values (emails, business name, SLA).
6. Run `install()` once.

## 2) Google Form bootstrap (5 minutes)
Create a form named `New Client Inquiry` with fields:
- Full Name
- Phone Number
- Service Needed
- Suburb / Area
- Message / Details
- Budget

## 3) Make scenario bootstrap (15–25 minutes)
1. Open `implementation/make-import-template.json` for module order.
2. Build Scenario A exactly by module sequence.
3. Build Scenario B for acknowledgements.
4. Test with 3 form submissions (normal, duplicate, urgent text).

## 4) Turn on safety controls
- Confirm escalation trigger exists in Apps Script triggers.
- Confirm weekly digest trigger exists.
- Confirm owner and admin emails receive test messages.

## 5) Go live
Use `implementation/go-live-checklist.md` and check every box before client launch.
