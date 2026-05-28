# Modal Conversion Plan - Speed-to-Lead Automation

## Goal
Convert the Make.com MVP into a Python/Modal workflow while keeping Google Sheets as the lead CRM.

## Modal Endpoints and Jobs
1. `lead_intake_endpoint` - accepts Google Form/web form payloads.
2. `follow_up_cron` - runs weekdays at 09:00 and 14:00 SAST.
3. `reply_webhook` - optional WhatsApp inbound webhook when client-paid WhatsApp is enabled.

## Free V1 Mode
- Capture leads through Google Forms or website forms.
- Store leads in Google Sheets.
- Send owner alerts by Gmail.
- Generate manual WhatsApp click-to-chat links instead of automated WhatsApp sends.
- Create follow-up tasks in Sheets.

## Client-Paid Mode
- Enable WhatsApp Business Platform sending.
- Use approved templates for business-initiated messages.
- Track message counts and costs per client.

## Required Code Modules
- `workflows/speed_to_lead.py`
- `adapters/google_sheets.py`
- `adapters/email.py`
- `adapters/whatsapp_cloud.py` behind `whatsapp_enabled`
