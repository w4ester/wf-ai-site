#!/usr/bin/env python3
"""
WF-AI Site Manager
==================
A CLI tool for managing posts on the WF-AI Site static site.

Features:
- Markdown support for rich content
- Automatic RSS feed generation
- Tag support for categorization
- Staggered animation delays on new posts

Usage:
    python manager.py post "Title" "Content" --tags tag1,tag2
    python manager.py rss                           # Regenerate RSS feed
    python manager.py list                          # List recent posts
    
Examples:
    python manager.py post "My First AI Experiment" "Built a **RAG system** today!" --tags ai,rag
    python manager.py post "Quick Note" "Just a thought about local LLMs."
"""

import sys
import os
import re
import datetime
import argparse
from html import escape
from pathlib import Path

# Configuration
SITE_URL = "https://w4ester.github.io/wf-ai-site"
SITE_TITLE = "WF-AI Site"
SITE_DESCRIPTION = "A digital garden for AI experiments, projects, and ideas from the Baltimore AI Producers Lab."
AUTHOR = "Will Capellaro"

# Try to import markdown, fallback to plain text if not installed
try:
    import markdown
    from markdown.extensions.fenced_code import FencedCodeExtension
    from markdown.extensions.tables import TableExtension
    HAS_MARKDOWN = True
except ImportError:
    HAS_MARKDOWN = False

# HTML Template for posts
POST_TEMPLATE = """
<article class="group rounded-lg border border-border bg-card text-card-foreground shadow-sm transition-all hover:shadow-lg hover:border-accent/50 animate-slide-up" style="animation-delay: 0.1s; opacity: 0;" data-date="{iso_date}">
    <div class="flex flex-col space-y-1.5 p-6">
        <div class="flex justify-between items-start gap-4">
            <h3 class="font-semibold leading-none tracking-tight text-lg font-mono group-hover:text-accent transition-colors">{title}</h3>
            <span class="text-xs text-muted-foreground font-mono whitespace-nowrap">{date_display}</span>
        </div>
    </div>
    <div class="p-6 pt-0 text-muted-foreground prose">
        {content}
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


def convert_markdown(raw_content: str) -> str:
    """Convert markdown to HTML if available."""
    if HAS_MARKDOWN:
        md = markdown.Markdown(extensions=[
            FencedCodeExtension(),
            TableExtension(),
            'nl2br'  # Convert newlines to <br>
        ])
        return md.convert(raw_content)
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
