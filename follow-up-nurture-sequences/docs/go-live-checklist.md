# Go-Live Checklist - Follow-up & Nurture Sequences

## Data & CRM
- [ ] Leads sheet contains all new follow-up columns
- [ ] Existing rows initialized with defaults
- [ ] Phone normalization consistent with Speed-to-Lead

## Scenario 2
- [ ] Weekday 09:00 schedule configured
- [ ] Weekday 14:00 schedule configured
- [ ] Due-date filter validated (`Next Follow-up Date <= NOW`)
- [ ] Sequence stage routing validated for Day1/3/7/Final

## Scenario 3
- [ ] Inbound WhatsApp trigger connected
- [ ] Lead lookup by phone works reliably
- [ ] Sequence Active set to NO on reply
- [ ] Owner receives reply-alert in <60 seconds

## QA
- [ ] Test 1: no-reply lead receives Day1 then Day3
- [ ] Test 2: replied lead stops future follow-ups
- [ ] Test 3: final attempt message sends only once
