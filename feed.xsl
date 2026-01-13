<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:atom="http://www.w3.org/2005/Atom">
  <xsl:output method="html" encoding="UTF-8" indent="yes"/>

  <xsl:template match="/">
    <html lang="en">
      <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title><xsl:value-of select="/rss/channel/title"/> - RSS Feed</title>
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&amp;family=Space+Grotesk:wght@400;500;600&amp;display=swap" rel="stylesheet"/>
        <style>
          :root {
            --background: #fafaf9;
            --foreground: #1c1917;
            --card: #fafaf9;
            --card-foreground: #1c1917;
            --muted: #e7e5e4;
            --muted-foreground: #78716c;
            --accent: #16a34a;
            --border: #d6d3d1;
          }

          @media (prefers-color-scheme: dark) {
            :root {
              --background: #18181b;
              --foreground: #fafaf9;
              --card: #1f1f23;
              --card-foreground: #fafaf9;
              --muted: #27272a;
              --muted-foreground: #a1a1aa;
              --accent: #4ade80;
              --border: #3f3f46;
            }
          }

          * { box-sizing: border-box; margin: 0; padding: 0; }

          body {
            font-family: 'Space Grotesk', sans-serif;
            background: var(--background);
            color: var(--foreground);
            line-height: 1.6;
            min-height: 100vh;
          }

          .container {
            max-width: 42rem;
            margin: 0 auto;
            padding: 3rem 1.5rem;
          }

          .header {
            margin-bottom: 2rem;
            padding-bottom: 1.5rem;
            border-bottom: 1px solid var(--border);
          }

          .rss-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: var(--accent);
            color: var(--background);
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 600;
            font-family: 'JetBrains Mono', monospace;
            margin-bottom: 1rem;
          }

          .rss-badge svg {
            width: 1rem;
            height: 1rem;
          }

          h1 {
            font-family: 'JetBrains Mono', monospace;
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
          }

          .description {
            color: var(--muted-foreground);
            font-size: 0.875rem;
          }

          .subscribe-hint {
            background: var(--muted);
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 2rem;
            font-size: 0.875rem;
            color: var(--muted-foreground);
          }

          .subscribe-hint code {
            background: var(--card);
            padding: 0.125rem 0.375rem;
            border-radius: 0.25rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8125rem;
            word-break: break-all;
          }

          .items { display: flex; flex-direction: column; gap: 1.5rem; }

          .item {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 0.5rem;
            padding: 1.5rem;
            transition: border-color 0.2s;
          }

          .item:hover {
            border-color: var(--accent);
          }

          .item-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 1rem;
            margin-bottom: 0.75rem;
          }

          .item-title {
            font-family: 'JetBrains Mono', monospace;
            font-size: 1.125rem;
            font-weight: 500;
            color: var(--foreground);
          }

          .item-title:hover {
            color: var(--accent);
          }

          .item-date {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.75rem;
            color: var(--muted-foreground);
            white-space: nowrap;
          }

          .item-content {
            color: var(--muted-foreground);
            font-size: 0.875rem;
          }

          .item-content h1, .item-content h2, .item-content h3 {
            font-family: 'JetBrains Mono', monospace;
            color: var(--foreground);
            margin-top: 1.25rem;
            margin-bottom: 0.5rem;
          }

          .item-content h1 { font-size: 1.25rem; }
          .item-content h2 { font-size: 1.125rem; }
          .item-content h3 { font-size: 1rem; }

          .item-content p { margin-bottom: 0.75rem; }

          .item-content a {
            color: var(--accent);
            text-decoration: underline;
            text-underline-offset: 2px;
          }

          .item-content code {
            background: var(--muted);
            padding: 0.125rem 0.375rem;
            border-radius: 0.25rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8125rem;
          }

          .item-content pre {
            background: var(--muted);
            padding: 1rem;
            border-radius: 0.5rem;
            overflow-x: auto;
            margin: 1rem 0;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8125rem;
          }

          .item-content pre code {
            background: none;
            padding: 0;
          }

          .item-content ul, .item-content ol {
            margin-left: 1.5rem;
            margin-bottom: 0.75rem;
          }

          .item-content table {
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
            font-size: 0.8125rem;
          }

          .item-content th, .item-content td {
            padding: 0.5rem;
            border: 1px solid var(--border);
            text-align: left;
          }

          .item-content th {
            background: var(--muted);
            font-weight: 600;
          }

          .item-content blockquote {
            border-left: 3px solid var(--accent);
            padding-left: 1rem;
            margin: 1rem 0;
            font-style: italic;
          }

          .item-content hr {
            border: none;
            border-top: 1px solid var(--border);
            margin: 1.5rem 0;
          }

          .back-link {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--accent);
            text-decoration: none;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.875rem;
            margin-top: 2rem;
          }

          .back-link:hover {
            text-decoration: underline;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <header class="header">
            <div class="rss-badge">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                <path d="M3.75 3a.75.75 0 00-.75.75v.5c0 .414.336.75.75.75H4c6.075 0 11 4.925 11 11v.25c0 .414.336.75.75.75h.5a.75.75 0 00.75-.75V16C17 8.82 11.18 3 4 3h-.25z"/>
                <path d="M3 8.75A.75.75 0 013.75 8H4a8 8 0 018 8v.25a.75.75 0 01-.75.75h-.5a.75.75 0 01-.75-.75V16a6 6 0 00-6-6h-.25A.75.75 0 013 9.25v-.5z"/>
                <circle cx="5" cy="19" r="2"/>
              </svg>
              RSS Feed
            </div>
            <h1><xsl:value-of select="/rss/channel/title"/></h1>
            <p class="description"><xsl:value-of select="/rss/channel/description"/></p>
          </header>

          <div class="subscribe-hint">
            Subscribe to this feed by copying this URL into your RSS reader:
            <br/>
            <code><xsl:value-of select="/rss/channel/atom:link/@href"/></code>
          </div>

          <div class="items">
            <xsl:for-each select="/rss/channel/item">
              <article class="item">
                <div class="item-header">
                  <a class="item-title" href="{link}"><xsl:value-of select="title"/></a>
                  <span class="item-date"><xsl:value-of select="pubDate"/></span>
                </div>
                <div class="item-content">
                  <xsl:value-of select="description" disable-output-escaping="yes"/>
                </div>
              </article>
            </xsl:for-each>
          </div>

          <a class="back-link" href="https://w4ester.github.io/wf-ai-site">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M19 12H5M12 19l-7-7 7-7"/>
            </svg>
            Back to site
          </a>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
