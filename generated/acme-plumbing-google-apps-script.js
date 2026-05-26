/**
 * Speed-to-Lead SA — Google Apps Script Template
 *
 * What this does:
 * 1) Creates/validates the lead log sheet + headers.
 * 2) Applies data validation for status.
 * 3) Adds formulas for Lead ID, SAST time, phone normalization, response minutes.
 * 4) Creates time-driven triggers:
 *    - Escalation watchdog every 5 minutes
 *    - Weekly KPI email every Monday 08:00 (script timezone)
 *
 * Setup:
 * - Open Extensions > Apps Script in your target Google Sheet.
 * - Paste this file.
 * - Update CONFIG values.
 * - Run install() once and grant permissions.
 */

const CONFIG = {
  SHEET_NAME: 'Lead Log',
  OWNER_EMAIL: 'owner@acme.co.za',
  ADMIN_EMAIL: 'ops@acme.co.za',
  BUSINESS_NAME: 'Acme Plumbing',
  PRIMARY_CONTACT: '+27821234567',
  BACKUP_CONTACT: '+27831234567',
  RESPONSE_SLA_MINUTES: 5,
  TIMEZONE: 'Africa/Johannesburg'
};

const HEADERS = [
  'Lead ID', 'Created At (UTC)', 'Local Time (SAST)', 'Source', 'Lead Name',
  'Phone (raw)', 'Phone (normalized)', 'Email', 'Service Needed', 'Area/Suburb',
  'Message', 'Budget', 'Consent Captured (Y/N)', 'Consent Timestamp', 'Status',
  'Owner Assigned', 'First Response At', 'Minutes to First Response',
  'Follow-up Due At', 'Last Follow-up At', 'Lead Score', 'Loss Reason',
  'Job Value (ZAR)', 'Notes', 'Escalation Level', 'Escalation Time',
  'Escalation Root Cause', 'Automation Health'
];

function install() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  ss.setSpreadsheetTimeZone(CONFIG.TIMEZONE);
  const sheet = ensureSheet_(ss, CONFIG.SHEET_NAME);
  ensureHeaders_(sheet, HEADERS);
  applyStatusValidation_(sheet);
  applyFormulas_(sheet);
  ensureTriggers_();
  SpreadsheetApp.flush();
}

function ensureSheet_(ss, name) {
  return ss.getSheetByName(name) || ss.insertSheet(name);
}

function ensureHeaders_(sheet, headers) {
  const headerRange = sheet.getRange(1, 1, 1, headers.length);
  headerRange.setValues([headers]);
  headerRange.setFontWeight('bold');
  sheet.setFrozenRows(1);
}

function applyStatusValidation_(sheet) {
  const values = ['New', 'Contacted', 'Qualified', 'Quoted', 'Closed', 'Lost'];
  const rule = SpreadsheetApp.newDataValidation()
    .requireValueInList(values, true)
    .setAllowInvalid(false)
    .build();
  sheet.getRange('O2:O').setDataValidation(rule);
}

function applyFormulas_(sheet) {
  const formulas = {
    A2: '=IF(B2="","","LD-"&TEXT(ROW()-1,"0000"))',
    C2: '=IF(B2="","",TEXT((VALUE(SUBSTITUTE(SUBSTITUTE(B2,"T"," "),"Z",""))+TIME(2,0,0)),"yyyy-mm-dd hh:mm"))',
    G2: '=IF(F2="","",IF(LEFT(REGEXREPLACE(F2,"[^0-9+]",""),1)="+",SUBSTITUTE(REGEXREPLACE(F2,"[^0-9+]",""),"+",""),IF(LEFT(REGEXREPLACE(F2,"[^0-9]",""),1)="0","27"&RIGHT(REGEXREPLACE(F2,"[^0-9]",""),LEN(REGEXREPLACE(F2,"[^0-9]",""))-1),REGEXREPLACE(F2,"[^0-9]",""))))',
    R2: '=IF(OR(B2="",Q2=""),"",ROUND((Q2-VALUE(SUBSTITUTE(SUBSTITUTE(B2,"T"," "),"Z","")))*1440,0))',
    S2: '=IF(B2="","",IF(O2="New",VALUE(SUBSTITUTE(SUBSTITUTE(B2,"T"," "),"Z",""))+TIME(0,5,0),IF(O2="Contacted",NOW()+TIME(2,0,0),"")))'
  };

  Object.entries(formulas).forEach(([cell, formula]) => sheet.getRange(cell).setFormula(formula));
}

function escalationWatchdog() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName(CONFIG.SHEET_NAME);
  if (!sheet) return;

  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  const data = sheet.getRange(2, 1, lastRow - 1, HEADERS.length).getValues();
  const now = new Date();
  const alerts = [];

  data.forEach((row, i) => {
    const status = row[14];
    const created = parseUtc_(row[1]);
    if (status !== 'New' || !created) return;

    const mins = Math.floor((now.getTime() - created.getTime()) / 60000);
    let nextLevel = '';
    if (mins > 30) nextLevel = 'L3';
    else if (mins > 15) nextLevel = 'L2';
    else if (mins > CONFIG.RESPONSE_SLA_MINUTES) nextLevel = 'L1';

    if (!nextLevel) return;

    const currentLevel = row[24] || '';
    if (currentLevel === nextLevel) return;

    const rowNumber = i + 2;
    sheet.getRange(rowNumber, 25).setValue(nextLevel);
    sheet.getRange(rowNumber, 26).setValue(new Date().toISOString());
    sheet.getRange(rowNumber, 28).setValue('OK');

    alerts.push({ rowNumber, nextLevel, leadName: row[4], service: row[8], phone: row[6] || row[5] });
  });

  if (alerts.length) sendEscalationEmail_(alerts);
}

function weeklyKpiDigest() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName(CONFIG.SHEET_NAME);
  if (!sheet) return;

  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  const data = sheet.getRange(2, 1, lastRow - 1, HEADERS.length).getValues();

  const counters = { New: 0, Contacted: 0, Qualified: 0, Quoted: 0, Closed: 0, Lost: 0 };
  let slaMet = 0;
  let responded = 0;

  data.forEach(row => {
    const status = row[14];
    if (counters[status] !== undefined) counters[status]++;
    const mins = Number(row[17]);
    if (!Number.isNaN(mins) && mins >= 0) {
      responded++;
      if (mins <= CONFIG.RESPONSE_SLA_MINUTES) slaMet++;
    }
  });

  const slaPct = responded ? ((slaMet / responded) * 100).toFixed(1) : '0.0';
  const body = [
    `Business: ${CONFIG.BUSINESS_NAME}`,
    `Total Leads: ${data.length}`,
    `SLA Met: ${slaMet}/${responded} (${slaPct}%)`,
    '',
    'Status Counts:',
    `- New: ${counters.New}`,
    `- Contacted: ${counters.Contacted}`,
    `- Qualified: ${counters.Qualified}`,
    `- Quoted: ${counters.Quoted}`,
    `- Closed: ${counters.Closed}`,
    `- Lost: ${counters.Lost}`
  ].join('\n');

  MailApp.sendEmail(CONFIG.OWNER_EMAIL, `Weekly KPI Digest — ${CONFIG.BUSINESS_NAME}`, body);
}

function ensureTriggers_() {
  const triggers = ScriptApp.getProjectTriggers();
  const hasEscalation = triggers.some(t => t.getHandlerFunction() === 'escalationWatchdog');
  const hasWeekly = triggers.some(t => t.getHandlerFunction() === 'weeklyKpiDigest');

  if (!hasEscalation) {
    ScriptApp.newTrigger('escalationWatchdog').timeBased().everyMinutes(5).create();
  }

  if (!hasWeekly) {
    ScriptApp.newTrigger('weeklyKpiDigest').timeBased().onWeekDay(ScriptApp.WeekDay.MONDAY).atHour(8).create();
  }
}

function sendEscalationEmail_(alerts) {
  const lines = alerts.map(a =>
    `Row ${a.rowNumber} | ${a.nextLevel} | ${a.leadName} | ${a.service} | ${a.phone}`
  );
  const body = ['Escalation alerts triggered:', '', ...lines].join('\n');
  MailApp.sendEmail({
    to: CONFIG.OWNER_EMAIL,
    cc: CONFIG.ADMIN_EMAIL,
    subject: `Escalation Alerts — ${CONFIG.BUSINESS_NAME}`,
    body
  });
}

function parseUtc_(value) {
  if (!value) return null;
  const d = new Date(value);
  return Number.isNaN(d.getTime()) ? null : d;
}
