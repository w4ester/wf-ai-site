---
title: "Guardian Architecture: What the Research Actually Says"
tags: guardian, research, spr, headscale, netbird, privacy, families, ai, local-llms
date: 2026-01-12
---

# Guardian Architecture: What the Research Actually Says

*Academic research validates "support not surveillance." The technical research points to a dual-track solution.*

---

## The Striking Discovery

I spent the week diving into academic research on parental monitoring technology. The findings weren't just interesting—they were vindicating.

Studies from arXiv, PMC, and Cambridge consistently show that **surveillance-based parental control apps harm parent-teen relationships and foster paranoia**. The research explicitly calls for "collaborative technologies that move beyond surveillance."

That's exactly what Guardian is building.

---

## What the Research Says About Monitoring

```
┌───────────────────────────────┬─────────────────────────────┐
│      What Research Says       │     Guardian's Approach     │
├───────────────────────────────┼─────────────────────────────┤
│ Surveillance backfires        │ Transparency instead        │
├───────────────────────────────┼─────────────────────────────┤
│ Secret tracking damages trust │ Kids see same dashboard     │
├───────────────────────────────┼─────────────────────────────┤
│ Blocking everything fails     │ Contract-based access       │
├───────────────────────────────┼─────────────────────────────┤
│ Teens become more secretive   │ Collaborative communication │
└───────────────────────────────┴─────────────────────────────┘
```

The academic literature doesn't just suggest Guardian's philosophy might work—it explicitly validates that surveillance approaches cause harm.

---

## The Technical Research

The technical side is equally clear.

**TU Dresden** found that microsegmentation reduces attack surface by **65.85%**. This is the approach SPR (Secure Private Router) uses—giving each device its own WiFi password and network segment.

**WireGuard benchmarks** show **1-3ms latency overhead** vs 8-12ms for OpenVPN, with **600% better throughput**. This matters for solutions like Headscale and NetBird that use WireGuard for encrypted tunnels.

---

## Three Paths Forward

The research points to three viable technical approaches, each with different tradeoffs.

### Path 1: SPR Router

**What it does:** Per-device WiFi passwords + microsegmentation

**Research support:**
- TU Dresden: 65% attack surface reduction
- WPA3 research: "individualized data security"

**Tradeoffs:**
- ✅ Zero clients needed at home
- ✅ Solves MAC randomization completely (each device has unique password)
- ✅ Guardian becomes pure family support layer
- ⚠️ Only works at home

**Best for:** Home network identity, simplicity

**Hardware (~$150-230):**
```
┌──────────────────────────┬────────┐
│           Item           │ Price  │
├──────────────────────────┼────────┤
│ Raspberry Pi 4/5 8GB     │ $75-80 │
├──────────────────────────┼────────┤
│ Official Pi power supply │ $15    │
├──────────────────────────┼────────┤
│ 32-64GB USB SSD          │ $15-30 │
├──────────────────────────┼────────┤
│ ALFA WiFi adapter        │ $35-90 │
├──────────────────────────┼────────┤
│ Ethernet cable           │ $5     │
└──────────────────────────┴────────┘
```

---

### Path 2: Headscale

**What it does:** Self-hosted Tailscale coordination server

**Research support:**
- WireGuard performance benchmarks
- 34k GitHub stars, mature community
- Tailscale employee contributes officially

**Tradeoffs:**
- ✅ Works everywhere (school, friend's house, cellular)
- ✅ Privacy-focused (no external company sees metadata)
- ✅ Escape hatch to Tailscale if needed
- ⚠️ Requires VPN client on each device
- ⚠️ No built-in activity logging

**Best for:** Privacy-focused families who want devices connected everywhere

---

### Path 3: NetBird

**What it does:** Full zero-trust networking platform

**Research support:**
- WireGuard foundation
- 21k GitHub stars, rapid growth
- Built-in activity logging (Headscale lacks this)

**Tradeoffs:**
- ✅ Activity logging built-in
- ✅ MSP portal for multi-family potential
- ✅ Enterprise features if Guardian scales
- ⚠️ More complex than Headscale
- ⚠️ Younger project

**Best for:** Enterprise features, future scaling to help other families

---

## The Key Insight: Mesh Unlocks Portable Family AI

Here's what crystallized during research: **Without the mesh, family AI only works at home. The mesh transforms local AI into portable AI.**

```
Without Mesh:                    With Mesh:
─────────────                    ──────────
Home: AI ✓                       Home: AI ✓
School: Use ChatGPT ✗            School: Family AI via mesh ✓
Friend's: Use Gemini ✗           Friend's: Family AI via mesh ✓

Corporate values                 YOUR values
Corporate data collection        Data stays home
```

The mesh isn't just about knowing where your kid is—it's about **extending your family's values and support to wherever they are.**

---

## The Recommended Strategy: Tri-Track

The research points to three tracks working together:

```
COMPLETE ARCHITECTURE:

Track A: SPR for Home
├─ Solves MAC randomization completely
├─ No VPN client needed for home devices
└─ Guardian becomes pure family layer

Track B: Headscale/NetBird for Remote
├─ Cryptographic identity everywhere
├─ Support kids at school, friend's house
└─ Could overlay on SPR for complete coverage

Track C: Family AI Extension
├─ Local AI (Ollama) with family values
├─ Age-appropriate boundaries per child
├─ Accessible anywhere via mesh
└─ Data never leaves family control
```

**At home:** SPR gives each device a unique password. No more MAC randomization problems. Guardian doesn't need to track device identity—SPR handles it.

**Away from home:** Headscale or NetBird creates an encrypted tunnel back to the family network. Kid at school can still reach home. Contracts still apply.

**Family AI everywhere:** Local AI runs at home, accessible through the mesh. Kid at friend's house asks for homework help—gets YOUR family's AI, with YOUR values, not corporate AI optimized for engagement.

**Combined:** Complete coverage. Identity solved everywhere. No external company dependencies. Your values, portable.

---

## Track C: Family AI Extension

This is where it gets interesting.

### The Problem with Corporate AI

```
┌──────────────────────────┬────────────────────────┐
│       Corporate AI       │      Guardian AI       │
├──────────────────────────┼────────────────────────┤
│ Optimize for engagement  │ Optimize for wellbeing │
├──────────────────────────┼────────────────────────┤
│ Data is the product      │ Data stays home        │
├──────────────────────────┼────────────────────────┤
│ Same AI for everyone     │ Curated for YOUR child │
├──────────────────────────┼────────────────────────┤
│ Aligned with advertisers │ Aligned with parents   │
└──────────────────────────┴────────────────────────┘
```

When your kid uses ChatGPT at school, they're using AI optimized for OpenAI's goals. When they use Gemini at a friend's house, Google's goals. The AI doesn't know your family values, your kid's age, your boundaries.

### The Architecture

```
HOME SERVER                      KID'S PHONE (anywhere)
───────────                      ────────────────────
Local AI (Ollama)                "Hey Guardian AI,
├─ Family values embedded         help me with homework"
├─ Age-appropriate                      │
├─ Knows each child's context           │
└─ Transparency log              MESH TUNNEL (encrypted)
         ▲                              │
         └──────────────────────────────┘
```

### Key Features

1. **Age-Appropriate Boundaries** — 10-year-old gets different boundaries than 15-year-old
2. **Sensitivity Detection** — Flags concerning topics, notifies parents
3. **Transparency** — Kid knows parents can see conversations (not secret surveillance)
4. **Family Knowledge** — AI knows pet names, traditions, school info
5. **Values Configuration** — Parents set honesty, kindness, growth mindset, etc.

---

## Implementation Timeline

```
┌───────┬──────────────────────┬─────────────────────────┐
│ Phase │        Focus         │          Goal           │
├───────┼──────────────────────┼─────────────────────────┤
│ 1-2   │ SPR Foundation       │ Home network identity   │
├───────┼──────────────────────┼─────────────────────────┤
│ 3-4   │ Mesh Overlay         │ Remote identity         │
├───────┼──────────────────────┼─────────────────────────┤
│ 5-6   │ Unified Identity     │ Single view across both │
├───────┼──────────────────────┼─────────────────────────┤
│ 7-8   │ Contract Enforcement │ Policies that work      │
├───────┼──────────────────────┼─────────────────────────┤
│ 9-10  │ Family AI Foundation │ Local AI running        │
├───────┼──────────────────────┼─────────────────────────┤
│ 11-12 │ Portable AI          │ AI via mesh anywhere    │
├───────┼──────────────────────┼─────────────────────────┤
│ 13-14 │ AI Curation          │ Family values embedded  │
├───────┼──────────────────────┼─────────────────────────┤
│ 15-16 │ Polish & Testing     │ Real family ready       │
└───────┴──────────────────────┴─────────────────────────┘
```

**The full architecture:** SPR + Mesh + Family AI = Complete support for kids, on your terms, with your values, everywhere they go.

---

## Why This Matters

The current parental control market is built on fear.

Companies profit when caregivers feel anxious. They build surveillance tools because surveillance creates engagement—every "alert" drives a parent back to the app. The business model requires maintaining fear.

But the research is clear: this approach backfires. Kids become more secretive. Trust erodes. The technology becomes adversarial.

Guardian takes a different path:

- **Transparency over surveillance** — Kids see the same dashboard
- **Contracts over control** — Agreements made together, with mutual commitments
- **Support over monitoring** — Helping kids develop self-regulation, not dependence

The academic research validates this philosophy. The technical research shows how to build it.

---

## Hardware Shopping List

If you want to start experimenting:

**Budget SPR Setup (~$150)**
- Raspberry Pi 4 8GB: $75
- Official power supply: $15
- 32GB microSD: $15
- ALFA AWUS036ACM (WiFi 5): $35
- Ethernet cable: $5

**Performance Setup (~$230)**
- Raspberry Pi 5 8GB: $80
- Official Pi 5 power supply: $15
- 64GB USB SSD: $25
- Netgear A8000 (WiFi 6E): $90
- TP-Link UE300 (extra LAN): $15
- Ethernet cable: $5

**Network topology:**
```
INTERNET ──▶ [Pi Ethernet] ──▶ SPR ──▶ [USB WiFi] ──▶ YOUR DEVICES
              (WAN/uplink)              (LAN/AP mode)
```

---

## What's Next

I'm building both tracks in parallel:

1. **SPR evaluation** — Setting up per-device passwords, integrating with Guardian's contract system
2. **Headscale deployment** — Self-hosted coordination, WireGuard tunnels for remote access
3. **Integration layer** — Guardian as the family support layer on top of either/both

The goal: families can choose their comfort level. Want simple home-only? SPR. Want everywhere coverage? Add Headscale. Want to avoid all external dependencies? Both, self-hosted.

The architecture should encode our values. Support, not surveillance. Family control, not corporate extraction.

---

*Let's GrOw!*
