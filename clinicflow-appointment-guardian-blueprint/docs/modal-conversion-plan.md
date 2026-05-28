# Modal Conversion Plan - ClinicFlow Appointment Guardian

## Goal
Convert clinic booking/reminder workflows into Modal jobs while minimizing medical-data risk.

## Modal Endpoints and Jobs
1. `clinic_inbound_webhook` - booking, reschedule, cancellation, billing, and general admin messages.
2. `appointment_reminder_cron` - daily reminder batch for upcoming appointments.
3. `clinic_daily_report_cron` - owner/reception summary.

## Free V1 Mode
- Use Google Calendar and Google Sheets for appointment tracking.
- Send receptionist alerts by email.
- Use manual WhatsApp click-to-chat links if WhatsApp automation is not client-paid.
- Store only appointment/admin data needed for the workflow.

## Client-Paid Mode
- Enable WhatsApp reminders with approved utility templates.
- Add AI-assisted admin replies.
- Add no-show analysis and billing reminder reports.

## Required Guardrails
- No medical advice.
- Emergency messages must instruct the patient to contact emergency services or the clinic directly.
- Sensitive health details should not be sent to AI unless the client has explicitly approved the data flow.
- Run early pilots in receptionist-approval mode.
