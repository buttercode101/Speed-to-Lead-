# Make.com Scenario Blueprint (Implementation Ready)

## Scenario A — Intake → Log → Owner Alert

### Modules
1. **Trigger**: Google Forms > Watch Responses
2. **Tools**: Set variables
   - `created_at_utc = now`
   - `source = "Form"`
3. **Tools**: Text parser/replace for phone normalization
4. **Google Sheets**: Search rows (dedupe by normalized phone + past 4h)
5. **Router**:
   - Branch 1: duplicate found → update existing row note + stop
   - Branch 2: no duplicate → add row
6. **Google Sheets**: Add row using full schema
7. **Gmail**: Send owner alert
8. **Google Sheets**: Update row status confirmation (`Automation Health=OK`)
9. **Error Handler**: On any module error set `Automation Health=Error` and notify admin

### Required mappings
- Lead Name ← Form: Full Name
- Phone raw ← Form: Phone Number
- Service Needed ← Form: Service Needed
- Area ← Form: Suburb / Area
- Message ← Form: Message / Details
- Budget ← Form: Budget

## Scenario B — Instant acknowledgement
1. Trigger: New row in sheet where Status=New
2. Router by `Business Hours` boolean
3. In-hours template send
4. After-hours template send
5. Log send timestamp

## Scenario C — Escalation watchdog
1. Trigger: Schedule every 5 minutes
2. Search rows where Status=New and CreatedAt older than SLA
3. Route by elapsed minutes:
   - >5m => L1
   - >15m => L2
   - >30m => L3
4. Notify respective contacts
5. Update escalation fields

## Scenario D — Weekly KPI digest
1. Trigger weekly Monday 08:00 SAST
2. Aggregate counts by status + SLA compliance
3. Build summary table
4. Send Gmail summary to owner
