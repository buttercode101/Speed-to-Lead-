# Modal Conversion Plan - WhatsApp AI Tenant Agent

## Goal
Convert the tenant assistant into a Modal inbound webhook that logs maintenance, rent, viewing, and support requests into Google Sheets.

## Modal Endpoint
`tenant_whatsapp_webhook` handles inbound tenant/landlord/prospect messages and routes them by intent.

## Free V1 Mode
- Focus on inbound support within the WhatsApp service window.
- Log maintenance requests and tenant questions to Sheets.
- Send manager alerts by email.
- Avoid proactive rent reminders unless client-paid WhatsApp is enabled.

## Client-Paid Mode
- Enable rent reminders, maintenance updates, and viewing follow-ups through WhatsApp templates.
- Add AI intent classification and response drafting.
- Add landlord/owner summary reports.

## Required Guardrails
- No legal advice, eviction guidance, or debt-collection threats.
- Escalate disputes, complaints, arrears disputes, and safety issues to a human.
- Keep tenant documents in client-owned Google Drive.
