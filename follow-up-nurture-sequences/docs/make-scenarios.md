# Make.com Scenarios - Follow-up & Nurture Sequences

## Scenario 2 - Follow-up Engine

### Module 1: Scheduler
- Run times: weekdays at 09:00 and 14:00
- Timezone: Africa/Johannesburg

### Module 2: Google Sheets -> Search Rows
Filter:
- Sequence Active = YES
- Replied != YES
- Next Follow-up Date <= NOW

### Module 3: Iterator
- Process each lead row individually.

### Module 4: Router by Sequence Stage
Routes:
- Day1
- Day3
- Day7
- Final

### Module 5: WhatsApp Business Cloud -> Send Message
Message rules:
- Keep under 120 words
- Human and low-pressure tone
- Avoid spammy formatting

### Module 6: Google Sheets -> Update Row
- Follow-up Count = Follow-up Count + 1
- Last Follow-up Sent = now
- Sequence Stage = next stage
- Next Follow-up Date = calculated by stage delay

### Date Logic
- Day1: 24 hours
- Day3: +2 days
- Day7: +4 days
- Final: +7 days

---

## Scenario 3 - Reply Detection & Sequence Stopper

### Module 1: WhatsApp Business Cloud -> Watch Messages
- Trigger on incoming lead replies.

### Module 2: Google Sheets -> Search Rows
- Match by normalized phone number.

### Module 3: Google Sheets -> Update Row
Set:
- Replied = YES
- Sequence Active = NO
- Last Reply Date = now
- Follow-up Outcome = Interested (or custom rule)

### Module 4: WhatsApp Business Cloud -> Send Owner Alert
```
🔥 LEAD REPLIED

Name: {{name}}
Phone: {{phone}}

Reply:
{{message}}

Follow up ASAP.
```
