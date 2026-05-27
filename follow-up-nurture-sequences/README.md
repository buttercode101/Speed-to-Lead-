# Follow-up & Nurture Sequences (SA SME V1)

This project is the second automation in the stack and is designed to convert more leads without increasing ad spend.

## Goal
Automate follow-ups, stop sequences when leads reply, escalate hot replies to owners, and keep CRM fully updated.

## System Architecture
- Scenario 1: Incoming Leads Processor (from Speed-to-Lead project)
- Scenario 2: Follow-up Engine
- Scenario 3: Reply Detection & Sequence Stopper

## Folder Structure
- `docs/`
  - `build-plan.md`
  - `make-scenarios.md`
  - `go-live-checklist.md`
- `templates/`
  - `leads-sheet-upgrade.csv`
  - `follow-up-message-pack.md`
- `make/`
  - `scenario-2-follow-up-engine.json`
  - `scenario-3-reply-detection-stopper.json`

## Build Order
1. Apply the Leads sheet upgrade columns from `templates/leads-sheet-upgrade.csv`.
2. Build Scenario 2 from `docs/make-scenarios.md`.
3. Build Scenario 3 from `docs/make-scenarios.md`.
4. Test with cold leads and reply-positive leads.
5. Validate sequence stop behavior.

## V1 Constraints
- Keep rule-based sequence routing.
- No AI dependency for scheduling, routing, or state changes.
- Run follow-up scheduler only at 09:00 and 14:00 on weekdays.
