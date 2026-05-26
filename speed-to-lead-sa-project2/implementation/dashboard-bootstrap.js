/**
 * Dashboard bootstrap for Speed-to-Lead Lead Log workbook.
 *
 * Run createDashboard() in Apps Script after install().
 */
function createDashboard() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const lead = ss.getSheetByName('Lead Log');
  if (!lead) throw new Error('Lead Log sheet not found');

  let dash = ss.getSheetByName('Dashboard');
  if (!dash) dash = ss.insertSheet('Dashboard', 0);
  dash.clear();

  const headers = [['Metric', 'Value', 'Target', 'Status', 'Last Updated', 'Notes']];
  dash.getRange(1, 1, 1, headers[0].length).setValues(headers).setFontWeight('bold');
  dash.setFrozenRows(1);

  const metrics = [
    ['Total Leads (7d)'],
    ['Contacted Leads (7d)'],
    ['Contact Rate % (7d)'],
    ['Closed Leads (7d)'],
    ['Close Rate % (7d)'],
    ['Median First Response (min, 7d)'],
    ['SLA Met % (7d)']
  ];
  dash.getRange(2, 1, metrics.length, 1).setValues(metrics);

  dash.getRange('B2').setFormula('=COUNTIFS("Lead Log"!B:B,">="&NOW()-7)');
  dash.getRange('B3').setFormula('=COUNTIFS("Lead Log"!B:B,">="&NOW()-7,"Lead Log"!O:O,"Contacted")+COUNTIFS("Lead Log"!B:B,">="&NOW()-7,"Lead Log"!O:O,"Qualified")+COUNTIFS("Lead Log"!B:B,">="&NOW()-7,"Lead Log"!O:O,"Quoted")+COUNTIFS("Lead Log"!B:B,">="&NOW()-7,"Lead Log"!O:O,"Closed")');
  dash.getRange('B4').setFormula('=IF(B2=0,0,B3/B2)');
  dash.getRange('B5').setFormula('=COUNTIFS("Lead Log"!B:B,">="&NOW()-7,"Lead Log"!O:O,"Closed")');
  dash.getRange('B6').setFormula('=IF(B2=0,0,B5/B2)');
  dash.getRange('B7').setFormula('=IFERROR(MEDIAN(FILTER("Lead Log"!R:R,"Lead Log"!B:B>=NOW()-7,"Lead Log"!R:R>0)),0)');
  dash.getRange('B8').setFormula('=IFERROR(COUNTIFS("Lead Log"!B:B,">="&NOW()-7,"Lead Log"!R:R,"<="&5,"Lead Log"!R:R,">0")/COUNTIFS("Lead Log"!B:B,">="&NOW()-7,"Lead Log"!R:R,">0"),0)');

  dash.getRange('C4').setValue(0.80);
  dash.getRange('C6').setValue(0.20);
  dash.getRange('C7').setValue(5);
  dash.getRange('C8').setValue(0.85);

  dash.getRange('D4').setFormula('=IF(B4>=C4,"🟢 On Target","🔴 Below Target")');
  dash.getRange('D6').setFormula('=IF(B6>=C6,"🟢 On Target","🔴 Below Target")');
  dash.getRange('D7').setFormula('=IF(B7<=C7,"🟢 On Target","🔴 Below Target")');
  dash.getRange('D8').setFormula('=IF(B8>=C8,"🟢 On Target","🔴 Below Target")');

  dash.getRange('E2:E8').setFormula('=NOW()');
  dash.getRange('B4:B4,B6:B6,B8:B8,C4:C4,C6:C6,C8:C8').setNumberFormat('0.00%');
  dash.autoResizeColumns(1, 6);
}
