# Google Antigravity Prompt Pack for Building the Automation Suite

## How to Use This Prompt Pack
Copy one prompt at a time into Google Antigravity. Do not ask Antigravity to build the whole suite in one run. Use the prompts in sequence:

1. Repository understanding
2. Runtime implementation
3. Product workflow implementation
4. Tests
5. Deployment docs
6. Safety/cost review
7. Client demo assets

Always instruct Antigravity to:
- Keep Make.com docs as legacy/no-code options.
- Build production code in `modal-automation-runtime/`.
- Use Google Sheets/Drive/Gmail as the default free layer.
- Keep WhatsApp and AI behind explicit feature flags.
- Add or update tests with every code change.
- Never commit secrets.

---

## 1) Repository Understanding Prompt
```text
You are working in the Speed-to-Lead automation repository.

First, read these files:
- complete-automation-suite-modal-plan.md
- modal-automation-runtime/README.md
- shared-docs/free-tier-cloud-strategy.md
- shared-docs/popia-and-ai-safety-checklist.md
- shared-docs/antigravity-step-by-step-implementation-guide.md
- invoiceflow-email-invoice-processing-blueprint/README.md
- speed-to-lead-automation/README.md
- follow-up-nurture-sequences/README.md
- document-processing-automation/README.md
- propguard-ai-system/README.md
- clinicflow-appointment-guardian-blueprint/README.md
- gym-fitness-member-retention-blueprint/README.md
- real-estate-agent-whatsapp-ai-blueprint/README.md
- whatsapp-ai-tenant-agent-blueprint/README.md

Return a concise architecture recap with:
1. The purpose of each blueprint.
2. Which workflows should be built first.
3. Which shared runtime modules are needed.
4. Which integrations must be feature-flagged to preserve free-tier safety.
5. The exact files you recommend editing next.

Do not change files yet.
```

---

## 2) Shared Runtime Adapter Prompt
```text
Implement the next shared runtime adapter in modal-automation-runtime.

Target adapter: [GoogleSheetsAdapter | GmailAdapter | GoogleDriveAdapter | EmailAdapter | PlainTextPdfExtractor]

Requirements:
1. Keep the adapter behind the existing Protocol interfaces in automation_platform/adapters/interfaces.py.
2. Do not hard-code credentials.
3. Read credentials from environment variables or Modal Secrets only.
4. Add a fake/in-memory adapter for tests if needed.
5. Add unit tests that do not require live Google credentials.
6. Update README or deployment docs with required environment variables/secrets.
7. Preserve dry-run behavior.
8. Do not add WhatsApp or AI dependencies in this step.

After implementing, run:
- python3 -m compileall modal-automation-runtime/automation_platform modal-automation-runtime/modal_app.py
- cd modal-automation-runtime && python3 -m pytest -q

Return changed files and test results.
```

---

## 3) InvoiceFlow Lite Build Prompt
```text
Build InvoiceFlow Lite on top of the Modal runtime.

Read:
- invoiceflow-email-invoice-processing-blueprint/docs/modal-deployment-guide.md
- invoiceflow-email-invoice-processing-blueprint/docs/make-scenarios.md
- modal-automation-runtime/automation_platform/workflows/invoiceflow.py
- modal-automation-runtime/tests/test_invoiceflow.py

Implement the next production-ready slice:
[choose one]
A. Dry-run fixture runner for sample invoice attachments.
B. Plain text PDF extraction for text-based PDFs.
C. Google Sheets adapter wiring for Incoming, Processed, Exceptions, and Chart of Accounts.
D. Gmail label intake adapter.
E. Google Drive archive adapter.
F. Daily summary workflow.

Rules:
- No AI by default.
- No WhatsApp by default.
- Enforce max_documents_per_batch, max_ai_calls_per_day, max_messages_per_day, and max_ocr_pages_per_batch.
- Route unclear documents to Exceptions instead of forcing paid OCR/AI.
- Add tests for clean, duplicate, missing-field, VAT mismatch, and category cases.
- Update InvoiceFlow docs with exact setup steps.

Return a PR-style summary and test results.
```

---

## 4) Speed-to-Lead Lite Build Prompt
```text
Build the Speed-to-Lead Lite Modal workflow.

Read:
- speed-to-lead-automation/docs/modal-conversion-plan.md
- speed-to-lead-automation/docs/make-scenarios.md
- speed-to-lead-automation/templates/leads-sheet-template.csv
- modal-automation-runtime/README.md

Implement:
1. Lead intake data model.
2. SA phone normalization.
3. Lead scoring using rule-based hot keywords.
4. Google Sheets row builder.
5. Owner email alert builder.
6. Manual WhatsApp click-to-chat link generator.
7. Optional WhatsApp send feature flag, but do not implement proactive sending unless asked.
8. Unit tests for phone normalization, hot keyword detection, row building, and click-to-chat links.

Free V1 must work without WhatsApp API.
```

---

## 5) Follow-up & Nurture Build Prompt
```text
Build the Follow-up & Nurture Lite Modal workflow.

Read:
- follow-up-nurture-sequences/docs/modal-conversion-plan.md
- follow-up-nurture-sequences/docs/make-scenarios.md
- follow-up-nurture-sequences/templates/follow-up-message-pack.md

Implement:
1. Rule-based sequence stage selection.
2. Due lead search abstraction.
3. Next follow-up date calculation.
4. Free-mode owner email/task queue output.
5. Reply-state stopper logic.
6. Tests for Day1, Day3, Day7, Final, replied leads, and overdue leads.

Do not send proactive WhatsApp messages unless whatsapp_enabled is explicitly true.
```

---

## 6) Document Processing Worker Prompt
```text
Build shared document-processing workers for InvoiceFlow and document-processing-automation.

Read:
- document-processing-automation/docs/modal-conversion-plan.md
- document-processing-automation/docs/make-scenarios.md
- invoiceflow-email-invoice-processing-blueprint/docs/modal-deployment-guide.md

Implement one slice at a time:
A. Text extraction interface.
B. Local text-PDF extractor.
C. Exception classifier.
D. Archive path builder.
E. Duplicate detection helper.
F. High-value approval router.

Rules:
- Text PDFs first.
- OCR optional and capped.
- AI optional and capped.
- Messy scans route to Exceptions when OCR is disabled.
- Add unit tests for each slice.
```

---

## 7) TenantDesk / Property Prompt
```text
Build TenantDesk Lite as the first property-management workflow.

Read:
- whatsapp-ai-tenant-agent-blueprint/docs/modal-conversion-plan.md
- propguard-ai-system/docs/modal-conversion-plan.md
- whatsapp-ai-tenant-agent-blueprint/templates/system-prompt.md
- propguard-ai-system/templates/propguard-master-hub-template.csv

Implement:
1. Tenant/prospect/owner role lookup abstraction.
2. Intent router for maintenance, rent/payment, lease/general, viewing/prospect, complaint/handoff.
3. Maintenance ticket row builder.
4. Manager email alert builder.
5. Human handoff rules.
6. Tests for each intent route.

Guardrails:
- No legal advice.
- No debt-collection threats.
- No proactive WhatsApp unless client-paid mode is enabled.
```

---

## 8) Real Estate Agent Prompt
```text
Build Real Estate Agent Lite.

Read:
- real-estate-agent-whatsapp-ai-blueprint/docs/modal-conversion-plan.md
- real-estate-agent-whatsapp-ai-blueprint/docs/make-scenarios.md
- real-estate-agent-whatsapp-ai-blueprint/templates/system-prompt.md

Implement:
1. Lead inquiry model.
2. Deterministic listing matcher by suburb, budget, bedrooms, and sale/rental intent.
3. Viewing request row builder.
4. Google Calendar booking abstraction.
5. Agent email alert builder.
6. Tests for listing matching and handoff cases.

Free V1 must work with email alerts and Sheets even if WhatsApp is disabled.
```

---

## 9) ClinicFlow Prompt
```text
Build ClinicFlow Reminder Lite.

Read:
- clinicflow-appointment-guardian-blueprint/docs/modal-conversion-plan.md
- clinicflow-appointment-guardian-blueprint/docs/make-scenarios.md
- clinicflow-appointment-guardian-blueprint/templates/openai-prompts.md

Implement:
1. Appointment reminder selector.
2. Reschedule/cancel intent queue.
3. Receptionist email alert builder.
4. Daily clinic summary builder.
5. Emergency/medical-query handoff rule.
6. Tests for reminders, cancellations, billing questions, and emergency handoff.

Guardrails:
- No medical advice.
- Store minimum patient data.
- AI must be disabled by default.
- WhatsApp reminders require client-paid mode and approved templates.
```

---

## 10) FitGuard Gym Retention Prompt
```text
Build FitGuard Gym Retention Lite.

Read:
- gym-fitness-member-retention-blueprint/docs/modal-conversion-plan.md
- gym-fitness-member-retention-blueprint/docs/make-scenarios.md
- gym-fitness-member-retention-blueprint/templates/openai-prompts.md

Implement:
1. Member status model.
2. Rule-based churn risk scoring.
3. Failed-payment recovery task builder.
4. No-show follow-up task builder.
5. Weekly owner report builder.
6. Tests for churn risk, overdue payment, missed class, and report totals.

Free V1 should queue tasks and email owner reports. WhatsApp campaigns are client-paid mode only.
```

---

## 11) PropGuard Modular Suite Prompt
```text
Build the next PropGuard module only after TenantDesk Lite passes tests.

Read:
- propguard-ai-system/docs/modal-conversion-plan.md
- propguard-ai-system/docs/make-scenarios.md
- propguard-ai-system/templates/propguard-master-hub-template.csv

Choose one module:
A. Maintenance status updates.
B. Owner daily report.
C. Rent reminder task queue.
D. Prospect follow-up task queue.
E. Document processing integration using InvoiceFlow workers.

Rules:
- Do not build all PropGuard modules at once.
- Keep one or two active modules for free V1.
- Email-first alerts and summaries.
- WhatsApp and AI behind feature flags.
- Add tests and docs for the selected module.
```

---

## 12) Modal Deployment Prompt
```text
Prepare the Modal deployment instructions for [workflow name].

Read:
- modal-automation-runtime/README.md
- modal-automation-runtime/modal_app.py
- modal-automation-runtime/configs/client.example.json
- shared-docs/free-tier-cloud-strategy.md

Create or update the workflow deployment guide with:
1. Required Google assets.
2. Required Modal Secrets.
3. Client config JSON example.
4. Dry-run command.
5. Deploy command.
6. Go-live checklist.
7. Rollback procedure.
8. Free-tier limits.
9. Paid upgrade switches.
10. Troubleshooting section.

Do not include real secrets.
```

---

## 13) Test Expansion Prompt
```text
Expand tests for [workflow/module].

Requirements:
1. Use fake adapters only.
2. Do not require network access.
3. Cover clean path, exception path, duplicate/stop behavior, usage limit behavior, and dry-run behavior.
4. Include South African edge cases where relevant: E.164 phone format, 15% VAT, SAST schedule assumptions, POPIA-sensitive handoff.
5. Run pytest and compileall.

Return:
- tests added
- tests changed
- command output summary
- uncovered risks
```

---

## 14) Safety and Cost Review Prompt
```text
Review the current implementation for free-tier, POPIA, AI, and WhatsApp risk.

Read:
- shared-docs/free-tier-cloud-strategy.md
- shared-docs/popia-and-ai-safety-checklist.md
- the workflow code and docs you changed

Return a table with:
1. Risk
2. Severity
3. File/line or workflow area
4. Recommended fix
5. Whether the fix is required before go-live

Pay special attention to:
- hidden WhatsApp sends
- hidden AI calls
- missing usage caps
- secrets in code
- medical/legal/accounting advice risk
- missing human handoff
- unbounded batch sizes
```

---

## 15) Client Demo Script Prompt
```text
Create a client demo script for [workflow name].

The script must include:
1. One-minute value proposition.
2. Demo prerequisites.
3. Step-by-step live demo.
4. What the client should see in Google Sheets/Drive/Gmail.
5. ROI calculation.
6. Common objections and answers.
7. Free-tier limitations explained honestly.
8. Paid upgrade options.
9. Close/next-step script.

Keep the demo focused on business value, not technical architecture.
```
