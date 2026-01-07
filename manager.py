#!/usr/bin/env python3
"""
WF-AI Site Manager
==================
A CLI tool for managing posts on the WF-AI Site static site.

Features:
- Markdown support for rich content
- Automatic RSS feed generation
- Tag support for categorization
- BEADS (bd) integration for task tracking

Usage:
    python manager.py post "Title" "Content" --tags tag1,tag2
    python manager.py rss                           # Regenerate RSS feed
    python manager.py list                          # List recent posts

    # BEADS workflow (recommended):
    python manager.py idea "Topic to write about"   # Create post task in bd
    python manager.py ready                         # See what's ready to write
    python manager.py publish                       # Interactive: pick task, write, publish

Examples:
    python manager.py idea "Local LLMs on Mac" -p 1
    python manager.py publish
    python manager.py post "Quick Note" "Just a thought." --tags ai
"""

import sys
import os
import re
import json
import datetime
import argparse
import subprocess
from html import escape
from pathlib import Path

# Configuration
SITE_URL = "https://w4ester.github.io/wf-ai-site"
SITE_TITLE = "WF-AI Site"
SITE_DESCRIPTION = "A digital garden for AI experiments, projects, and ideas from the Baltimore AI Producers Lab."
AUTHOR = "w4ester"

# Try to import markdown, fallback to plain text if not installed
try:
    import markdown
    from markdown.extensions.fenced_code import FencedCodeExtension
    from markdown.extensions.tables import TableExtension
    HAS_MARKDOWN = True
except ImportError:
    HAS_MARKDOWN = False

# HTML Template for posts (with collapsible content)
POST_TEMPLATE = """
<article class="group rounded-lg border border-border bg-card text-card-foreground shadow-sm transition-all hover:shadow-lg hover:border-accent/50 animate-slide-up" style="animation-delay: 0.1s; opacity: 0;" data-date="{iso_date}">
    <div class="flex flex-col space-y-1.5 p-6">
        <div class="flex justify-between items-start gap-4">
            <h3 class="font-semibold leading-none tracking-tight text-lg font-mono group-hover:text-accent transition-colors">{title}</h3>
            <span class="text-xs text-muted-foreground font-mono whitespace-nowrap">{date_display}</span>
        </div>
    </div>
    <div class="p-6 pt-0 text-muted-foreground prose post-content">
        {content}
        <div class="post-fade"></div>
    </div>
    <div class="px-6 pb-2">
        <button class="read-more-btn" onclick="togglePost(this)">
            <span>Continue reading...</span>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" /></svg>
        </button>
    </div>
    {tags_html}
</article>
"""

TAGS_TEMPLATE = """<div class="px-6 pb-4 flex gap-2 flex-wrap">
{tags}
</div>"""

TAG_TEMPLATE = '<span class="text-xs font-mono px-2 py-1 rounded bg-muted text-muted-foreground">#{tag}</span>'


def print_banner():
    """Print a nice CLI banner."""
    print("\n╔═══════════════════════════════════════╗")
    print("║         WF-AI Site Manager            ║")
    print("╚═══════════════════════════════════════╝\n")


# =============================================================================
# BEADS (bd) Integration
# =============================================================================

def run_bd(args: list[str], json_output: bool = True) -> dict | str | None:
    """Run a bd command and return the result."""
    cmd = ['bd'] + args
    if json_output and '--json' not in args:
        cmd.append('--json')

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            if result.stderr:
                print(f"⚠️  bd error: {result.stderr.strip()}")
            return None

        if json_output:
            try:
                return json.loads(result.stdout)
            except json.JSONDecodeError:
                return result.stdout.strip()
        return result.stdout.strip()
    except FileNotFoundError:
        print("⚠️  bd not found. Install with: brew install steveyegge/beads/bd")
        return None


def bd_ready() -> list[dict]:
    """Get list of ready (unblocked) tasks from bd."""
    result = run_bd(['ready'])
    if result and isinstance(result, list):
        return result
    return []


def bd_create_post_task(title: str, priority: int = 2) -> str | None:
    """Create a bd task for a post idea. Returns task ID."""
    result = run_bd(['create', f'Write post: {title}', '-t', 'task', '-p', str(priority)])
    if result and isinstance(result, dict):
        return result.get('id')
    return None


def bd_close_task(task_id: str, reason: str = "Published") -> bool:
    """Close a bd task."""
    result = run_bd(['close', task_id, '--reason', reason])
    return result is not None


def bd_list_ready():
    """Display ready tasks for posting."""
    tasks = bd_ready()

    if not tasks:
        print("📭 No ready tasks. Create one with:")
        print("   python manager.py idea 'Post title'")
        print("   or: bd create 'Write post: Topic' -t task -p 2")
        return []

    print(f"📋 Ready to write ({len(tasks)} tasks):\n")
    for i, task in enumerate(tasks, 1):
        task_id = task.get('id', 'unknown')
        title = task.get('title', 'Untitled')
        priority = task.get('priority', 2)
        print(f"   {i}. [{task_id}] (P{priority}) {title}")

    return tasks


def bd_publish_flow():
    """Interactive flow: pick a ready task, write post, close task."""
    tasks = bd_ready()

    if not tasks:
        print("📭 No ready tasks to publish.")
        print("   Create post ideas with: python manager.py idea 'Topic'")
        return False

    print(f"\n📋 Ready tasks ({len(tasks)}):\n")
    for i, task in enumerate(tasks, 1):
        task_id = task.get('id', 'unknown')
        title = task.get('title', 'Untitled')
        print(f"   {i}. [{task_id}] {title}")

    print("\n   0. Cancel")

    try:
        choice = input("\nSelect task number: ").strip()
        if choice == '0' or not choice:
            print("Cancelled.")
            return False

        idx = int(choice) - 1
        if idx < 0 or idx >= len(tasks):
            print("Invalid selection.")
            return False

        task = tasks[idx]
        task_id = task.get('id')
        task_title = task.get('title', 'Untitled')

        # Remove "Write post: " prefix if present
        post_title = task_title
        if post_title.lower().startswith('write post:'):
            post_title = post_title[11:].strip()

        print(f"\n✏️  Writing post: {post_title}")
        print("   Enter content (Markdown supported). End with an empty line:\n")

        lines = []
        while True:
            line = input()
            if line == '':
                break
            lines.append(line)

        content = '\n'.join(lines)

        if not content.strip():
            print("❌ No content provided. Cancelled.")
            return False

        # Get tags
        tags_input = input("\nTags (comma-separated, or Enter to skip): ").strip()
        tags = [t.strip() for t in tags_input.split(',') if t.strip()] if tags_input else []

        # Create the post
        success = create_post(post_title, content, tags)

        if success:
            # Close the bd task
            if bd_close_task(task_id, "Published to site"):
                print(f"   ✅ Closed task {task_id}")

            # Regenerate RSS
            generate_rss()

            print("\n💡 Ready to deploy:")
            print("   git add . && git commit -m 'New post' && git push")

        return success

    except (ValueError, KeyboardInterrupt):
        print("\nCancelled.")
        return False


def style_images(html: str) -> str:
    """Add responsive styling to images in HTML."""
    # Match <img> tags and add styling classes
    img_pattern = re.compile(r'<img\s+([^>]*)>', re.IGNORECASE)

    def add_classes(match):
        attrs = match.group(1)
        # Don't add classes if already has class attribute
        if 'class=' in attrs:
            return match.group(0)
        # Add responsive, rounded styling
        return f'<img class="w-full max-w-2xl rounded-lg shadow-md my-4 mx-auto" {attrs}>'

    return img_pattern.sub(add_classes, html)


def convert_markdown(raw_content: str) -> str:
    """Convert markdown to HTML if available."""
    if HAS_MARKDOWN:
        md = markdown.Markdown(extensions=[
            FencedCodeExtension(),
            TableExtension(),
            'nl2br'  # Convert newlines to <br>
        ])
        html = md.convert(raw_content)
        # Add styling to images
        html = style_images(html)
        return html
    else:
        # Basic fallback: escape HTML and wrap in paragraph
        paragraphs = raw_content.split('\n\n')
        return ''.join(f'<p>{escape(p)}</p>' for p in paragraphs if p.strip())


def generate_date_display() -> tuple[str, str]:
    """Generate both display date and ISO date."""
    now = datetime.datetime.now()
    # Display format: "2024-12-22::14:30"
    display = now.strftime("%Y-%m-%d::%H:%M")
    # ISO format for RSS and sorting
    iso = now.isoformat()
    return display, iso


def create_tags_html(tags: list[str]) -> str:
    """Generate HTML for tags."""
    if not tags:
        return ""
    tags_inner = '\n'.join(TAG_TEMPLATE.format(tag=tag.strip()) for tag in tags if tag.strip())
    return TAGS_TEMPLATE.format(tags=tags_inner)


def create_post(title: str, raw_content: str, tags: list[str] = None):
    """Create a new post and inject it into index.html."""
    file_path = Path("index.html")
    
    if not file_path.exists():
        print("❌ Error: index.html not found. Run this from your wf-ai-site directory.")
        return False

    # Convert content
    html_content = convert_markdown(raw_content)
    date_display, iso_date = generate_date_display()
    tags_html = create_tags_html(tags or [])
    
    # Build the new entry
    new_entry = POST_TEMPLATE.format(
        title=escape(title),
        date_display=date_display,
        iso_date=iso_date,
        content=html_content,
        tags_html=tags_html
    )
    
    # Read existing HTML
    html = file_path.read_text(encoding='utf-8')
    
    # Find injection point
    marker = '<main id="content-feed" class="space-y-6">'
    
    if marker not in html:
        print("❌ Error: Could not find injection marker in index.html")
        print("   Looking for: " + marker)
        return False
    
    # Inject new post after the opening <main> tag
    updated_html = html.replace(marker, marker + "\n" + new_entry)
    
    # Write back
    file_path.write_text(updated_html, encoding='utf-8')
    
    print(f"✅ Post added: '{title}'")
    print(f"   📅 {date_display}")
    if tags:
        print(f"   🏷️  {', '.join(tags)}")
    
    return True


def extract_posts_from_html() -> list[dict]:
    """Extract all posts from index.html for RSS generation."""
    file_path = Path("index.html")
    if not file_path.exists():
        return []
    
    html = file_path.read_text(encoding='utf-8')
    posts = []
    
    # Simple regex to extract articles
    article_pattern = re.compile(
        r'<article[^>]*data-date="([^"]*)"[^>]*>.*?'
        r'<h3[^>]*>([^<]*)</h3>.*?'
        r'<div class="p-6 pt-0[^"]*prose">\s*(.*?)\s*</div>',
        re.DOTALL
    )
    
    for match in article_pattern.finditer(html):
        iso_date, title, content = match.groups()
        posts.append({
            'date': iso_date,
            'title': title.strip(),
            'content': content.strip()
        })
    
    return posts


def generate_rss():
    """Generate RSS feed from existing posts."""
    posts = extract_posts_from_html()
    
    if not posts:
        print("⚠️  No posts found with data-date attribute.")
        print("   Only posts created with this version of manager.py will appear in RSS.")
        return False
    
    # Build RSS XML
    now = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")
    
    items = []
    for post in posts[:20]:  # Limit to 20 most recent
        try:
            pub_date = datetime.datetime.fromisoformat(post['date']).strftime("%a, %d %b %Y %H:%M:%S +0000")
        except:
            pub_date = now
        
        item = f"""    <item>
      <title>{escape(post['title'])}</title>
      <link>{SITE_URL}</link>
      <description><![CDATA[{post['content']}]]></description>
      <pubDate>{pub_date}</pubDate>
      <guid>{SITE_URL}#{escape(post['title'].lower().replace(' ', '-'))}</guid>
    </item>"""
        items.append(item)
    
    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{SITE_TITLE}</title>
    <link>{SITE_URL}</link>
    <description>{SITE_DESCRIPTION}</description>
    <language>en-us</language>
    <lastBuildDate>{now}</lastBuildDate>
    <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>
    <author>{AUTHOR}</author>
{chr(10).join(items)}
  </channel>
</rss>"""
    
    Path("feed.xml").write_text(rss, encoding='utf-8')
    print(f"✅ RSS feed generated: feed.xml")
    print(f"   📰 {len(posts)} posts included")
    return True


def list_posts():
    """List recent posts from index.html."""
    posts = extract_posts_from_html()

    if not posts:
        print("📭 No posts found.")
        return

    print(f"📋 Found {len(posts)} post(s):\n")
    for i, post in enumerate(posts[:10], 1):
        title = post['title'][:50] + "..." if len(post['title']) > 50 else post['title']
        date = post['date'][:10] if post['date'] else "unknown"
        print(f"   {i}. [{date}] {title}")


# =============================================================================
# Drafts Workflow (New!)
# =============================================================================

def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return {}, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content

    frontmatter_text = parts[1].strip()
    body = parts[2].strip()

    # Simple YAML parsing (title, tags)
    frontmatter = {}
    for line in frontmatter_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"\'')
            if key == 'tags':
                frontmatter[key] = [t.strip() for t in value.split(',')]
            else:
                frontmatter[key] = value

    return frontmatter, body


def list_drafts():
    """List all drafts in drafts/ folder."""
    drafts_dir = Path("drafts")
    if not drafts_dir.exists():
        print("📭 No drafts folder. Create one with: mkdir drafts")
        return []

    drafts = list(drafts_dir.glob("*.md"))

    if not drafts:
        print("📭 No drafts found in drafts/")
        print("   AI can save drafts here, then you publish with:")
        print("   python manager.py publish-draft <name>")
        return []

    print(f"📝 Drafts ({len(drafts)}):\n")
    for i, draft in enumerate(sorted(drafts), 1):
        content = draft.read_text(encoding='utf-8')
        frontmatter, _ = parse_frontmatter(content)
        title = frontmatter.get('title', draft.stem)
        print(f"   {i}. {draft.name}")
        print(f"      Title: {title}")
        if frontmatter.get('tags'):
            print(f"      Tags: {', '.join(frontmatter['tags'])}")
        print()

    return drafts


def publish_draft(draft_name: str):
    """Publish a draft from drafts/ folder."""
    drafts_dir = Path("drafts")
    posts_dir = Path("posts")

    # Find the draft
    if not draft_name.endswith('.md'):
        draft_name += '.md'

    draft_path = drafts_dir / draft_name

    if not draft_path.exists():
        print(f"❌ Draft not found: {draft_path}")
        print("\n   Available drafts:")
        list_drafts()
        return False

    # Parse the draft
    content = draft_path.read_text(encoding='utf-8')
    frontmatter, body = parse_frontmatter(content)

    title = frontmatter.get('title', draft_path.stem.replace('-', ' ').title())
    tags = frontmatter.get('tags', [])

    print(f"📄 Publishing: {title}")
    print(f"   Tags: {', '.join(tags) if tags else 'none'}")

    # Create the post (using existing function)
    success = create_post(title, body, tags)

    if success:
        # Move draft to posts/ for archive
        posts_dir.mkdir(exist_ok=True)
        date_prefix = datetime.datetime.now().strftime("%Y-%m-%d")
        archive_name = f"{date_prefix}-{draft_path.stem}.md"
        archive_path = posts_dir / archive_name
        draft_path.rename(archive_path)
        print(f"   📁 Draft archived to: posts/{archive_name}")

        # Generate RSS
        generate_rss()

        print("\n💡 Ready to deploy:")
        print("   git add . && git commit -m 'New post' && git push")

    return success


def main():
    parser = argparse.ArgumentParser(
        description="WF-AI Site Manager - Manage your static AI blog",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python manager.py post "My Title" "My **markdown** content" --tags ai,local
  python manager.py rss
  python manager.py list
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Post command
    post_parser = subparsers.add_parser('post', help='Create a new post')
    post_parser.add_argument('title', help='Post title')
    post_parser.add_argument('content', help='Post content (Markdown supported)')
    post_parser.add_argument('--tags', '-t', help='Comma-separated tags', default='')
    
    # RSS command
    subparsers.add_parser('rss', help='Regenerate RSS feed')

    # List command
    subparsers.add_parser('list', help='List recent posts')

    # BEADS integration commands
    idea_parser = subparsers.add_parser('idea', help='Create a post idea (bd task)')
    idea_parser.add_argument('title', help='Post idea/topic')
    idea_parser.add_argument('--priority', '-p', type=int, default=2, help='Priority 0-4 (default: 2)')

    subparsers.add_parser('ready', help='List ready post ideas from bd')
    subparsers.add_parser('publish', help='Interactive: pick task, write post, close task')

    # Drafts workflow commands (NEW!)
    subparsers.add_parser('drafts', help='List drafts in drafts/ folder')
    publish_draft_parser = subparsers.add_parser('publish-draft', help='Publish a draft from drafts/')
    publish_draft_parser.add_argument('name', help='Draft filename (without .md)')
    
    # Parse args
    args = parser.parse_args()
    
    print_banner()
    
    if not HAS_MARKDOWN:
        print("⚠️  Warning: 'markdown' library not found. Posts will be plain text.")
        print("   Install with: pip install markdown\n")
    
    if args.command == 'post':
        tags = [t.strip() for t in args.tags.split(',') if t.strip()] if args.tags else []
        success = create_post(args.title, args.content, tags)
        if success:
            print("\n💡 Tip: Run 'python manager.py rss' to update your RSS feed")
            print("   Then: git add . && git commit -m 'new post' && git push")
    
    elif args.command == 'rss':
        generate_rss()
    
    elif args.command == 'list':
        list_posts()

    elif args.command == 'idea':
        task_id = bd_create_post_task(args.title, args.priority)
        if task_id:
            print(f"✅ Post idea created: {task_id}")
            print(f"   '{args.title}' (priority {args.priority})")
            print("\n💡 When ready to write: python manager.py publish")

    elif args.command == 'ready':
        bd_list_ready()

    elif args.command == 'publish':
        bd_publish_flow()

    elif args.command == 'drafts':
        list_drafts()

    elif args.command == 'publish-draft':
        publish_draft(args.name)

    else:
        # Legacy mode: support old "python manager.py 'Title' 'Content'" syntax
        if len(sys.argv) >= 3:
            title = sys.argv[1]
            content = sys.argv[2]
            tags = sys.argv[3].split(',') if len(sys.argv) > 3 else []
            success = create_post(title, content, tags)
            if success:
                print("\n💡 Tip: Run 'python manager.py rss' to update your RSS feed")
        else:
            parser.print_help()
            print("\n" + "="*50)
            print("Quick start:")
            print('  python manager.py post "Hello World" "My first post!"')


if __name__ == "__main__":
    main()
