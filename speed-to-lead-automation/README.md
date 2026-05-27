# Speed-to-Lead Automation (SA SME MVP)

This project implements a **production-ready V1** for South African SMEs:

`Google Form -> Make Trigger -> Google Sheets -> WhatsApp Reply -> Owner Notification -> Sheet Update`

## Folder Structure

- `docs/`
  - `build-plan.md` – phased implementation plan.
  - `make-scenarios.md` – exact module-by-module Make setup.
  - `go-live-checklist.md` – launch checks.
- `templates/`
  - `leads-sheet-template.csv` – exact column schema for the Leads sheet.
  - `whatsapp-message-pack.md` – copy/paste messages for instant reply + follow-ups.
- `make/`
  - `scenario-1-incoming-leads.json` – import-oriented scenario blueprint.
  - `scenario-2-follow-up-engine.json` – import-oriented follow-up blueprint.

## Scope (Phase 1 MVP)

Includes only:
1. Capture lead
2. Save to Sheets
3. Send instant WhatsApp reply
4. Notify owner
5. Update status

No AI logic in MVP routing/scoring.

## V1 Stack

- Google Sheets (master CRM)
- Make.com (orchestration)
- WhatsApp Business Cloud API (messaging)
- Google Calendar (booking link destination)
- Google Forms (lead intake)

## Build Order

1. Create Google Sheet and import `templates/leads-sheet-template.csv`.
2. Build Scenario 1 from `docs/make-scenarios.md`.
3. Test with 5 sample leads (cold + hot keywords).
4. Build Scenario 2 follow-up engine.
5. Run go-live checklist.

## Notes

- Use E.164 phone format for South Africa (`27XXXXXXXXX`) to avoid WhatsApp delivery failures.
- Keep automation under 3 scenarios initially.
- Add AI only after baseline conversion and response-time SLAs are stable.
