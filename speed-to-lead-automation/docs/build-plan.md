# Build Plan - Speed-to-Lead Automation

## Objective
Deploy a reusable, low-complexity automation that reduces response time from minutes/hours to near real-time for South African SMEs.

## Phase 1 (2-3 hours): Working MVP

### Deliverables
- Lead intake via Google Form
- Lead row created in Google Sheets
- Instant WhatsApp acknowledgment to lead
- Owner notification via WhatsApp
- Sheet status update to `CONTACTED`

### Acceptance Criteria
- New form submission appears in `Leads` sheet within 10 seconds.
- Lead receives first WhatsApp in <60 seconds.
- Owner receives alert for every inbound lead.
- Hot lead keyword logic tags `Hot Lead = YES` and score >= 8.

## Phase 2 (1-2 hours): Follow-up Engine
- Daily scheduler at 09:00 (weekdays)
- Pull leads where `Status != WON` and `Next Follow-up <= TODAY`
- Send day-based follow-up
- Update last-contacted and next-follow-up fields

## Phase 3 (Optional after stability)
- Add AI personalization for reply polish only
- Add Facebook Lead Ads trigger path
- Add reporting dashboard and daily digest

## Suggested First Niches
- Solar installers
- Security companies
- Gyms
- Real estate agencies
- Car dealerships
- Coaches/consultants
- Cleaning services
- Marketing agencies
