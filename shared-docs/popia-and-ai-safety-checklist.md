# POPIA and AI Safety Checklist

## Scope
Use this checklist for all South African SME workflows that process leads, invoices, tenants, patients, members, or payment records.

## Client-Owned Data
- [ ] Google Sheet is owned by the client or a client-controlled Workspace.
- [ ] Google Drive archive is owned by the client.
- [ ] Modal secrets are separated per client.
- [ ] Access is limited to approved operators.

## Data Minimization
- [ ] Only collect fields needed for the workflow.
- [ ] Do not send unnecessary personal data to AI providers.
- [ ] Avoid storing medical, legal, or sensitive financial notes unless required.
- [ ] Use IDs and links rather than copying full documents into logs.

## AI Guardrails
- [ ] AI does not provide medical, legal, accounting, or debt-collection advice.
- [ ] AI routes uncertainty to a human.
- [ ] Prompts include escalation rules.
- [ ] High-risk messages require human review during pilot.

## Messaging Consent
- [ ] Capture consent or legitimate communication basis where needed.
- [ ] Include opt-out language for marketing or nurture sequences.
- [ ] Avoid proactive WhatsApp messages unless the client accepts platform costs and template rules.

## Retention and Deletion
- [ ] Define how long rows and documents are retained.
- [ ] Define who can request deletion or correction.
- [ ] Keep a simple incident response process.
