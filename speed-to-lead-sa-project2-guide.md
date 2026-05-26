## 9. Next Project: Document Processing Automation (Project #2)

**Project Name:** DocProcess SA  
**Version:** MVP v1.0  
**Difficulty:** Beginner+ (builds on Speed-to-Lead skills)  
**Estimated Build Time:** 4–8 hours  
**Target Price:** R12,000 – R20,000 one-time

### Why This Sells Well in South Africa
- Many small businesses and accountants still manually type invoice data
- Saves expensive admin time (bookkeepers cost R15k–R30k/month)
- Reduces errors that cost real money
- Perfect for construction, retail, logistics, law firms, and accountants in Cape Town & Johannesburg

### Tech Stack (Mostly Free)
- Make.com (Free plan)
- Gmail / Email trigger
- Google Sheets
- PDF.co or free PDF parsers (limited free tier)
- Optional: WhatsApp notification

### Step-by-Step Build Guide (Beginner Version)

#### Phase 1: Create Google Sheet Template
Create a new spreadsheet: `Invoice Log - [Client Name]`

**Exact Columns:**
- Date Received
- Invoice Number
- Supplier/Vendor Name
- Invoice Date
- Total Amount (R)
- VAT Amount
- Description/Line Items
- Status (New / Processed / Flagged)
- Notes

#### Phase 2: Make.com Scenario

1. **Module 1: Trigger**  
   - Gmail → **Watch Emails**  
   - Filter: Subject contains "invoice" OR attachment is PDF

2. **Module 2: Extract Data from PDF**  
   - Use **PDF.co** (free tier) or **ParseHub** / simple text extractor  
   - Extract: Invoice Number, Date, Amount, Vendor

3. **Module 3: Google Sheets**  
   - **Add Row** to your Invoice Log sheet  
   - Map all extracted fields

4. **Module 4: Notification**  
   - Gmail → Send Email to business owner  
   - OR WhatsApp notification (via ManyChat)

5. **Optional Human Review Step**  
   - Add a Filter: If amount > R10,000 → flag for review

**Testing:**
- Email yourself a sample invoice PDF
- Check if it appears correctly in the Google Sheet

### Client Delivery for Document Processing
- Shared Make.com scenario
- Shared Google Sheet template
- Sample invoice test pack (5–10 real-looking PDFs)
- 15-minute training Loom video
- Basic rules for common suppliers

### Sales Script Snippet (WhatsApp)
