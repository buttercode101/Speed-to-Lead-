# Make.com Scenario Specs - PropGuard AI System

## Scenario 1: WhatsApp AI Central Brain
1. WhatsApp Business Cloud -> Watch Incoming Messages
2. Tools -> Normalize phone variable
3. Google Sheets -> Search Rows (Tenants/Owners/Leads/Old Database)
4. OpenAI -> Intent + response generation
5. Router (7 intent branches)
6. WhatsApp Business Cloud -> Send reply
7. Google Sheets -> Update relevant tab
8. WhatsApp Business Cloud -> Manager escalation alert (conditional)

## Scenario 2: Scheduled Automations
1. Scheduler (Daily 08:00)
2. Rent reminder run (pre-due/due/overdue)
3. Maintenance status update run
4. Owner summary report run (daily/weekly)
5. Lead nurture run (Day1/Day3/Day7)
6. Monthly reactivation run (small batch)
7. Google Sheets logging for each run outcome
