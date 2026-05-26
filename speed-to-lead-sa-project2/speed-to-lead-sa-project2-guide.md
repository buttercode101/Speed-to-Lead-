# Speed-to-Lead SA — Project 2 Revenue Capture System (V2)

**Project Name:** Speed-to-Lead SA - Project 2 (Real Estate Acceleration)  
**Version:** V2.0 (Productized Offer)  
**Creator:** Solo Builder  
**Primary Market:** South Africa (Cape Town first, national next)  
**Date:** May 24, 2026  
**Mission:** Help local businesses respond to every serious lead fast enough to increase booked jobs and reduce lost revenue.

---

## 1) Executive Summary (Brutally Honest)

Most small businesses do **not** lose leads because they are bad at their trade. They lose leads because they respond late, forget follow-ups, or never track outcomes.

A simple automation alone is not defensible. A competitor can copy “form → sheet → email.”

So this business must sell a **Revenue Capture System**, not “automation setup.”

### Core Promise
- Every new lead is captured and visible.
- Owner/team gets alerted immediately.
- Lead receives a rapid acknowledgement.
- Missed responses are escalated.
- Weekly reporting proves business impact.

### Positioning Statement
> “We help service businesses stop leaking revenue from slow lead response by installing a done-for-you response system with tracking, escalation, and weekly performance reporting.”

---

## 2) Ideal Customer Profile (ICP)

### Best-fit sectors
- Real estate agencies
- Independent property practitioners
- Property management teams
- Bond originator partners
- New development sales teams

### Best-fit business profile
- 20–300 inbound leads/month
- Owner complains about “bad quality leads” (often actually delayed response)
- Uses WhatsApp heavily
- No structured lead pipeline
- No reliable response-time KPI

### Red flags (qualify out)
- Under 10 leads/month
- No one available to respond to leads
- Unwilling to track outcomes
- Wants “set and forget” without operational ownership

---

## 3) Offer Stack (What You Sell)

## Tier 1: Foundation (Setup)
**Goal:** Lead never gets lost.
- Capture source connected (Form and/or WhatsApp intake)
- Central lead log
- Instant owner notification
- Basic status tracking

## Tier 2: Conversion (Standard)
**Goal:** Lead gets contacted faster and followed up.
- Everything in Foundation
- Auto-acknowledgement message templates
- Response-time tracking
- Missed-lead escalation rule
- Weekly KPI scorecard

## Tier 3: Revenue (Premium)
**Goal:** Improve close rate and prove ROI.
- Everything in Conversion
- Multi-step follow-up workflows
- Quote/booking outcome tracking
- Monthly optimization review
- Performance insights + scripts

## Suggested commercial model
- Setup fee (once-off)
- Monthly service fee (monitoring/reporting/optimization)
- Optional performance bonus tied to agreed KPI outcome

---

## 4) Operating KPIs (Non-Negotiable)

Track these from Day 1:
1. **Time-to-first-response** (median + 90th percentile)
2. **Contact rate** (% leads reached)
3. **Qualified rate** (% leads qualified)
4. **Quote rate** (% leads quoted)
5. **Close rate** (% leads closed)
6. **Revenue per lead**
7. **Missed lead count**
8. **Lead aging buckets** (0–5 min, 5–30 min, 30+ min, 24h+)

If a client won’t track KPIs, don’t promise ROI claims.

---

## 5) Technology Stack (Low Cost, Realistic)

| Tool | Use | Notes |
|---|---|---|
| Google Forms | Web lead intake | Fastest zero-cost input |
| Google Sheets | Lead log + pipeline | Quick to deploy and audit |
| Make.com | Workflow orchestration | Watch operations/credits closely |
| Gmail | Owner alerts + summaries | Universal and simple |
| ManyChat / WhatsApp channel | Customer acknowledgement | Must obey template/policy constraints |
| Loom | Sales/demo/training video | Speeds trust and onboarding |

> Important: Treat third-party pricing/limits as variable. Recheck before each new proposal.

---

## 6) Data Model (Lead Log Schema)

Use this exact schema in Google Sheets:
- Lead ID (unique)
- Created At (UTC)
- Local Time (SAST)
- Source (Form / WhatsApp / Referral / Call)
- Lead Name
- Phone (raw)
- Phone (normalized)
- Email (optional)
- Service Needed
- Area/Suburb
- Message
- Budget (optional)
- Consent Captured (Y/N)
- Consent Timestamp
- Status (New / Contacted / Qualified / Quoted / Closed / Lost)
- Owner Assigned
- First Response At
- Minutes to First Response
- Follow-up Due At
- Last Follow-up At
- Lead Score (optional)
- Loss Reason
- Job Value (ZAR)
- Notes
- Automation Health (OK / Error)

### Validation rules
- Status dropdown only
- Minutes to First Response = formula-derived
- Mandatory fields: Lead Name, Phone, Service Needed, Source

---

## 7) Automation Architecture (Make.com Blueprint)

## Scenario A: Intake + Log + Alert (Core)
1. Trigger: New lead captured
2. Normalize/clean fields
3. De-duplication check (phone + short time window)
4. Write to lead log
5. Send owner alert (email/WhatsApp)
6. Set status = New
7. Schedule follow-up due time

## Scenario B: Instant Customer Acknowledgement
1. Trigger: New valid lead
2. Select template by service + area
3. Send acknowledgement via approved channel
4. Log send status + timestamp

## Scenario C: Missed-Lead Escalation
1. Trigger: Lead still New past SLA threshold
2. Notify backup contact
3. Mark escalation flag
4. Continue periodic reminders until status changed

## Scenario D: Weekly KPI Summary
1. Trigger: Weekly schedule
2. Aggregate KPI metrics
3. Send owner report
4. Highlight bottlenecks and top opportunities

### Reliability requirements
- Error route on every scenario
- Admin alert on failure
- Retry policy for transient failures
- Daily heartbeat check (“system alive” message)

---

## 8) SLA & Response Rules

Recommended starting SLA:
- Owner alert: under 60 seconds from lead capture
- First human response: under 5 minutes in business hours
- Escalation: if not contacted within SLA threshold

Business-hours rule:
- In-hours: urgent routing
- After-hours: auto-acknowledge + next-opening callback promise

---

## 9) Message Templates (Starter)

## Owner Alert (Email)
Subject: 🚨 New Lead: {{Lead Name}} — {{Service Needed}} in {{Area}}

Body:
- Name: {{Lead Name}}
- Phone: {{Phone}}
- Service: {{Service Needed}}
- Area: {{Area}}
- Message: {{Message}}
- Logged at: {{Created At}}
- Open lead sheet: {{Link}}

## Customer Instant Acknowledgement
“Hi {{FirstName}}, thanks for contacting {{BusinessName}}. We’ve received your request for {{ServiceNeeded}} in {{Area}}. A team member will contact you shortly. If urgent, reply with ‘URGENT’.”

## After-hours Acknowledgement
“Hi {{FirstName}}, thanks for your message. We’ve logged your request and will contact you at {{NextBusinessHour}}. If this is urgent, reply with ‘URGENT’ and we’ll prioritize.”

---

## 10) Compliance-by-Design (South Africa)

Operational safeguards:
- Capture consent at source where required
- Track consent timestamp and source
- Maintain opt-out handling process
- Keep minimum necessary personal data
- Restrict data access to authorized users
- Document data retention and deletion cadence

Do not market compliance as “legal advice.” It is operational best practice.

---

## 11) Sales System (How You Close Clients)

## Sales narrative
1. Problem: “Leads are expensive and response is slow.”
2. Cost of delay: “Late response = lost jobs.”
3. System: “We install tracking + alerts + follow-up accountability.”
4. Proof: “You see response-time and close-rate metrics weekly.”
5. Offer: “Done-for-you install + monthly optimization.”

## Discovery questions
- How many leads/month?
- How fast are leads contacted now?
- Who owns first response?
- What % are never contacted?
- Average job value?
- What happens after hours?

## Objection handling
- “We already use WhatsApp.” → “Great; we make it measurable and impossible to forget.”
- “It’s too expensive.” → “One recovered job often pays for setup.”
- “My staff will handle it.” → “This gives staff a system and accountability.”

---

## 12) Onboarding Checklist (Per Client)

1. Confirm service scope + SLA
2. Gather brand/business details
3. Create/copy lead log template
4. Build intake form and fields
5. Connect Make scenario(s)
6. Configure alerts and escalation contacts
7. Load message templates
8. Run end-to-end tests (normal + edge cases)
9. Team training (15–30 min Loom/live)
10. Go-live + 7-day monitoring window

---

## 13) QA & Testing Protocol

Run these tests before go-live:
1. Valid lead test (all modules succeed)
2. Missing field test (validation catch)
3. Duplicate lead test
4. After-hours flow test
5. Escalation trigger test
6. Error route simulation
7. Weekly report generation test

Pass criteria:
- Data consistency between source and sheet
- Alert arrives within SLA
- Status updates function correctly
- No silent failures

---

## 14) Weekly Reporting Template (Client-Facing)

Include:
- Total new leads
- Median time-to-first-response
- Leads contacted within SLA
- Qualified / quoted / closed counts
- Estimated revenue won
- Lost leads and primary reasons
- Top 3 improvement actions for next week

Use a “traffic light” style:
- Green: On target
- Amber: At risk
- Red: Immediate action needed

---

## 15) 30-Day Launch Plan

## Week 1
- Finalize positioning + assets
- Build master template system
- Internal dry run

## Week 2
- Pilot with first client (discounted proof project)
- Collect baseline metrics

## Week 3
- Tune workflows and scripts
- Produce first weekly KPI report

## Week 4
- Capture testimonial/case study
- Start outbound prospecting with proof

---

## 16) Real Estate Specialization Layer

- Track enquiry type: Buy / Rent / Sell / Valuation
- Track property type and budget range
- Route hot buyer/renter leads to available agent
- Measure viewing-booking rate and offer rate

---

## 17) What Makes This Hard to Refuse

A business can refuse “automation setup.”
It is much harder to refuse:
- Faster response to hot leads
- Fewer missed inquiries
- Clear weekly performance visibility
- Better close consistency

So always sell outcome + accountability, not tools.

---

## 18) Next Build Artifacts to Create

1. Client proposal template
2. ROI calculator sheet
3. Niche-specific message packs (plumber, real estate, dental)
4. Lead status playbook for staff
5. Escalation SOP
6. 1-page dashboard layout
7. Case study template

