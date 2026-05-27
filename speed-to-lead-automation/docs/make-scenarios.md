# Make.com Scenarios - Detailed Configuration

## Scenario Naming
- Scenario 1: `[Client] - Incoming Leads Processor`
- Scenario 2: `[Client] - Follow-up Engine`

---

## Scenario 1 - Incoming Leads Processor

### Module 1: Google Forms -> Watch Responses
- Trigger source: chosen Google Form
- Polling: Immediately as available

### Module 2: Tools -> Set Variable (Lead ID)
Variable name: `lead_id`

Value:
`LD-{{formatDate(now; "YYMMDD")}}-{{random}}`

### Module 3: Tools/Text Functions -> Normalize Phone
Rules:
1. Trim spaces
2. Remove `+`
3. If first char is `0`, replace with `27`

Expected output examples:
- `0821234567` -> `27821234567`
- `+27 82 123 4567` -> `27821234567`

### Module 4: Google Sheets -> Add a Row (`Leads` sheet)
Map all form fields and defaults:
- Status = `NEW`
- Lead Score = `3`
- Hot Lead = `NO`
- Booking Link Sent = `YES`
- Assigned To = owner name

### Module 5: Router (rule-based qualification)
Hot keywords (case-insensitive):
- urgent
- today
- asap
- quote
- pricing
- ready
- install
- book now

If matched:
- Lead Score = `8-10`
- Hot Lead = `YES`

Else:
- Lead Score = `3-5`
- Hot Lead = `NO`

### Module 6: WhatsApp Business Cloud -> Send Message (lead)
Template body:

```
Hi {{firstName}} 👋

Thanks for reaching out to {{businessName}}.

We've received your inquiry about {{service}} and one of our team members will assist shortly.

Quick question:
What timeline are you working with?

You can also book a quick call here:
{{bookingLink}}
```

### Module 7: WhatsApp Business Cloud -> Send Message (owner)
Owner alert body:

```
🔥 NEW HOT LEAD

Name: {{name}}
Phone: {{phone}}
Service: {{service}}
Source: {{source}}

Message:
{{message}}

Lead Score: {{score}}/10
```

### Module 8: Google Sheets -> Update Row
Update fields:
- Lead Score
- Hot Lead
- Status = `CONTACTED`
- Last Contacted = `now()`

---

## Scenario 2 - Follow-up Engine

### Schedule
- Every weekday
- 09:00 local time (South Africa Standard Time)

### Flow
1. Scheduler
2. Google Sheets -> Search Rows
   - `Status != WON`
   - `Next Follow-up <= TODAY`
3. Iterator
4. WhatsApp send follow-up by day-rule
5. Google Sheets update

### Follow-up Copy
- Day 1: "Just checking if you saw our previous message..."
- Day 3: "Would you still like a quote?"
- Day 7: "We're closing your inquiry soon..."

### Update fields each follow-up
- Last Contacted = now
- Next Follow-up = now + offset
- Notes append = message type sent
