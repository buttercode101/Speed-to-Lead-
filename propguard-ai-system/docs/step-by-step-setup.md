# PropGuard AI System - Beginner Step-by-Step Setup (Copy/Paste Friendly)

This guide assumes you have never built on Make before.

## 1) Accounts & Access Checklist
- Google account (Sheets/Drive/Gmail)
- Make.com account
- WhatsApp Business Cloud account
- OpenAI API key
- Property manager owner WhatsApp number
- Payment links (PayFast or Yoco)

## 2) Create the Master Sheet
1. Create Google Sheet: `PropGuard Master Hub - [Client Name]`.
2. Import `templates/propguard-master-hub-template.csv`.
3. Create tabs from row section headers:
   - Properties
   - Tenants
   - Rent & Payments
   - Maintenance
   - Owners
   - Leads & Prospects
   - Old Database
   - Documents
   - Reports Log
4. Freeze header row in each tab.

## 3) Connect Apps in Make
In Make -> Connections, connect:
- Google Sheets
- Google Drive
- Gmail
- WhatsApp Business Cloud
- OpenAI

Set all scenario timezone settings to `Africa/Johannesburg`.

## 4) Build Scenario 1 - WhatsApp AI Central Brain
Scenario name: `[Client] - PropGuard AI Central Brain`

### Module 1: Trigger
- App: WhatsApp Business Cloud
- Event: Watch Incoming Messages

### Module 2: Normalize Phone
- App: Tools -> Set Variable
- Variable: `normalized_phone`
- Value:
```make
{{if(startsWith(replace(replace(trim(Phone);" ";"");"+";"");"0");concat("27";substring(replace(replace(trim(Phone);" ";"");"+";"");1));replace(replace(trim(Phone);" ";"");"+";""))}}
```

### Module 3: Search Contact Context
- App: Google Sheets -> Search Rows
- Search in tabs: Tenants, Owners, Leads & Prospects, Old Database
- Match field: Phone = `normalized_phone`

### Module 4: OpenAI Intent Analysis
- App: OpenAI -> Create Chat Completion
- Model: low-cost model (e.g. gpt-4.1-mini or equivalent)
- System prompt: copy from `templates/openai-prompts.md`
- Input: incoming message + row context
- Required output JSON fields:
  - intent
  - urgency
  - reply_text
  - handoff_required
  - target_tab

### Module 5: Router (7 Paths)
Create router branches by intent:
1. rent_inquiry_or_payment
2. maintenance_request
3. lease_or_general_query
4. new_lead
5. reactivation_reply
6. document_upload
7. human_handoff

### Module 6: Send WhatsApp Reply
- App: WhatsApp Business Cloud -> Send Message
- Recipient: normalized_phone
- Message: `reply_text`
- Keep under 130 words

### Module 7: Write Back to Sheet
- Update appropriate tab based on `target_tab`
- Log fields: timestamp, phone, intent, summary, status

### Module 8: Escalation (if needed)
If `handoff_required = true`:
- Send owner/manager WhatsApp alert with lead/tenant details and message summary.

Run test cases:
- "I need to pay rent" -> rent path
- "My geyser is leaking" -> maintenance path
- "Can I view this unit?" -> new lead path

## 5) Build Scenario 2 - Scheduled Automations
Scenario name: `[Client] - PropGuard Scheduled Automations`

### Module 1: Scheduler
- Run daily at 08:00
- Timezone: Africa/Johannesburg

### Module 2: Rent Reminders
- Search Tenants where:
  - pre-due (2 days before due)
  - due today
  - overdue (1/3/7+ days)
- Send tiered WhatsApp reminders with payment links (PayFast/Yoco)
- Update Rent & Payments tab with reminder status

### Module 3: Maintenance Status Updates
- Search Maintenance where status = Open/In Progress
- Send status message to tenant
- Escalate if SLA breach

### Module 4: Owner Reports
- Aggregate metrics:
  - occupancy
  - collection rate
  - overdue count
  - open maintenance tickets
  - estimated cash flow
- Send WhatsApp summary to owner(s)
- Log report in Reports Log

### Module 5: Lead Follow-up Sequences
- Search Leads & Prospects where follow-up due
- Send Day1/Day3/Day7 message
- Update next follow-up date

### Module 6: Monthly Reactivation Batch
- On the 1st of month, pull small batch from Old Database
- Send reactivation message
- Log results in Old Database and Reports Log

## 6) Templates to Copy/Paste
Use these files directly:
- `templates/whatsapp-message-pack.md`
- `templates/openai-prompts.md`

## 7) Testing Checklist (Must Pass)
- Incoming WhatsApp gets response in <2 min
- Rent reminder includes correct payment link
- Maintenance request generates ticket ID
- Owner gets daily summary
- Reactivation sends only to monthly batch size

## 8) Go Live
1. Turn Scenario 1 ON.
2. Turn Scenario 2 ON.
3. Monitor first 48 hours twice daily.
4. Fix mapping gaps immediately.

## 9) Weekly Optimization Routine
- Check failed operations in Make
- Review overdue rent conversions
- Review maintenance SLA misses
- Refine message templates
- Refine OpenAI prompt for clarity and fewer handoffs
