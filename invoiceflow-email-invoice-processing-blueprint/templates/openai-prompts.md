# OpenAI Prompts - InvoiceFlow Email Invoice Processing

## Main Extraction Prompt
```text
You are a senior South African bookkeeper.

Extract the following from the invoice text and return clean JSON only:

{
  "vendor": "",
  "invoice_number": "",
  "invoice_date": "YYYY-MM-DD",
  "due_date": "YYYY-MM-DD or null",
  "amount_ex_vat": number,
  "vat_amount": number,
  "total_amount": number,
  "description": "brief summary",
  "currency": "ZAR"
}

Use 15% VAT rate. If unclear, mark as null or "unclear".

Text:
{{invoice_text}}
```

## Categorization Prompt
```text
Choose the best category from this list for the invoice:
{{chart_of_accounts_list}}

Vendor: {{vendor}}
Description: {{description}}

Return only the exact category name.
```

## Exception Explanation Prompt
```text
You are helping an accountant review an invoice automation exception.

Given the extracted invoice JSON, validation issue, and file metadata, write a short explanation and suggested fix.

Rules:
- Keep it under 60 words.
- Be specific.
- Do not invent values.
- If a human must inspect the invoice, say exactly what they should check.

Extracted JSON:
{{extracted_json}}

Validation issue:
{{validation_issue}}

File metadata:
{{file_metadata}}
```

## Daily Summary Prompt
```text
Create a concise InvoiceFlow daily summary for a South African business owner/accountant.

Include:
- Processed invoice count
- Total value processed in ZAR
- VAT total in ZAR
- Exception count
- Top vendors or categories if available
- 2-3 actions needed tomorrow

Use a professional, confident tone. Keep it under 160 words.

Summary data:
{{summary_data}}
```
