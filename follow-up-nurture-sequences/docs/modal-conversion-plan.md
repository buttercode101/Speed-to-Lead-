# Modal Conversion Plan - Follow-up & Nurture Sequences

## Goal
Replace the Make.com follow-up scheduler and reply stopper with Modal cron jobs and optional inbound webhooks.

## Modal Jobs
1. `follow_up_cron_0900` - sends or queues Day1/Day3/Day7/Final actions.
2. `follow_up_cron_1400` - second daily run for due leads.
3. `reply_detection_webhook` - optional WhatsApp inbound endpoint.

## Free V1 Mode
- Do not send proactive WhatsApp automatically.
- Write due follow-up tasks to Google Sheets.
- Send owner email reminders with click-to-chat links.
- Keep routing rule-based; no AI needed.

## Client-Paid Mode
- Enable WhatsApp templates for approved follow-ups.
- Stop sequences automatically on inbound replies.
- Track sent message count per lead and per day.

## Required Code Modules
- `workflows/follow_up.py`
- Shared `SheetsAdapter`
- Shared `EmailAdapter`
- Optional `WhatsAppCloudAdapter`
