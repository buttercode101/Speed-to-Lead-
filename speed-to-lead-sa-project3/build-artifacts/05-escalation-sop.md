# Escalation SOP (Missed-Lead Recovery)

## Trigger
Escalation starts when a lead remains **New** past the agreed SLA threshold.

## Escalation levels
1. **Level 1 (SLA breach warning)**
   - Notify primary owner
   - Mark escalation flag = L1
2. **Level 2 (Persistent non-response)**
   - Notify backup owner/manager
   - Mark escalation flag = L2
3. **Level 3 (Critical delay)**
   - Notify owner + manager + fallback responder
   - Mark escalation flag = L3

## Required log fields
- Escalation level
- Escalation time
- Notified users
- Resolution time
- Root cause

## Resolution rules
- Escalation closes only when status moves from New to Contacted or higher.
- Resolver must document root cause and prevention action.

## Weekly review
- Count escalations by level
- Top root causes
- Process changes for next week
