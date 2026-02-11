---
title: "7 Commits, 1 Session: Building a Live Feedback Pipeline with AI"
tags: cloudflare-workers, dogfooding, ai-assisted-dev, education, feedback-loops
---

# 7 Commits, 1 Session: Building a Live Feedback Pipeline with AI

*From empty scaffold to a live, passphrase-gated feedback loop — deployed on Cloudflare Workers, tracked in BEADS, mobile-audited, and favicon'd — in one AI-assisted build session.*

---

## Context

I'm building an **AI-Aligned Lesson Builder** for Maryland CS educators. The tool helps teachers create lessons that bridge the gap between Maryland's 2018 CS standards and the 2025 CSTA AI Learning Priorities — a gap where one set of standards mentions AI exactly once and the other defines 60+ AI learning outcomes.

The product is a static PRD site today, hosted on GitHub Pages, with interactive Python playgrounds (Pyodide) and a Cloudflare Worker proxying Groq API calls. Think: a living document that's also a demo of what the agent will eventually build.

But a document nobody can give feedback on is just a monologue. I needed a feedback loop — and I needed it today.

## What We Built

Here's what went from idea to production in a single session, commit by commit.

### 1. The Feedback Pipeline (Form to KV to BEADS)

The core build: a passphrase-gated feedback form on the live site that routes through a Cloudflare Worker into KV storage, then gets pulled into a local BEADS issue tracker.

**How it flows:**

```
User fills form on site
  -> Client-side SHA-256 passphrase check (human gate)
  -> POST /feedback to CF Worker
  -> Server-side passphrase validation
  -> PII auto-redaction (email, phone, SSN, credit card)
  -> Honeypot + timing gate (bot defense)
  -> Rate limiting (env-configurable)
  -> Store in KV as pending:{id}
  -> pull-feedback.sh pulls from KV
  -> bd create assigns a BEADS issue
  -> POST /feedback/ack marks items as processed
```

The passphrase gate is intentional. This is a dogfood tool for authorized reviewers — not a public comment box. The passphrase is shared in workshops and PD sessions. If you don't know it, you can't submit. Simple, no auth infrastructure required.

**Why it matters for educators:** When this tool goes live in workshops, facilitators and participating teachers can submit feedback directly from the page they're using. No context-switching to a separate form. No GitHub account needed. Just type and submit.

### 2. The bd Import Pivot

This was the session's best debugging story. The pull script originally used `bd import` to batch-load feedback items from a JSONL file. Three errors later, we'd learned that:

- **Type mismatch**: The Worker stores priority as `"P2"` (string). BEADS expects an integer. JSON unmarshal failed.
- **Prefix mismatch**: BEADS IDs follow a `project-prefix-number` pattern. Our feedback IDs (`fb20260211c8b`) don't have hyphens. Import rejected them.
- **Rename failed too**: The `--rename-on-import` flag couldn't parse IDs without hyphens.

**The fix:** Replace the entire `bd import` approach with `bd create` per item, using `--external-ref` to preserve the original feedback ID as a cross-reference. BEADS assigns its own properly-prefixed ID. Clean separation of concerns.

```bash
BD_ID=$(bd create "$TITLE" \
  -d "$DESC" \
  -p "$PRIORITY" \
  --external-ref "$ID" \
  2>&1)
```

Sometimes the right fix isn't patching the integration — it's rethinking which tool owns which responsibility.

### 3. Mobile-First Audit & Hamburger Nav

With the pipeline working, I audited the entire 2,400-line `index.html` at 375px (iPhone SE). Found and fixed:

- **A real bug**: The error handler referenced `feedback-submit` but the button ID was `feedback-submit-btn`. When submission failed, the "Sending..." state never cleared.
- **Touch targets**: Buttons were ~30px tall. WCAG minimum is 44px. Fixed across all interactive elements.
- **Focus-visible styles**: Keyboard users couldn't see which element was focused. Added `:focus-visible` outlines.
- **Hamburger nav**: Built a CSS-driven hamburger menu with proper `aria-expanded`, auto-close on link tap, and SVG icon swap. Hidden on desktop, visible on mobile.

### 4. Environment-Based Rate Limiting

The Worker's rate limiter was hardcoded to 20 requests per hour. Now it reads `RATE_LIMIT_PER_MINUTE` from the Cloudflare dashboard — changeable without redeploying. The error message is dynamic too, so operators see the actual limit.

### 5. The Favicon (Yes, It Counts)

A 404 in the console is a paper cut. An SVG favicon — blue rounded rect with "AI" text and a subtle network node — eliminates it and brands every browser tab. Seven lines of SVG, one `<link>` tag, zero build tools.

## What We Learned

**Integration boundaries are where bugs live.** The Worker stores data one way, BEADS expects it another way, and the pull script is the translation layer. Every type mismatch and format incompatibility surfaced at these seams. The lesson: test end-to-end early, not just each piece in isolation.

**Env bindings beat hardcoded values.** Moving the rate limit to an environment variable seems trivial, but it means operations changes don't require code changes. For a CF Worker, that's the difference between a dashboard toggle and a full `wrangler deploy`.

**Mobile auditing catches real bugs.** The feedback button ID mismatch was invisible on desktop (success path worked fine). It only mattered when an error occurred — and only became obvious when testing the full flow at mobile resolution where every UI state is more visible.

## Challenges

**KV eventual consistency.** After submitting feedback, the first pull returned zero items. A 3-second delay was needed. For a dogfood tool with low volume, this is fine. At scale, you'd want a webhook or polling approach.

**BEADS JSONL isn't git-tracked by design.** The `.gitignore` explicitly excludes `issues.jsonl` — it's local state, like a SQLite database. This means issue tracking is per-machine unless you use `bd sync`. Took a minute to understand why `git add` was being refused.

**Single-file architecture has limits.** The entire site is one 2,400-line `index.html`. Adding the hamburger nav meant weaving CSS, HTML, and JS into specific locations across the file. A component framework would help, but for a static GitHub Pages site with zero build step, the single-file approach keeps deployment trivial.

## What's Next

- **SvelteKit frontend**: The scaffolded `frontend/` directory has PocketFlow agent nodes, WebLLM integration, and a Chat component — all dormant. Wiring these up is the next major milestone.
- **Standards crosswalk**: The MSDE-to-CSTA mapping that powers the agent's lesson generation. Currently "Not Started" in the knowledge base table.
- **Workshop pilot**: The feedback loop exists so real teachers can use the tool and tell us what's missing. Time to put it in front of people.

## Try It Yourself

The live site is at [w4ester.github.io/ai-workshop-cs](https://w4ester.github.io/ai-workshop-cs/). The interactive Python playgrounds work on any device — no install, no login. If you're a Maryland CS educator or PD facilitator and want to try the feedback form, reach out for the passphrase.

The code is open: [github.com/w4ester/ai-workshop-cs](https://github.com/w4ester/ai-workshop-cs).

---

*February 11, 2026 — Will F.*
