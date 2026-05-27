# Go-Live Checklist - ClinicFlow Appointment Guardian

## Data Hub
- [ ] All 6 tabs created and headers validated
- [ ] Initial patient and appointment data loaded
- [ ] Billing payment links populated

## Scenario 1 checks
- [ ] Incoming WhatsApp trigger works
- [ ] Router handles all main intents
- [ ] Booking flow creates calendar event + sheet row
- [ ] Emergency keywords escalate immediately
- [ ] Conversation and status updates logged

## Scenario 2 checks
- [ ] Daily 07:00 run firing
- [ ] 3-day / 24-hour / 2-hour reminders sent
- [ ] Overdue bill reminders sent
- [ ] Daily owner report generated and delivered
- [ ] Daily Reports tab updated

## Compliance
- [ ] POPIA consent and opt-out wording included
- [ ] No sensitive diagnosis details logged unnecessarily
- [ ] Templates configured for outside 24-hour WhatsApp window

## Reliability
- [ ] Error handler tested with forced failure
- [ ] 10-message UAT completed successfully
