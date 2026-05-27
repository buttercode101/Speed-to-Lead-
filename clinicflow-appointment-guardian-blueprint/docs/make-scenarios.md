# Make.com Scenarios - ClinicFlow Appointment Guardian

## Scenario 1: WhatsApp AI Patient Agent
1. WhatsApp Business Cloud -> Watch Incoming Messages
2. Google Sheets -> Search Rows (Patients by phone)
3. OpenAI -> Intent + context response
4. Router:
   - New Appointment
   - Reschedule/Cancel
   - Medical Query/Emergency (handoff)
   - Billing/Payment
   - Document Upload
   - General Inquiry
5. Google Calendar -> check/create event
6. WhatsApp -> send response/template
7. Google Sheets -> update patient/appointment/billing/lead records
8. Error handler -> receptionist alert

## Scenario 2: Automated Reminders + Daily Operations
1. Scheduler (Daily 07:00)
2. Pull appointments next 3 days + overdue bills
3. Iterator + reminder cadence (3d/24h/2h)
4. WhatsApp reminder sends
5. KPI aggregation
6. OpenAI daily owner report summary
7. WhatsApp owner report send
8. Write Daily Reports log
