# ClinicFlow Hub - Beginner Setup (Copy/Paste + Click-by-Click)

## 1) Prerequisites
- Google account (Sheets + Calendar + Drive)
- Make.com account
- WhatsApp Business Cloud API access
- OpenAI API key
- Clinic owner/manager WhatsApp number
- Payment links (PayFast / Yoco / Ozow)

## 2) Create Google Sheet Data Hub
1. Create sheet: `ClinicFlow Hub - [Clinic Name]`.
2. Import `templates/clinicflow-hub-template.csv`.
3. Create tabs:
   - Patients
   - Appointments
   - Leads
   - Documents
   - Billing
   - Daily Reports
4. Freeze row 1 in each tab.

## 3) Connect Apps in Make
Connect:
- Google Sheets
- Google Calendar
- Google Drive (for docs)
- WhatsApp Business Cloud
- OpenAI
Set timezone to `Africa/Johannesburg`.

## 4) Scenario 1 - WhatsApp AI Patient Agent
Scenario name: `[Client] - WhatsApp AI Patient Agent`

### Module Flow
1. WhatsApp Watch Incoming Messages
2. Normalize phone variable
3. Search Patients by phone
4. Search Appointments/Billing by phone
5. OpenAI intent + response draft
6. Router paths:
   - New appointment request
   - Reschedule/cancel
   - Medical query/emergency -> handoff
   - Billing/payment inquiry
   - Document upload
   - General inquiry
7. Google Calendar check availability/create event
8. WhatsApp send response
9. Update Sheets (patients, appointments, billing, leads log)
10. Error handler -> receptionist alert

## 5) Scenario 2 - Automated Reminders + Daily Ops
Scenario name: `[Client] - Automated Reminders + Daily Ops`

### Schedule
- Daily at 07:00

### Flow
1. Get appointments for next 3 days
2. Get overdue bills
3. Iterator for reminders:
   - 3 days before
   - 24 hours before
   - 2 hours before
4. Send WhatsApp reminder
5. Aggregate KPIs:
   - appointments today
   - expected revenue
   - no-shows
   - new leads
   - overdue accounts
6. OpenAI daily owner summary
7. Send owner report via WhatsApp
8. Log to Daily Reports tab

## 6) Compliance & Safety
- Never provide medical advice in AI replies.
- Route emergency/pain keywords to human immediately.
- Keep minimal sensitive information in Sheets.
- Add opt-out and consent wording for POPIA.

## 7) UAT Tests
Test messages:
1. "I want to book a dental cleaning"
2. "I need to reschedule my appointment"
3. "I have severe pain"
4. "Can I pay my invoice now?"
5. "Where do I send my consent form?"

Expected:
- Correct route selection
- Proper escalation for urgent medical content
- Appointment rows updated
- Billing reminders sent correctly
- Report generated and sent
