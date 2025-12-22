# WF-AI Site

A minimal, terminal-driven static blog for AI experiments, projects, and ideas. Built with Tailwind CSS and managed via Python CLI.

**Live at:** [w4ester.github.io/wf-ai-site](https://w4ester.github.io/wf-ai-site)

## Features

- 🌓 **Dark/Light Mode** - Toggle with persistent localStorage preference
- 📡 **RSS Feed** - Auto-generated `feed.xml` for subscribers
- ✍️ **Markdown Support** - Write posts with full markdown formatting
- 🏷️ **Tags** - Categorize posts with hashtags
- ⚡ **Zero Build Step** - Pure HTML + Tailwind CDN, no bundler needed
- 🎨 **Shadcn-inspired UI** - Clean, modern design with terminal aesthetics

## Quick Start

```bash
# 1. Clone and navigate
git clone https://github.com/w4ester/wf-ai-site.git
cd wf-ai-site

# 2. Install markdown support (optional but recommended)
pip install markdown

# 3. Create your first post
python manager.py post "Hello World" "This is my **first** post!" --tags intro,ai

# 4. Update RSS feed
python manager.py rss

# 5. Preview locally (optional)
python -m http.server 8000
# Open http://localhost:8000
```

## Usage

### Create a Post

```bash
# Basic post
python manager.py post "Post Title" "Your content here with **markdown**"

# Post with tags
python manager.py post "My AI Experiment" "Built a RAG system today!" --tags ai,rag,local

# Multi-line content (use quotes)
python manager.py post "Longer Post" "First paragraph.

Second paragraph with a [link](https://example.com).

- Bullet point one
- Bullet point two"
```

### Other Commands

```bash
# Regenerate RSS feed
python manager.py rss

# List recent posts
python manager.py list
```

### Legacy Syntax (backwards compatible)

```bash
python manager.py "Title" "Content" "tag1,tag2"
```

## GitHub Pages Setup

### Option 1: User/Organization Site

1. Create repo named `<username>.github.io`
2. Push this code to the `main` branch
3. Site will be live at `https://<username>.github.io`

### Option 2: Project Site (Recommended)

1. Create a new repo (e.g., `wf-ai-site`)
2. Push this code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/<username>/wf-ai-site.git
   git push -u origin main
   ```
3. Go to repo **Settings** → **Pages**
4. Under "Source", select `main` branch and `/ (root)` folder
5. Click **Save**
6. Site will be live at `https://<username>.github.io/wf-ai-site`

### Update Site URL

Edit `manager.py` and update these lines at the top:

```python
SITE_URL = "https://yourusername.github.io/wf-ai-site"
SITE_TITLE = "Your Site Title"
SITE_DESCRIPTION = "Your site description"
AUTHOR = "Your Name"
```

Also update the footer link in `index.html`.

## Posting Workflow

```bash
# Write your post
python manager.py post "New Discovery" "Found an interesting pattern in..." --tags ai,discovery

# Regenerate RSS
python manager.py rss

# Commit and push
git add .
git commit -m "Add: New Discovery"
git push
```

GitHub Pages will automatically rebuild (takes ~1 minute).

## Customization

### Colors

Edit the CSS variables in `index.html` under `:root` and `.dark`:

```css
:root {
    --accent: 142 76% 36%;  /* Green accent - change hue for different color */
    /* ... other variables */
}
```

### Typography

The site uses:
- **Space Grotesk** - Headings and body
- **JetBrains Mono** - Code and terminal elements

Change in the `<head>` Google Fonts link and Tailwind config.

## File Structure

```
wf-ai-site/
├── index.html      # Main page with all posts
├── manager.py      # CLI tool for posting
├── feed.xml        # RSS feed (auto-generated)
└── README.md       # This file
```

## Tips

1. **Preview Before Pushing**: Use `python -m http.server 8000` to preview locally
2. **Backup**: Posts are stored directly in `index.html` - commit regularly
3. **RSS Readers**: Share `feed.xml` URL for people to subscribe
4. **MCP Integration**: Call `manager.py` from your AI workflows for automated posting

## Requirements

- Python 3.9+
- `markdown` library (optional, for rich formatting): `pip install markdown`

## License

MIT - Use freely, modify as needed.

---

*Built with ❤️ for the Baltimore AI Producers Lab*
