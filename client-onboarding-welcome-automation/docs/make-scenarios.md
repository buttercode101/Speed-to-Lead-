# Make.com Scenarios - Client Onboarding & Welcome Automation

## Scenario 1: Client Onboarding Automation
1. Google Forms -> Watch New Responses from the onboarding/agreement form
2. Google Sheets -> Add row in `New Clients`
3. Google Drive -> Create client folder named `Client - {{Client Name}}`
4. Google Drive -> Copy template files into the client folder:
   - Welcome pack
   - Signed contract copy or agreement summary
   - Onboarding checklist
   - Access request form
5. Google Sheets -> Update `New Clients` with the client folder link
6. OpenAI -> Generate personalized Day 0 welcome email using the selected service package and client details
7. Gmail -> Send Day 0 welcome email with folder link and next steps
8. Google Sheets -> Add default onboarding tasks in `Onboarding Checklist`
9. Router:
   - If kickoff meeting required -> Google Calendar create event or send booking link
   - If first invoice required -> Gmail send invoice/payment link
   - If contract not signed -> Gmail send e-sign reminder
10. Gmail or Slack/Teams -> Send internal owner notification with client summary
11. Sleep/Delay -> Wait until Day 3
12. OpenAI -> Generate Day 3 check-in email
13. Gmail -> Send Day 3 follow-up
14. Sleep/Delay -> Wait until Day 7
15. Gmail -> Send Day 7 document/checklist reminder if onboarding is not complete
16. Error handler -> Send admin alert and log issue in `Reports`

### Suggested Default Checklist Tasks
- Confirm signed contract or agreement
- Confirm invoice/payment status
- Create client Drive folder
- Share welcome pack
- Book kickoff call
- Collect required access or documents
- Confirm service delivery owner
- Mark onboarding complete

## Scenario 2: Weekly Onboarding Status Report
1. Scheduler -> Every Monday 08:00
2. Google Sheets -> Search `New Clients` where `Onboarding Status` is not `Complete`
3. Google Sheets -> Search overdue tasks in `Onboarding Checklist`
4. OpenAI -> Summarize active onboarding clients, blockers, overdue items, and recommended actions
5. Gmail -> Send weekly owner report
6. Google Sheets -> Add row in `Reports`

## Router Rules
- `Contract Signed = No` -> Send contract/e-sign reminder and set `Onboarding Status = Waiting for Contract`
- `Payment Status = Unpaid` -> Send payment reminder and keep access limited
- `Payment Status = Paid` -> Continue access granting and kickoff preparation
- `Preferred Language = Afrikaans` -> Use Afrikaans email templates
- `Service Package` includes `Premium` or `Enterprise` -> Create higher-touch checklist and owner notification

## Error Handling
- If Drive folder creation fails, notify the owner and keep the client row status as `Setup Error`.
- If Gmail send fails, add a report note and alert the admin with the client email.
- If OpenAI personalization fails, use the standard email template fallback.
- If payment link is missing, send internal alert instead of sending an incomplete invoice email.
