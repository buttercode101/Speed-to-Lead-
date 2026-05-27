# WhatsApp AI Tenant Agent - Beginner Setup (Copy/Paste)

If you can click buttons and copy/paste text, you can deploy this.

## 1) What You Need
- Google account (Sheets + Drive)
- Make.com account
- WhatsApp Business Cloud API account
- OpenAI API key
- Property manager WhatsApp number (for escalations)
- Payment link(s): PayFast or Yoco

## 2) Create Google Sheet Data Hub
1. Create a Google Sheet named: `Tenant Agent Hub - [Client Name]`.
2. Import `templates/google-sheets-tabs-template.csv`.
3. Create tabs based on section names:
   - Tenants
   - Properties
   - Maintenance
   - Rent Payments
   - Conversation Log
4. In each tab, freeze header row.

## 3) Create Make Connections
In Make.com > Connections, connect:
- Google Sheets
- WhatsApp Business Cloud
- OpenAI

Set timezone to `Africa/Johannesburg`.

## 4) Build Main Scenario
Scenario name: `[Client] - WhatsApp AI Tenant Agent`

### Module 1: Trigger
- WhatsApp Business Cloud -> Watch Incoming Messages

### Module 2: Phone Normalization
- Tools -> Set variable
- Variable name: `normalized_phone`
- Value:
```make
{{if(startsWith(replace(replace(trim(Phone);" ";"");"+";"");"0");concat("27";substring(replace(replace(trim(Phone);" ";"");"+";"");1));replace(replace(trim(Phone);" ";"");"+";""))}}
```

### Module 3: Search Tenant Context
- Google Sheets -> Search Rows
- Tab: `Tenants`
- Match: Phone = `normalized_phone`

### Module 4: Pull Extra Context
Add Google Sheets search modules for:
- `Properties` by tenant phone/property ID
- `Maintenance` by tenant phone where status != Closed
- `Rent Payments` by tenant phone latest row

### Module 5: Set Context Variable
- Tools -> Set variable
- Name: `context_summary`
- Include:
  - tenant name
  - property
  - rent amount
  - due date
  - amount due
  - open tickets count

### Module 6: OpenAI Intent + Draft Reply
- OpenAI -> Create Chat Completion
- System prompt: copy from `templates/system-prompt.md`
- User input: incoming WhatsApp message + context_summary
- Ask model to return JSON:
  - intent
  - reply_text
  - urgency
  - escalate

### Module 7: Router by Intent
Create branches:
1. rent_related
2. maintenance_request
3. lease_general
4. new_prospect
5. complaint_escalation
6. human_handoff

### Module 8: Path Actions

#### Rent Path
- Read latest balance from Rent Payments
- Compose rent reminder + payment link
- Update/add Rent Payments row

#### Maintenance Path
- Add row to Maintenance tab
- Generate ticket ID:
```make
PM-{{formatDate(now; "YYMMDD")}}-{{random}}
```
- Send acknowledgement and ask for photo if missing

#### Lease/General Path
- Respond using known lease/property details
- Escalate if uncertain

#### New Prospect Path
- Add row to Tenants or lead intake process (based on your ops policy)
- Send viewing next-step response

#### Complaint/Escalation Path
- Send empathetic acknowledgement
- Mark escalation required

#### Human Handoff Path
- Send manager WhatsApp alert with:
  - name
  - number
  - issue summary
  - urgency

### Module 9: Optional OpenAI Refinement
- Optional second OpenAI call to polish message tone under 130 words.

### Module 10: Send WhatsApp Reply
- WhatsApp Business Cloud -> Send Message
- Recipient: `normalized_phone`
- Message: final reply text

### Module 11: Conversation Logging
- Google Sheets -> Add Row to `Conversation Log`
- Save:
  - timestamp
  - phone
  - incoming message
  - AI reply
  - intent
  - outcome

### Module 12: Error Handler
- Add fallback error route:
  - Send manager alert with module and error details
  - Log failure in Conversation Log outcome

## 5) Copy/Paste System Prompt
Use `templates/system-prompt.md` exactly first. Tune later only after stable testing.

## 6) Testing (Must Pass)
Run these test messages from a phone:
1. “How much is my rent this month?”
2. “I paid already, here is my POP.”
3. “My geyser is leaking.”
4. “When does my lease end?”
5. “I want to view a unit.”
6. “I’m unhappy and want to complain.”

Expected result:
- Correct route selected
- WhatsApp reply sent
- Sheet log row added
- Escalation alert sent when needed

## 7) Go-Live
1. Turn scenario ON.
2. Monitor first 72 hours morning + afternoon.
3. Fix wrong-intent routing quickly.
4. Keep replies short and practical.

## 8) POPIA + Window Rules
- Add consent wording in onboarding message.
- Include opt-out line: “Reply STOP to opt out.”
- Use approved WhatsApp templates outside the 24-hour session window.
