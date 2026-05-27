# Make.com Scenarios - Real Estate Agent WhatsApp AI Blueprint

## Scenario 1: Main WhatsApp AI Agent (Core Intelligence)
1. WhatsApp Business Cloud -> Watch Incoming Messages
2. Google Sheets -> Search Rows (Leads by phone)
3. Tools -> Set Variable (conversation summary)
4. OpenAI -> Chat Completion (intent + reply)
5. Router:
   - Path A: Property Search
   - Path B: Booking Request
   - Path C: FAQ/General
   - Path D: Human Handoff
6. Google Calendar -> Search availability / Create event
7. WhatsApp Business Cloud -> Send message/template
8. Google Sheets -> Add/update in Leads, Viewings, Conversations
9. Error handler -> Agent alert with context

## Scenario 2: Follow-up & Pipeline Maintenance
1. Scheduler (Daily 08:00 or every 3 days)
2. Search stalled leads
3. Router by follow-up stage (Day 2 / Day 7 / Day 14)
4. OpenAI short personalization
5. WhatsApp send (template if outside 24-hour window)
6. Google Sheets pipeline update
7. Optional BI summary to agent
