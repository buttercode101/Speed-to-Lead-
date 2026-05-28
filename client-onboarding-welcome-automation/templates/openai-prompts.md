# OpenAI Prompts - Client Onboarding & Welcome Automation

## Personalized Welcome Email Prompt
```text
Write a warm, professional welcome email for a new client.

Client Name: {{client_name}}
Company Name: {{company_name}}
Service Package: {{service_package}}
Next Steps: Kickoff call + access to shared folder
Shared Folder Link: {{folder_link}}
Payment Link: {{payment_link}}
Preferred Language: {{preferred_language}}

Tone: Friendly, confident, and helpful.
Highlight that they made a great decision choosing us.
Include a short POPIA-aware note that their information will be handled securely and only used for service delivery.
If Preferred Language is Afrikaans, write the email in Afrikaans.
Keep under 180 words.
```

## Day 3 Follow-Up Prompt
```text
Write a Day 3 onboarding check-in email.

Client Name: {{client_name}}
Service Package: {{service_package}}
Kickoff Call Details: {{kickoff_details}}
Outstanding Items: {{outstanding_items}}
Preferred Language: {{preferred_language}}

Ask if they have any questions and remind them of the kickoff call.
Use a helpful, supportive tone.
Include one clear call to action.
Keep under 140 words.
```

## Day 7 Reminder Prompt
```text
Write a polite Day 7 onboarding reminder.

Client Name: {{client_name}}
Outstanding Items: {{outstanding_items}}
Folder Link: {{folder_link}}
Preferred Language: {{preferred_language}}

The email should be friendly but clear that these items are needed to continue smoothly.
Keep under 140 words.
```

## Weekly Owner Report Prompt
```text
Create a short weekly onboarding status report for the business owner.

Active Clients: {{active_clients}}
Overdue Tasks: {{overdue_tasks}}
Clients Waiting for Contract: {{waiting_contract}}
Clients Waiting for Payment: {{waiting_payment}}
Completed This Week: {{completed_clients}}

Output:
- 3-bullet executive summary
- Client-by-client blockers
- Recommended next actions

Use a professional, concise tone.
Keep under 220 words.
```
