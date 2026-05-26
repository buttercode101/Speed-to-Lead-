## 10. Project #3: Follow-up & Nurture Sequences

**Project Name:** NurtureFlow SA  
**Version:** MVP v1.0  
**Difficulty:** Beginner+  
**Estimated Build Time:** 6–10 hours  
**Target Price:** R12,000 – R25,000 one-time + R2,000/month optional maintenance

### Why This Sells Extremely Well in South Africa
- Businesses spend money on leads but fail to follow up
- Most warm leads go cold after 1–2 contacts
- Perfect add-on to Speed-to-Lead clients
- High recurring value (monthly nurture campaigns)
- Works great for coaches, consultants, real estate agents, gyms, dental clinics, and service businesses

**Core Function:**  
When a lead submits a form or books a call, the system automatically sends a timed sequence of personalized follow-up messages (WhatsApp + Email) with value-driven content until the lead replies or books.

---

### Tech Stack (Free to Start)

| Tool              | Purpose                          | Cost      |
|-------------------|----------------------------------|-----------|
| Make.com          | Main automation engine           | Free      |
| Google Sheets     | Lead tracking                    | Free      |
| Gmail             | Email follow-ups                 | Free      |
| ManyChat          | WhatsApp sequences               | Free tier |
| Google Calendar   | Booking links                    | Free      |

---

### Step-by-Step Build Guide (Beginner Friendly)

#### Phase 1: Create Tracking Sheet
Create spreadsheet: `Nurture Leads - [Client Name]`

**Columns:**
- Timestamp
- Lead Name
- Phone
- Email
- Source (Form / Webinar / Ad)
- Service Interested
- Status (New → Nurturing → Booked → Closed → Lost)
- Last Contacted
- Next Follow-up
- Notes

#### Phase 2: Make.com Scenario (Main Flow)

1. **Module 1: Trigger**  
   - Google Forms → Watch Responses (or Gmail for form submissions)

2. **Module 2: Google Sheets**  
   - Add Row to Nurture Leads sheet

3. **Module 3: Filter**  
   - Only continue if Status = "New"

4. **Module 4: Send First Message (Instant)**  
   - ManyChat or Gmail → Send personalized thank you + value message

5. **Module 5: Scheduler**  
   - Add delay → 2 days  
   - Send Follow-up #2 (different value content)

6. **Module 6: Scheduler**  
   - Add delay → 4 days  
   - Send Follow-up #3 (soft call-to-action)

7. **Module 7: Stop Sequence**  
   - If lead replies or books → stop sending (use Filter)

**Example Message Sequence:**

**Message 1 (Immediate):**
