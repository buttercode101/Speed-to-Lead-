# Exception & Approval Message Pack

## High Value Approval
⚠️ Invoice Approval Needed

Vendor: {{vendor}}
Amount: R{{amount}}

Reason:
Invoice exceeds approval threshold.

Reply:
APPROVE or REJECT

## Duplicate Alert
🚨 Possible Duplicate Invoice Detected

Vendor: {{vendor}}
Invoice #: {{invoice}}

Please review before payment processing.

## OCR Failure Alert
❌ Document Processing Failed

The uploaded document could not be read properly.

Manual review required.

## Daily Summary
📄 Daily Document Processing Summary

Processed Today: {{processed_count}} documents
Exceptions: {{exception_count}}
Duplicate Warnings: {{duplicate_count}}

Top Categories:
{{top_categories}}

Total Processed Value:
R{{total_value}}
