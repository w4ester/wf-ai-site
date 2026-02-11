---
title: "Zero Unauthorized Credentials: Building an Auditable Career Guidance AI"
tags: cte, education, ai, local-first, privacy, maryland, open-source, audit
---

# Zero Unauthorized Credentials

*Building a career guidance AI that earns trust by showing its work.*

---

What if a career guidance tool could tell you, with certainty, that every credential it recommends is officially approved by the state?

Not "we try to keep it updated." Not "sources may vary." A verifiable claim: **zero unauthorized credentials** out of 209 industry-recognized credentials, audited against the official Maryland State Department of Education approved list.

That's not a marketing promise. It's a SQL query.

---

## The World As It Is

A high school student in Maryland walks into their counselor's office. They're interested in automotive technology, or cybersecurity, or nursing. They want to know: *What credentials can I earn? Where do they lead? Which colleges accept them?*

The counselor has a PDF from 2022. Maybe a spreadsheet. The student goes home and asks ChatGPT, which confidently invents credentials that don't exist and names colleges that don't offer the program.

This is the state of career guidance for most students:

- **Scattered data.** PDFs, spreadsheets, and institutional catalogs that don't talk to each other.
- **Cloud tools that track everything.** The "free" AI chatbots collect conversations, build profiles, sell attention. A 16-year-old asking about career options becomes a data point.
- **Opaque recommendations.** When an AI suggests a credential, there's no way to verify it against the official list. No citations, no audit trail.
- **Stale information.** By the time a PDF makes it through the approval process, programs have changed, credentials have been added or retired, and new institutions have opened pathways.

The result: students get bad data, families can't verify it, and counselors spend their time navigating bureaucracy instead of advising.

---

## The World As It Could Be

Imagine a different tool. One that:

- **Runs locally.** No accounts, no tracking, no cookies. Your questions stay on your device.
- **Shows its sources.** Every answer cites the actual crosswalk data. Click through to see which programs at which institutions offer which credentials.
- **Is auditable.** The entire database — 818 pathway connections across 48 CTE programs and 42 Maryland institutions — is open for inspection. Every credential maps to the MSDE-approved list.
- **Responds to feedback.** When an educator says "you're missing Bowie State" or "that CTSO description isn't quite right," the fix ships in hours, not semesters.
- **Treats privacy as architecture, not policy.** No login, no analytics, no third-party scripts. The privacy page isn't legal boilerplate — it's a technical audit showing exactly what the system does and doesn't collect.

This is the Maryland CTE Crosswalk. And last week, we put it through the hardest test we could think of: we asked educators to break it.

---

## The Insight

### The Data Model

The crosswalk maps the full landscape of Maryland CTE:

| Metric | Count |
|--------|-------|
| Pathway connections | 818 |
| CTE programs | 48 |
| Maryland institutions | 42 |
| Community colleges | 16 |
| Universities | 26 |
| Career clusters | 14 |
| Industry-recognized credentials | 209 |

Every row represents a real pathway: a high school CTE program, connected to a postsecondary institution, with the credentials a student can earn along the way. The composite key is `(cluster_code, hs_program, institution_name)` — no duplicates, no ghosts.

### The Audit Methodology

The audit was straightforward:

1. **Extract** all unique IRCs from the database (183 at the time).
2. **Scrape** the official MSDE State-Approved List of Industry-Recognized Credentials — 210 credentials from the live page at `marylandpublicschools.org`.
3. **Compare.** Every one of our 183 credentials matched an MSDE-approved name. Zero unauthorized.
4. **Identify gaps.** 27 MSDE-approved credentials weren't yet in our crosswalk. One was an unclear placeholder ("AWS Certified Welding - BZ or NZ?"). We added the other 26.

The result: 183 → 209 unique IRCs, still at 100% compliance. Every credential a student sees through the crosswalk is one the state has officially recognized.

This matters because when a tool recommends a credential, a student might spend months preparing for it. Getting it wrong wastes their time and erodes trust in the system. Getting it right — and being able to *prove* it's right — is the minimum bar for responsible guidance.

---

## The Path: One Building Session, 13 Feedback Items, 7 Commits

The most interesting part isn't the architecture — it's how fast the system responds to real feedback. Here's what happened in a single session when educators reviewed the crosswalk:

### Commit 1: University coverage gaps
**`717a1b8`** — *Add 3 university program gaps (Bowie State, Coppin State, JHU)*

Feedback: "Where's Bowie State? Where's Coppin State?" Two HBCUs and Johns Hopkins were missing from specific program pathways. This is exactly the kind of gap that erodes trust — if a student at a Title I school doesn't see their likely institutions represented, the tool feels like it wasn't built for them.

### Commit 2: Remove non-Maryland CTSOs
**`8e6eafd`** — *Remove non-MD CTSOs (DECA, HOSA, TSA, FCCLA) from prompts and tooltip*

Feedback: "DECA isn't a Maryland CTSO." Correct — Maryland has specific Career and Technical Student Organizations (SkillsUSA, FFA, FBLA). We had included national CTSOs that don't operate as Maryland-designated organizations. Removed from both the AI prompts and the UI tooltip.

### Commit 3: Mobile-responsive stats bar
**`e03a41e`** — *Make crosswalk stats bar mobile-responsive (feedback #10)*

A counselor pulled up the crosswalk on their phone during a student meeting. The stats bar — showing 818 connections, 42 institutions, 16 community colleges, 26 universities — was cut off on mobile. Fixed: the stats now wrap properly on small screens.

### Commit 4: The IRC audit
**`933f887`** — *Add 26 missing MSDE-approved IRCs across 9 programs (feedback #8)*

This was the big one. The audit compared our 183 unique IRCs against the 210 on the official MSDE list. Result:

- **0 unauthorized credentials** in our database
- **27 MSDE-approved credentials** not yet in our crosswalk
- **26 added** across 9 programs (1 skipped as an unclear MSDE placeholder)

The breakdown:
- Automotive Technology: +12 IRCs (ASE A-series full certifications)
- Medium-Heavy Truck Equipment: +3 (diesel, forklift, hazmat)
- 3D Animation Game Design: +3 (web animation, app development)
- Graphic Communications: +4 (web design, web development)
- Engineering: +3 (logistics, Onshape CAD)
- Machining: +3 (logistics, Onshape CAD)
- Certified Nursing Assistant: +1 (phlebotomy)
- Biomedical Science: +1 (phlebotomy)
- Emergency Medical Technician: +2 (paramedic certifications)

### Commit 5: 3D Animation community college gaps
**`c0f4acd`** — *Add 3 CC gaps to 3D Animation Game Design (feedback #5)*

Three community colleges offering relevant programs weren't in the 3D Animation pathway. Added.

### Commit 6: CTSO terminology
**`a9d46c6`** — *Add cocurricular/applied-learning terminology to CTSO descriptions (feedback #1)*

An educator noted that CTSOs are more accurately described as "cocurricular" and "applied learning" organizations, not just "student organizations." Language matters — these terms carry specific meaning in the CTE community and affect how the AI explains them to students.

### Commit 7: The data foundation
Before the feedback session, we had already laid the groundwork with a significant data commit:

**`f30d94c`** — *Add 10 rows across agriculture, architecture, facilities, horticulture*

This and prior commits in the session added coverage for underrepresented programs — agriculture, architecture, facilities maintenance, horticulture — programs that serve students heading into essential trades.

---

## The Architecture Behind the Audit

For the builders reading this, here's what makes the audit possible:

**PostgreSQL with pgvector.** The crosswalk data lives in a single `crosswalks` table. IRCs are stored as semicolon-separated strings in the `industry_credentials` column. This is intentionally simple — no credential-normalization microservice, no complex join tables. The data model is straightforward enough that a SQL query *is* the audit.

**Local-first deployment.** The entire stack — PostgreSQL, FastAPI backend, SvelteKit frontend — runs in Docker containers. No external dependencies, no cloud database, no API keys for the core crosswalk functionality. The RAG-powered chat uses a local embedding model.

**Privacy as architecture.** No user accounts. No cookies. No analytics scripts. No third-party resources. The privacy page includes a technical audit table showing every data flow in the system. When we say "your questions stay on your device," that's not a policy — it's the absence of any mechanism to collect them.

**Feedback loop.** Thumbs up/down on chat responses stores only the question-answer pair — no user identification. This creates an RLHF-style signal without surveillance.

---

## Who This Is For

**Students and families.** You can look up your CTE program, see which colleges connect to it, and know that every credential listed is MSDE-approved. No account needed, no data collected.

**School counselors.** A tool you can pull up during a student meeting — on your phone, on your desktop — that shows real pathway data with citations. When something is wrong, tell us and it gets fixed fast.

**CTE administrators and educators.** The crosswalk data is open. The audit methodology is documented. The commit history shows every change. Use it as a reference, point out gaps, help us get it right.

**Builders.** The stack is straightforward: PostgreSQL, FastAPI, SvelteKit, Docker. The interesting part isn't the technology — it's the methodology. Audit your AI's recommendations against authoritative sources. Make the audit reproducible. Ship the fixes fast.

---

## The Invitation

The Maryland CTE Crosswalk is live. You can:

- **Browse the crosswalk** — 818 pathway connections across 48 programs and 42 institutions
- **Ask the AI** — grounded in the actual crosswalk data, with citations
- **Check our work** — the commit history, the audit SQL, the MSDE comparison are all visible
- **Give feedback** — every suggestion makes the data better

The thesis is simple: career guidance tools should be auditable, private, and responsive to the communities they serve. The credential data should be verifiable against official sources. The feedback loop should be measured in hours, not semesters.

We started with a question: *What if a career guidance AI had zero unauthorized credentials?*

The answer turned out to be a SQL query, an afternoon of commits, and a willingness to show the work.

---

*The Maryland CTE Crosswalk is a local-first, privacy-sovereign career pathway assistant. It maps Maryland high school CTE programs to postsecondary institutions and industry-recognized credentials using data from MSDE, community college catalogs, and university program listings.*

*All 209 industry-recognized credentials have been audited against the MSDE State-Approved List. Zero unauthorized.*
