# FitGuard Hub - Beginner Setup (Copy/Paste + Click-by-Click)

## 1) Prerequisites
- Google account (Sheets + Calendar)
- Make.com account
- WhatsApp Business Cloud API access
- OpenAI API key
- Gym manager WhatsApp number for escalations/reports
- Payment links (Yoco / PayFast / Ozow)

## 2) Create Google Sheet Data Hub
1. Create sheet: `FitGuard Hub - [Gym Name]`.
2. Import `templates/fitguard-hub-template.csv`.
3. Create tabs:
   - Members
   - Attendance
   - Payments
   - Leads & Trials
   - Reactivation Campaigns
   - Classes/Schedule
   - Reports Log
4. Freeze row 1 in each tab.

## 3) Connect Apps in Make
Connect:
- Google Sheets
- Google Calendar
- WhatsApp Business Cloud
- OpenAI
Set timezone to `Africa/Johannesburg`.

## 4) Scenario 1 - WhatsApp AI Member Agent
Scenario name: `[Client] - WhatsApp AI Member Agent`

### Module Flow
1. WhatsApp Watch Incoming Messages
2. Set variable `normalized_phone`
```make
{{if(startsWith(replace(replace(trim(Phone);" ";"");"+";"");"0");concat("27";substring(replace(replace(trim(Phone);" ";"");"+";"");1));replace(replace(trim(Phone);" ";"");"+";""))}}
```
3. Search `Members` by phone
4. Search `Leads & Trials` by phone
5. Set context summary (status, expiry, last visit, payment state)
6. OpenAI intent + reply JSON
7. Router paths:
   - Book Class / Trial
   - Payment Inquiry
   - Check Attendance / Last Visit
   - Membership Renewal
   - Facility / Class Info
   - Complaint / Feedback (handoff)
   - Churned Reactivation Reply
8. Optional Calendar booking/check availability
9. Send WhatsApp reply
10. Update logs + relevant tabs
11. Error handler -> manager alert

## 5) Scenario 2 - Retention & Reporting Engine
Scenario name: `[Client] - Retention & Reporting Engine`

### Schedule
- Daily at 07:00
- Weekly on Monday (owner report + reactivation batch)

### Daily tasks
- Due and overdue payment reminders
- No-show follow-up for missed classes
- Failed debit order recovery prompts

### Weekly tasks
- Reactivation campaign to 20-50 churned members
- Owner WhatsApp performance summary

## 6) OpenAI prompts
Use `templates/openai-prompts.md` for:
- Main member agent prompt
- Reactivation prompt
- Daily owner report prompt

## 7) UAT Tests
Send these test messages:
1. "I want to book a class tomorrow"
2. "Did my payment go through?"
3. "When did I last check in?"
4. "I want to renew"
5. "I have a complaint"

Expected:
- Correct route
- Useful WhatsApp response
- Logging in Sheets
- Escalation when appropriate

## 8) SA-specific setup
- Prefer sending windows that avoid severe load-shedding times.
- Add STOP opt-out line for POPIA compliance.
- Use approved templates outside 24-hour WhatsApp service window.
