---
name: evidence-blog-writer
description: Transform drafts into publication-ready posts with voice preservation, absolute removal, source-backed numbers, and citations with proof maps. Use when refining a blog post for defensibility or when user says "make this defensible" or "add sources".
---

# Evidence-First Blog Writer

Transform raw or existing blog drafts into publication-ready posts that:
- Preserve the author's voice and structure
- Remove easy-to-attack absolutes ("always", "never", "everyone", "forever")
- Upgrade numeric and factual claims into verifiable, sourced statements
- Add inline citations and a proof map

Optimized for "local AI / infrastructure / family sovereignty" posts but works for most technical writing.

## When to Use This Skill

- User has a draft that needs sourcing/citations
- User says "make this defensible" or "add sources"
- User wants to upgrade a post from opinion to evidence-backed
- Post contains numeric claims (model sizes, benchmark scores, prices)
- Post contains licensing claims that need verification

## Inputs

**Required:**
- `draft_text`: The full original post text (markdown preferred)
- `post_date`: ISO date (YYYY-MM-DD) for the post header

**Optional:**
- `voice_profile`: Short description of voice (default: "practical, builder energy, optimistic, community-first, ends with Let's GrOw")
- `must_include`: List of required insertions (models/tools/sections)
- `must_avoid`: List of claims or phrases to avoid
- `citation_style`: "footnotes" (default) or "[1]" style

## Outputs

Deliver these artifacts:

1. **final_post_markdown** - polished post with voice preserved, inline citations, Resources section
2. **references_section** - link list aligned to citation markers
3. **proof_map** - bullet list mapping each high-stakes claim → citation(s)
4. **claim_log** (optional) - compact table of claims with status

## Hard Rules (Non-Negotiable)

### Voice Preservation
- Keep the author's rhythm, headings, punchy lines, and signature phrases
- Only rewrite where needed for accuracy, defensibility, or clarity
- Keep distinctive phrases (e.g., "Local AI as infrastructure," "Let's GrOw!") unless asked to remove

### Proofability Standard
- Any **numeric claim** (speeds, prices, sizes, scores, RAM/VRAM requirements, context windows) MUST be cited
- Any **licensing claim** MUST be cited from a primary source (official release, model card, license text)
- Any **benchmark claim** MUST be cited to the benchmark's primary page (leaderboard/methodology)
- Any **policy/privacy claim** about a provider MUST be cited to the provider's policy or softened to general language

### Absolute Language Policy

Replace absolutes with defendable language:

| Avoid | Replace With |
|-------|-------------|
| "every" | "many / most / typical / often" |
| "forever" | "for some period / subject to retention policies" |
| "no downstream restrictions" | "permissive, with standard obligations (e.g., license notice)" |
| "always" | "typically / in most cases / by default" |
| "never" | "rarely / not typically / in few cases" |
| "everyone" | "many people / most users / typical users" |

### Source Quality Hierarchy

Use sources in this order of preference:
1. Official docs / model cards / license texts / benchmarks
2. Maintainer repos (GitHub orgs)
3. Reputable technical orgs (Mozilla, Apple, etc.)
4. Community benchmarks ONLY if clearly labeled as community + not used for high-stakes claims

## Workflow

### Step 1: Claim Audit

Scan the draft and build a claim list. Tag each claim as:

| Type | Examples |
|------|----------|
| NUM | numbers, sizes, speed, price, percentages |
| LICENSE | Apache/MIT/Community license, restrictions |
| BENCH | benchmark claims, leaderboard positions |
| POLICY | logging, retention, privacy statements |
| FEATURE | context length, MoE active params, capabilities |
| HISTORY | dates, releases, "in 2022 this was…" |
| ANECDOTE | personal experience, "in my testing" |

**Flag high-risk claims:**
- "logged forever"
- exact performance claims without benchmark source
- product pricing without date/source
- "default" statements about industry behavior

### Step 2: Research & Source Acquisition

For each NUM/LICENSE/BENCH/POLICY/FEATURE claim:
- Find a primary source
- Prefer sources that display the exact value you will state
- If the exact value varies by config, report a range and cite representative entries

### Step 3: Rewrite with Defendable Certainty

- Preserve structure and voice
- Replace absolutes with defensible phrasing
- Convert fragile numbers into sourced values or ranges
- If a claim cannot be sourced quickly:
  - Downgrade to anecdote ("In my experience…"), OR
  - Remove it, OR
  - Reframe as "can" / "often" + explain the dependency

### Step 4: Insert Citations

Use footnotes by default:
- Inline marker: `...works offline.[^7]`
- Add a References section with URLs at the end

Place citations immediately after the sentence they support.

### Step 5: Add Verifiable Tables

When listing models/tools/hardware, prefer a table with:
- Model tag (exactly as user would type it)
- Download size (from a library page)
- Default context (from docs/tags)
- Source citation for each row

### Step 6: Build Proof Map

Create 10-20 bullets mapping important claims to citations:

```markdown
## Proof Map

- Qwen3 Apache 2.0 license → [^1] (Qwen release notes)
- qwen3:14b ~9.3GB download → [^2] (Ollama tags page)
- LocalScore 1000/250/100 thresholds → [^7] (LocalScore about page)
- Mac Studio 512GB unified memory → [^10] (Apple store page)
```

### Step 7: Final Quality Checks

- The post should read naturally (not like a research paper)
- Citations should not interrupt the voice
- Every high-stakes claim must have a citation or be softened
- Read aloud - does it still sound like the author?

## Done Criteria

This skill is complete when:
- [ ] Final post is publishable without edits
- [ ] No "easy dunk" absolutes remain
- [ ] Every number and license claim is source-backed
- [ ] A reader can verify model sizes, licensing, and benchmark numbers with the links provided
- [ ] Voice is preserved - still sounds like the author

## Voice Profile: wf-ai-site

For posts on wf-ai-site, use this voice:
- **Builder energy** - practical, hands-on, "here's what actually works"
- **Family sovereignty focus** - privacy, control, ownership
- **Optimistic but grounded** - possibilities without hype
- **Community-first** - "we" for shared goals, "I" for personal experience
- **Signature closer** - "Let's GrOw!"

## Common Proof Targets (Local AI Posts)

Source these every time they appear:
- Model license (link to model card or license text)
- Model sizes (link to Ollama/HuggingFace tag page)
- Context windows (link to official docs or tag page)
- Benchmark methodology + threshold interpretation
- Hardware recommendations (VRAM/unified memory guidelines)
- Pricing (use official store pages and include access date)

## Example Claim Log

| # | Claim | Type | Action | Citation |
|---|-------|------|--------|----------|
| 1 | Qwen3 is Apache 2.0 licensed | LICENSE | sourced | [^1] |
| 2 | qwen3:14b is ~9.3GB download | NUM | sourced | [^2] |
| 3 | "cloud prompts are logged forever" | POLICY | softened | — |
| 4 | LocalScore 250 is "passable" | BENCH | sourced | [^7] |
| 5 | Mac Studio supports 512GB | FEATURE | sourced | [^10] |

---

**Let's GrOw!**
