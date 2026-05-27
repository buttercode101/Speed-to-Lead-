# Go-Live Checklist - WhatsApp AI Tenant Agent

## Data Hub
- [ ] All required tabs exist (Tenants, Properties, Maintenance, Rent Payments, Conversation Log)
- [ ] Tenant phone numbers are normalized to SA format
- [ ] Payment links loaded for active tenants

## Scenario Health
- [ ] Incoming trigger captures tenant messages
- [ ] Intent routing works for all 6 branches
- [ ] Rent replies include exact balance + payment link
- [ ] Maintenance messages create ticket rows
- [ ] Escalations notify manager
- [ ] Conversation Log updates on every message

## Compliance
- [ ] Opt-out instruction present (STOP)
- [ ] WhatsApp template usage configured for outside 24-hour window
- [ ] POPIA consent wording reviewed

## Reliability
- [ ] Error route tested with forced failure
- [ ] Manager receives full context on failure
- [ ] 10 live-message UAT test completed successfully
