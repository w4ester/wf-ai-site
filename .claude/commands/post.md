---
description: Publish a draft post to wf-ai-site (or list available drafts)
argument_hint: "[draft-slug] or leave empty to list drafts"
---

# Publish a Post to WF-AI Site

You are helping the user publish a blog post to their wf-ai-site (https://w4ester.github.io/wf-ai-site).

## The Correct Workflow

Posts should flow through drafts before publishing:

```
/blog → drafts/{slug}.md → /post {slug} → live on site
```

## Commands

### If no argument provided: List drafts

```bash
cd /Users/willf/wf-ai-site && python manager.py drafts
```

Show the user what drafts are available and ask which one to publish.

### If draft slug provided: Publish that draft

1. **Verify the draft exists:**
   ```bash
   cat /Users/willf/wf-ai-site/drafts/{slug}.md
   ```

2. **Review for inclusive language** before publishing:
   - **"parents/guardians"** or **"caregivers"** - never just "parents"
   - **"children and young people"** - not just "kids" when discussing teens
   - **"families"** - acknowledge diverse structures
   - **Economic access** - don't assume everyone can "buy" solutions
   - **Technical access** - acknowledge varying skill levels

   Search for: "parents", "kids", "buy", "family" and review each.

3. **Publish the draft:**
   ```bash
   cd /Users/willf/wf-ai-site && python manager.py publish-draft {slug}
   ```

4. **Update RSS feed:**
   ```bash
   cd /Users/willf/wf-ai-site && python manager.py rss
   ```

5. **Deploy** - Commit and push:
   ```bash
   cd /Users/willf/wf-ai-site && git add . && git commit -m "New post: {TITLE}

Built by w4ester & ai orchestration" && git push
   ```

## If User Wants to Post Directly (Without Draft)

If the user insists on posting without going through drafts, remind them:

> "The recommended workflow is `/blog` → draft → `/post`. This lets you review before publishing and keeps source markdown archived in `posts/`."

If they still want to proceed directly:
1. Save to `drafts/{slug}.md` first anyway
2. Then immediately publish with `publish-draft`

This ensures source is always archived.

## Quick Reference

| Command | What it does |
|---------|--------------|
| `/blog` | Write a new post → saves to `drafts/` |
| `/post` | List available drafts |
| `/post {slug}` | Publish draft to live site |
| `manager.py drafts` | List drafts |
| `manager.py publish-draft {slug}` | Publish + archive to `posts/` |

## Content Tips

- Markdown is supported (bold, links, code blocks, etc.)
- Keep posts concise - this is a digital garden, not long-form essays
- Good tags: ai, local-llm, projects, thoughts, tools, baltimore-ai, guardian, families

---

**Let's GrOw!** 🌱
