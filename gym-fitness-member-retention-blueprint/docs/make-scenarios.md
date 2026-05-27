# Make.com Scenarios - FitGuard Member Retention Engine

## Scenario 1: WhatsApp AI Member Agent
1. WhatsApp Business Cloud -> Watch Incoming Messages
2. Google Sheets -> Search Rows (Members + Leads & Trials)
3. Tools -> Set Variable (context summary)
4. OpenAI -> Chat Completion (intent + reply)
5. Router paths:
   - Book Class / Trial
   - Payment Inquiry
   - Attendance / Last Visit
   - Membership Renewal
   - Facility / Class Info
   - Complaint / Feedback (handoff)
   - Churned Reactivation Reply
6. Google Calendar -> check/create booking (if needed)
7. WhatsApp -> send reply
8. Google Sheets -> log conversation + update relevant records
9. Error handler -> manager alert

## Scenario 2: Retention & Reporting Engine
1. Scheduler (Daily 07:00 + Weekly Monday)
2. Payments reminders (due/overdue/failed)
3. No-show follow-ups
4. Weekly reactivation batch (20-50 members)
5. KPI aggregation
6. OpenAI -> owner report summary
7. WhatsApp -> send owner report
8. Google Sheets -> write to Reports Log + Campaign tab
