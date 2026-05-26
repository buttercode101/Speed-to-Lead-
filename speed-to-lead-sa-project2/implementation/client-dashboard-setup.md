# Client Dashboard Setup (Google Sheets)

This guide builds a simple, live KPI dashboard inside the same spreadsheet.

## 1) Create dashboard tab
- Add new sheet tab named `Dashboard`.
- Freeze row 1.
- Set A1:F1 headers:
  - Metric
  - Value
  - Target
  - Status
  - Last Updated
  - Notes

## 2) Core KPIs (rows 2-8)
Use these labels in column A:
- Total Leads (7d)
- Contacted Leads (7d)
- Contact Rate % (7d)
- Closed Leads (7d)
- Close Rate % (7d)
- Median First Response (min, 7d)
- SLA Met % (7d)

## 3) Dashboard formulas
Assumes `Lead Log` sheet with headers from `implementation/lead-log-template.csv`.

In `B2` (Total Leads 7d):
```gs
=COUNTIFS('Lead Log'!B:B,">="&NOW()-7)
```

In `B3` (Contacted 7d):
```gs
=COUNTIFS('Lead Log'!B:B,">="&NOW()-7,'Lead Log'!O:O,"Contacted")+COUNTIFS('Lead Log'!B:B,">="&NOW()-7,'Lead Log'!O:O,"Qualified")+COUNTIFS('Lead Log'!B:B,">="&NOW()-7,'Lead Log'!O:O,"Quoted")+COUNTIFS('Lead Log'!B:B,">="&NOW()-7,'Lead Log'!O:O,"Closed")
```

In `B4` (Contact Rate %):
```gs
=IF(B2=0,0,B3/B2)
```

In `B5` (Closed 7d):
```gs
=COUNTIFS('Lead Log'!B:B,">="&NOW()-7,'Lead Log'!O:O,"Closed")
```

In `B6` (Close Rate %):
```gs
=IF(B2=0,0,B5/B2)
```

In `B7` (Median First Response):
```gs
=IFERROR(MEDIAN(FILTER('Lead Log'!R:R,'Lead Log'!B:B>=NOW()-7,'Lead Log'!R:R>0)),0)
```

In `B8` (SLA Met %):
```gs
=IFERROR(COUNTIFS('Lead Log'!B:B,">="&NOW()-7,'Lead Log'!R:R,"<="&5,'Lead Log'!R:R,">0")/COUNTIFS('Lead Log'!B:B,">="&NOW()-7,'Lead Log'!R:R,">0"),0)
```

## 4) Targets
Set target values in column C:
- C4 (Contact Rate %): 0.80
- C6 (Close Rate %): 0.20
- C7 (Median First Response): 5
- C8 (SLA Met %): 0.85

## 5) Status logic (column D)
In `D4`:
```gs
=IF(B4>=C4,"🟢 On Target","🔴 Below Target")
```

In `D6`:
```gs
=IF(B6>=C6,"🟢 On Target","🔴 Below Target")
```

In `D7`:
```gs
=IF(B7<=C7,"🟢 On Target","🔴 Below Target")
```

In `D8`:
```gs
=IF(B8>=C8,"🟢 On Target","🔴 Below Target")
```

## 6) Last updated
In `E2:E8` use:
```gs
=NOW()
```
Format as date-time.

## 7) Visual polish
- Format % metrics (B4, B6, B8; C4, C6, C8) as Percentage.
- Add conditional formatting:
  - Cells containing "🟢" => green fill
  - Cells containing "🔴" => red fill

## 8) Client-share view
- Share sheet as view-only for client stakeholders.
- Pin `Dashboard` as first tab.
