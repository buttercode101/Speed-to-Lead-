# Real Estate Agent WhatsApp AI Agent - Beginner Setup (Copy/Paste + Click-by-Click)

This guide assumes zero technical background.

## 1) What You Need Before Starting
- Google account (Sheets + Calendar)
- Make.com account
- WhatsApp Business Cloud API access
- OpenAI API key
- Agent WhatsApp number for escalations
- Agency info:
  - areas covered
  - services offered
  - booking hours
  - disclaimers

## 2) Create the Master Sheet
1. Create a Google Sheet named: `Real Estate Agent Hub - [Client Name]`.
2. Import file: `templates/real-estate-agent-hub-template.csv`.
3. Create tabs from section names:
   - Leads
   - Listings
   - Viewings
   - Conversations
   - System Knowledge
4. Freeze row 1 in each tab.
5. Share edit access with the client.

## 3) Connect Apps in Make
In Make -> Connections, connect:
- Google Sheets
- Google Calendar
- WhatsApp Business Cloud
- OpenAI

Set timezone in scenarios to `Africa/Johannesburg`.

## 4) Build Scenario 1 (Main WhatsApp AI Agent)
Scenario name: `[Client] - Main WhatsApp AI Agent`

### Module 1: Trigger
- WhatsApp Business Cloud -> Watch Incoming Messages

### Module 2: Normalize Phone
- Tools -> Set Variable
- Name: `normalized_phone`
- Value:
```make
{{if(startsWith(replace(replace(trim(Phone);" ";"");"+";"");"0");concat("27";substring(replace(replace(trim(Phone);" ";"");"+";"");1));replace(replace(trim(Phone);" ";"");"+";""))}}
```

### Module 3: Pull Lead Context
- Google Sheets -> Search Rows (Leads)
- Match: Phone = `normalized_phone`

### Module 4: Pull Conversation Memory
- Google Sheets -> Search Rows (Conversations)
- Match: Phone = `normalized_phone`
- Sort latest first, keep recent rows summary

### Module 5: Set Context Variable
- Tools -> Set Variable: `context_summary`
- Include:
  - name
  - inquiry type
  - budget
  - location
  - property type
  - timeline
  - last conversation notes

### Module 6: OpenAI Intent + Draft Reply
- OpenAI -> Create Chat Completion
- System prompt: copy from `templates/system-prompt.md`
- Input: incoming message + context_summary
- Output JSON fields:
  - intent
  - missing_fields
  - reply_text
  - lead_score
  - handoff_required

### Module 7: Router (4 main paths)
1. Property Search
2. Booking Request
3. FAQ/General
4. Human Handoff

### Module 8A: Property Search Path
- Google Sheets -> Search Rows (Listings)
- Filters:
  - Status = Available
  - Location matches lead area
  - Price <= budget (or within range)
- Select top 2–3 listings
- Send WhatsApp with short summaries + image links
- Update Leads status: `MATCHED`

### Module 8B: Booking Request Path
- Google Calendar -> Search Availability
- Propose 3 viewing slots
- If lead confirms slot:
  - Google Calendar -> Create Event
  - Google Sheets -> Add row in Viewings
  - WhatsApp confirmation to lead

### Module 8C: FAQ/General Path
- Use System Knowledge + AI response
- Keep under 120 words
- Include disclaimer line

### Module 8D: Human Handoff Path
- Send WhatsApp alert to agent with summary:
  - lead name
  - number
  - message
  - budget/location
  - urgency
- Update lead status: `ESCALATED`

### Module 9: Log Conversation
- Google Sheets -> Add row in Conversations
- Fields:
  - timestamp
  - phone
  - incoming message
  - AI response
  - intent
  - context summary

### Module 10: Error Handler
- On failure, send agent alert with module + error details
- Log error in Conversations outcome

## 5) Build Scenario 2 (Follow-up & Pipeline Maintenance)
Scenario name: `[Client] - Follow-up & Pipeline Maintenance`

### Module 1: Scheduler
- Run daily at 08:00 (or every 3 days for lower cost)
- Timezone: Africa/Johannesburg

### Module 2: Pull Stalled Leads
- Google Sheets -> Search Rows (Leads)
- Filter:
  - Status not in WON/LOST
  - Last contact older than target days

### Module 3: Follow-up Stage Router
- Day 2 follow-up
- Day 7 follow-up
- Day 14 follow-up

### Module 4: AI Personalization (light)
- OpenAI short follow-up generator
- Limit reply <120 words

### Module 5: Send WhatsApp
- Use regular message if in 24-hour window
- Use approved template outside 24-hour window

### Module 6: Pipeline Updates
- Update:
  - follow-up count
  - last contacted
  - next follow-up date
  - lead status

### Module 7: Daily BI Snapshot
- Optional summary message to agent:
  - new leads
  - matched leads
  - viewings booked
  - escalations

## 6) Copy/Paste Prompt + Message Files
Use directly:
- `templates/system-prompt.md`
- `templates/whatsapp-message-pack.md`

## 7) POPIA & SA Compliance Setup
- Add consent line for data handling.
- Add opt-out line: “Reply STOP to opt out.”
- Store only required lead details.
- Use approved Meta templates for outside 24h session.

## 8) UAT Testing (Must Pass)
Test these messages:
1. “I need a 2-bedroom in Randburg under R1.5m.”
2. “Can I book a viewing this week?”
3. “Do you help with rentals?”
4. “I want to sell my house.”
5. “Please call me, this is urgent.”

Expected:
- Correct route selected
- Listing suggestions sent when relevant
- Calendar slots offered/booking created
- Escalations sent to agent
- Conversations logged

## 9) Go Live
1. Turn Scenario 1 ON.
2. Turn Scenario 2 ON.
3. Monitor first 7 days daily.
4. Adjust filters and message tone.

## 10) Operations Control (Free Tier)
- Keep 2 scenarios only.
- Use keyword pre-routing before AI where possible.
- Reduce follow-up frequency if operation usage is high.
- Skip second OpenAI call unless necessary.
