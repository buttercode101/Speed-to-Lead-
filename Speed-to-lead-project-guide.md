# Speed-to-Lead SA - Zero Budget Automation Project

**Project Name:** Speed-to-Lead SA  
**Version:** MVP v1.0 (Zero Budget Edition)  
**Creator:** Solo Builder  
**Location:** South Africa (Cape Town focus)  
**Start Date:** May 2026  
**Goal:** Build & sell simple, high-ROI instant lead response systems to local businesses.

## 1. Project Overview

This project delivers a **Speed-to-Lead** automation that:
- Captures new leads instantly (Google Form or WhatsApp)
- Logs them into a Google Sheet
- Sends real-time notification to the business owner
- Sends a personalized auto-reply to the customer
- Tracks everything for follow-up

**Why this sells well in South Africa right now:**
- WhatsApp is the #1 communication tool
- Most small businesses reply after hours or the next day
- Fast response can increase close rates 2x–3x
- Clear ROI (extra jobs/revenue)

**Target Clients:** Plumbers, electricians, panel beaters, real estate agents, dentists, home service businesses, coaches.

**Pricing (2026 SA Market):**
- Basic: R8,500
- Standard: R14,000
- Premium (with auto-reply): R18,000
- Monthly maintenance: R1,800

---

## 2. Tech Stack (All Free to Start)

| Tool              | Purpose                    | Cost     |
|-------------------|----------------------------|----------|
| Google Forms      | Lead capture               | Free     |
| Google Sheets     | Lead database & log        | Free     |
| Make.com          | Automation engine          | Free (1,000 ops/mo) |
| Gmail             | Owner notifications        | Free     |
| ManyChat          | Basic WhatsApp replies     | Free tier |
| Loom              | Demo & training videos     | Free     |

---

## 3. Step-by-Step Build Guide

### Phase 1: Create Google Form
1. Go to [forms.google.com](https://forms.google.com)
2. Create new form titled "**New Client Inquiry**"
3. Add fields:
   - Full Name (Short answer)
   - Phone Number (WhatsApp) (Short answer)
   - Service Needed (Short answer)
   - Suburb / Area (Short answer)
   - Message / Details (Paragraph)
   - Budget (optional) (Short answer)
4. Copy the live form link.

### Phase 2: Create Google Sheets Lead Log
Create spreadsheet named `Lead Log - [Client Business Name]`

**Exact Columns:**
- Timestamp
- Lead Name
- Phone Number
- Service Needed
- Area
- Message
- Budget
- Status (`New` / `Contacted` / `Qualified` / `Closed`)
- Notes
- Job Value (R)

---

### Phase 3: Make.com Automation (Detailed)

1. Go to [make.com](https://www.make.com) → Create new scenario
2. **Module 1**: Google Forms → **Watch Responses**
   - Connect Google account
   - Select your form
3. **Module 2**: Google Sheets → **Add Row**
   - Select the spreadsheet
   - Map all fields (use `now` for Timestamp)
4. **Module 3**: Gmail → **Send an Email**
   - To: Business owner’s email
   - Subject: `🚨 NEW LEAD: {{Full Name}} - {{Service Needed}} in {{Area}}`
   - Body: Include all lead details + direct link to Google Sheet
5. Save scenario and turn it **ON**

**Testing:**
- Fill the Google Form yourself
- Wait 10–30 seconds
- Check Sheet + Email

---

## 4. WhatsApp Reply Templates

**Instant Auto-Reply:**
