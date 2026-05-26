# Generated Artifacts

Run the bootstrap script to create client-specific install files:

```bash
python3 tools/bootstrap_speed_to_lead.py \
  --business-name "Acme Plumbing" \
  --owner-email "owner@acme.co.za" \
  --admin-email "ops@acme.co.za"
```

Outputs:
- `generated/<client>-lead-log-template.csv`
- `generated/<client>-google-apps-script.js`
- `generated/<client>-deployment-manifest.json`
