# Step-by-Step Setup - Client Onboarding & Welcome Automation

## 1. Prepare the Google Sheet
1. Create a Google Sheet named `[Client Business] - Onboarding Hub`.
2. Add the tabs and columns from `templates/onboarding-hub-template.csv`.
3. Freeze the header row on each tab.
4. Add dropdowns for common statuses:
   - `Contract Signed`: Yes, No, Pending
   - `Onboarding Status`: New, In Progress, Waiting for Contract, Waiting for Payment, Waiting for Client, Complete, Setup Error
   - `Welcome Sent`: Yes, No
   - `Payment Status`: Unpaid, Paid, Not Required
   - `Task Status`: Not Started, In Progress, Waiting, Complete

## 2. Build the Client Onboarding Form
Recommended Google Form fields:
- Client name
- Primary contact name
- Phone
- Email
- Company name
- Service package
- Preferred language
- Contract signed confirmation
- VAT/BEE details if relevant
- Required access/documents
- Kickoff call preference

Connect responses to the `New Clients` tab or map responses into that tab via Make.com.

## 3. Prepare Google Drive Templates
Create a folder named `Onboarding Template Assets` with:
- Welcome pack PDF or Google Doc
- Contract/agreement copy template
- Access request checklist
- Project kickoff agenda
- Any service-specific documents

Keep these files generic so Make.com can copy them into each client folder.

## 4. Configure Payment Links
Choose the client's payment method:
- Yoco payment link
- PayFast payment request
- Ozow link
- Xero/QuickBooks invoice URL
- Manual EFT instructions

Store the default payment link or invoice instructions in Make.com variables or a settings row in Google Sheets.

## 5. Build Scenario 1 in Make.com
1. Add Google Forms `Watch New Responses` trigger.
2. Add Google Sheets `Add a Row` for `New Clients`.
3. Add Google Drive `Create a Folder`.
4. Add Google Drive `Copy a File` modules for each welcome asset.
5. Add Google Sheets `Update a Row` to save the folder link.
6. Add OpenAI email personalization.
7. Add Gmail send module for the Day 0 welcome email.
8. Add Google Sheets modules to create checklist rows.
9. Add routers for contract, payment, kickoff call, and language logic.
10. Add Day 3 and Day 7 delay/follow-up modules.
11. Add an error handler route that emails the owner.

## 6. Build Scenario 2 in Make.com
1. Add a weekly scheduler.
2. Search incomplete clients in `New Clients`.
3. Search overdue checklist tasks.
4. Summarize with OpenAI.
5. Email the owner.
6. Log the weekly report in `Reports`.

## 7. Test Before Go-Live
Run three test submissions:
- Standard new client with contract signed and payment required
- Client without signed contract
- Afrikaans-language client

Confirm that each test creates the correct folder, checklist rows, email content, owner notification, and report entries.
