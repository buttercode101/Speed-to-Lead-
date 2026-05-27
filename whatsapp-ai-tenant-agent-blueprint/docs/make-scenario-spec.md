# Make.com Scenario Specification - WhatsApp AI Tenant Agent

## Scenario Name
`[Client] - WhatsApp AI Tenant Agent`

## Module Blueprint
1. WhatsApp Business Cloud -> Watch Incoming Messages
2. Tools -> Set Variable (normalized phone)
3. Google Sheets -> Search Rows (Tenants by phone)
4. Google Sheets -> Search Rows (Properties/Rent/Maintenance context)
5. Tools -> Set Variable (context summary)
6. OpenAI -> Create Chat Completion (intent + reply JSON)
7. Router (intent branches)
8. Branch actions by intent:
   - Rent Related
   - Maintenance Request
   - Lease / General
   - New Prospect / Viewing
   - Complaint / Escalation
   - Human Handoff
9. (Optional) OpenAI second pass for response refinement
10. WhatsApp Business Cloud -> Send Message
11. Google Sheets -> Add/Update (Conversation Log + relevant tabs)
12. Error Handler -> manager escalation + log failure

## Router Outcomes
- rent_related
- maintenance_request
- lease_general
- new_prospect
- complaint_escalation
- human_handoff

## Free-Tier Optimization
- Use keyword pre-check before OpenAI where possible
- Skip second OpenAI call unless quality issues
- Batch non-urgent updates via scheduled scenario if volume grows
