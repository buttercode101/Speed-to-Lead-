# Modal Conversion Plan - FitGuard Member Retention Engine

## Goal
Convert gym retention, payment reminder, no-show follow-up, and reporting workflows into Modal scheduled jobs.

## Modal Jobs
1. `retention_daily_cron` - checks due payments, no-shows, and upcoming renewals.
2. `reactivation_weekly_cron` - queues a small churned-member campaign.
3. `owner_report_cron` - sends weekly performance summary.

## Free V1 Mode
- Import member/payment/attendance data by CSV or Google Sheets.
- Send owner reports by email.
- Queue member follow-up tasks in Sheets rather than sending WhatsApp automatically.
- Use rule-based churn scoring first.

## Client-Paid Mode
- Enable WhatsApp payment reminders and reactivation campaigns.
- Add AI copy generation for reactivation messages.
- Add attendance integrations if the gym software supports exports or API access.

## Sellable Focus
Lead with failed-payment recovery and churn reactivation, not generic chat automation.
