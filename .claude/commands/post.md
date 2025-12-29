---
description: Create and publish a new post to wf-ai-site
---

# Create a New Post for WF-AI Site

You are helping the user create a new post for their wf-ai-site blog (https://w4ester.github.io/wf-ai-site).

## Workflow

1. **Gather post details** - Ask the user for:
   - **Title**: A concise, engaging title
   - **Content**: The post body (markdown supported)
   - **Tags**: Optional comma-separated tags (e.g., ai, local-llm, projects)

2. **Create the post** - Run from the wf-ai-site directory:
   ```bash
   cd /Users/willf/wf-ai-site && python manager.py post "TITLE" "CONTENT" --tags TAGS
   ```

3. **Update RSS feed**:
   ```bash
   cd /Users/willf/wf-ai-site && python manager.py rss
   ```

4. **Ask about deployment** - Offer to commit and push:
   ```bash
   cd /Users/willf/wf-ai-site && git add . && git commit -m "New post: TITLE" && git push
   ```

## Content Tips

- Markdown is supported (bold, links, code blocks, etc.)
- Keep posts concise - this is a digital garden, not long-form essays
- Good tags: ai, local-llm, projects, thoughts, tools, baltimore-ai

## Inclusive Language Guidelines

Always review content for inclusive language before posting:

- **"parents/guardians"** - never just "parents" (acknowledges grandparents, foster families, aunts/uncles, chosen family)
- **"children and young people"** - not just "kids" when discussing teens
- **"families"** - acknowledge diverse structures (single-parent, blended, multigenerational, chosen)
- **Economic access** - don't assume everyone can "buy" solutions; include free/low-cost alternatives
- **Technical access** - acknowledge varying technical skill levels; avoid gatekeeping language
- **Cultural awareness** - recognize different cultural perspectives on family dynamics and child autonomy
- **Disability inclusion** - consider accessibility in digital tools discussions
- **Geographic diversity** - not everyone is in the US or has the same infrastructure

When editing, search for: "parents", "kids", "buy", "family" and review each for inclusivity.

## Start Now

Ask the user: "What would you like to post about? Give me a title and your content (markdown supported), and optionally some tags."
