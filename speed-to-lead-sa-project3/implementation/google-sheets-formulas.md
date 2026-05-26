# Google Sheets Formula Pack

## Assumptions
- Row 1 contains headers.
- Data starts at row 2.
- Header names match `implementation/lead-log-template.csv` exactly.

## 1) Lead ID (column A)
In `A2`:
```gs
=IF(B2="","","LD-"&TEXT(ROW()-1,"0000"))
```

## 2) Local Time (SAST) from Created At UTC (column C)
In `C2`:
```gs
=IF(B2="","",TEXT((VALUE(SUBSTITUTE(SUBSTITUTE(B2,"T"," "),"Z",""))+TIME(2,0,0)),"yyyy-mm-dd hh:mm"))
```

## 3) Phone normalization (column G)
In `G2`:
```gs
=IF(F2="","",IF(LEFT(REGEXREPLACE(F2,"[^0-9+]",""),1)="+",SUBSTITUTE(REGEXREPLACE(F2,"[^0-9+]",""),"+",""),IF(LEFT(REGEXREPLACE(F2,"[^0-9]",""),1)="0","27"&RIGHT(REGEXREPLACE(F2,"[^0-9]",""),LEN(REGEXREPLACE(F2,"[^0-9]",""))-1),REGEXREPLACE(F2,"[^0-9]",""))))
```

## 4) Minutes to First Response (column R)
In `R2`:
```gs
=IF(OR(B2="",Q2=""),"",ROUND((Q2-VALUE(SUBSTITUTE(SUBSTITUTE(B2,"T"," "),"Z","")))*1440,0))
```

## 5) Follow-up due at (column S)
In `S2`:
```gs
=IF(B2="","",IF(O2="New",VALUE(SUBSTITUTE(SUBSTITUTE(B2,"T"," "),"Z",""))+TIME(0,5,0),IF(O2="Contacted",NOW()+TIME(2,0,0),"")))
```

## 6) Status data validation list
Allowed values:
- New
- Contacted
- Qualified
- Quoted
- Closed
- Lost

## 7) Conditional formatting rules
- `Status=New` and `NOW()-CreatedAt > 5min` => amber
- `Status=New` and `NOW()-CreatedAt > 30min` => red
- `Escalation Level` not blank => purple
