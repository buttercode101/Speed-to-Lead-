# Go-Live Checklist

## Data Layer
- [ ] `Leads` sheet created and columns match template exactly
- [ ] Test row writes successfully from Make
- [ ] Timestamp/timezone consistency verified

## Messaging Layer
- [ ] WhatsApp Business Cloud token valid
- [ ] Recipient test to SA mobile passed
- [ ] Owner alert number configured and tested

## Scenario 1 Controls
- [ ] Lead ID generated for every record
- [ ] Phone normalization produces `27XXXXXXXXX`
- [ ] Hot lead keyword filter working
- [ ] Status updates to `CONTACTED`

## Scenario 2 Controls
- [ ] Weekday scheduler set to 09:00
- [ ] Search filter excludes `WON`
- [ ] Next follow-up logic updates correctly

## Operations
- [ ] Owner knows how to update `Status`
- [ ] Failure notification path configured
- [ ] Duplicate testing completed
- [ ] 5 real-device end-to-end tests completed
