---
title: "Headscale: Why Your Family's Data Shouldn't Depend on Anyone's Promises"
tags: guardian, headscale, tailscale, self-hosted, privacy, mesh-network
date: 2026-01-11
---

# Headscale: Why Your Family's Data Shouldn't Depend on Anyone's Promises

*Even "good" companies are only as trustworthy as their next funding round.*

---

## What Does Tailscale Actually See?

In [the previous post](/posts/2026-01-11-guardian-protocol-tracking-paradox.html), I proposed using Tailscale to extend family support everywhere. But there's a problem with that approach.

Even though Tailscale's data plane is end-to-end encrypted (WireGuard), their control plane sees plenty:

```
WHAT TAILSCALE'S SERVERS KNOW:
├── Which devices are in your "tailnet"
├── When each device comes online/offline
├── IP addresses of each device
├── Authentication events (who logged in when)
├── Connection patterns (which nodes talk to which)
└── Metadata about your family's digital life patterns
```

They don't see the *content* of your traffic, but they see the *shape* of your family's connectivity. That's still data. That's still your children's patterns.

**Today's Tailscale:**
- VC-funded (Accel, others)
- Good privacy stance currently
- Open source client, closed source control plane

**Tomorrow's Tailscale:**
- Could be acquired (by who? with what incentives?)
- Could need more revenue (monetize that metadata?)
- Could change terms of service
- Could cease to exist

A company's values are only as stable as their business model.

---

## The Alternative: Headscale

There's an open-source project called [Headscale](https://github.com/juanfont/headscale) — a self-hosted implementation of Tailscale's coordination server.

```
WITH TAILSCALE (current approach):
┌─────────────┐     ┌─────────────────────┐     ┌─────────────┐
│ Kid's Phone │────▶│ Tailscale's Servers │────▶│ Home        │
│ (anywhere)  │     │ (their computers)   │     │ (Guardian)  │
└─────────────┘     │                     │     └─────────────┘
                    │ THEY SEE:           │
                    │ - Your family map   │
                    │ - Who's online when │
                    │ - Connection graph  │
                    └─────────────────────┘

WITH HEADSCALE (self-hosted):
┌─────────────┐     ┌─────────────────────┐     ┌─────────────┐
│ Kid's Phone │────▶│ YOUR Headscale      │────▶│ Home        │
│ (anywhere)  │     │ (your computer)     │     │ (Guardian)  │
└─────────────┘     │                     │     └─────────────┘
                    │ YOU SEE:            │
                    │ - Your family map   │
                    │ - Who's online when │
                    │ - Connection graph  │
                    │                     │
                    │ NO COMPANY SEES     │
                    │ ANYTHING            │
                    └─────────────────────┘
```

**Headscale gives you:**
- Same WireGuard encryption (military-grade)
- Same mesh networking (devices find each other)
- Same "works everywhere" (school, friend's house, cellular)
- Zero external company involvement
- All metadata stays in YOUR control

---

## Trust Layers

Data about our children should stay as close to home as possible.

Let's map the trust boundaries:

```
TRUST LAYERS (from most trusted to least):

1. HOME (full trust)
   └── Guardian server, family devices on local network

2. YOUR INFRASTRUCTURE (high trust)
   └── Headscale on a $5/month VPS you control
   └── Or Headscale on a Raspberry Pi at home with dynamic DNS

3. KNOWN OPEN SOURCE (medium trust)
   └── WireGuard protocol (audited, proven)
   └── Headscale code (open source, verifiable)

4. COMPANIES WITH ALIGNED INCENTIVES (lower trust)
   └── Tailscale (currently good, but VC-funded)
   └── Could change

5. COMPANIES WITH MISALIGNED INCENTIVES (no trust)
   └── Social media platforms
   └── Ad-tech companies
   └── "Free" services where you're the product
```

**Guardian should minimize dependencies on layers 4 and 5.**

---

## The Path to True Independence

Removing ISP dependency isn't crazy — it's the logical end state of "data stays home."

```
TODAY (1 external dependency: ISP)
┌─────────┐     ┌─────────┐     ┌─────────┐
│  Home   │────▶│   ISP   │────▶│ Internet│
└─────────┘     └─────────┘     └─────────┘
                    ↑
              They see all
              traffic metadata

NEAR FUTURE (ISP sees less, you control identity)
┌─────────┐     ┌─────────┐     ┌─────────────────┐
│  Home   │────▶│   ISP   │────▶│ Your VPS        │
│Headscale│     │(tunnel) │     │ (relay only)    │
└─────────┘     └─────────┘     └─────────────────┘
                    ↑               ↑
              Encrypted          You control
              tunnel             the relay

FAR FUTURE (mesh network, no ISP)
┌─────────┐     ┌───────────────────┐     ┌─────────┐
│  Home   │────▶│ Community Mesh    │────▶│ Kid's   │
│         │     │ (neighbor nodes)  │     │ Device  │
└─────────┘     └───────────────────┘     └─────────┘
                         ↑
                   No company
                   No ISP
                   Just neighbors
```

**Technologies for the far future:**
- **LoRa** — Long-range, low-power radio mesh
- **Meshtastic** — Open source mesh networking
- **Community WiFi mesh** — Neighbor-to-neighbor
- **IPFS/libp2p** — Decentralized data

But you don't have to wait. **Headscale now prepares the architecture for mesh later.**

---

## Guardian with Headscale: The Architecture

```
GUARDIAN ARCHITECTURE (no external company dependencies)

┌─────────────────────────────────────────────────────────────────┐
│                         YOUR HOME                                │
│                                                                  │
│  ┌──────────────────┐     ┌──────────────────┐                  │
│  │  Guardian Server │     │   Headscale      │                  │
│  │  - Contracts     │────▶│   - Identity     │                  │
│  │  - Dashboard     │     │   - Mesh coord   │                  │
│  │  - AI Coach      │     │   - ACLs         │                  │
│  └──────────────────┘     └────────┬─────────┘                  │
│                                    │                             │
│         Raspberry Pi or old laptop │                             │
│         (runs both services)       │                             │
└────────────────────────────────────┼─────────────────────────────┘
                                     │
                    ┌────────────────┼────────────────┐
                    │                │                │
              ┌─────▼─────┐   ┌──────▼─────┐   ┌─────▼─────┐
              │ Kid Phone │   │ Kid Tablet │   │ Kid Laptop│
              │ (school)  │   │ (friend's) │   │ (library) │
              └───────────┘   └────────────┘   └───────────┘

              All connect home via WireGuard
              All identity managed by YOUR Headscale
              ZERO external companies involved
```

**What this gives you:**
- Kids always connected to home, wherever they are
- Contracts enforced via your own ACLs
- All metadata stays in your house
- No company can change terms on you
- Prepares for mesh future
- Aligns with your values completely

---

## The Paradigm Shift

This isn't just about software — it's about belief.

**Current paradigm:**
- "Use this company's service, trust their incentives"
- "Your data is safe (until we get acquired)"
- "Free until we need to monetize"
- Kids are users to be engaged, not people to be protected

**Guardian's paradigm:**
- "Our family's data stays in our family"
- "Incentives must be aligned by design, not by promise"
- "Children deserve protection, not exploitation"
- "Technology should serve families, not extract from them"

Most family monitoring software is built BY companies, FOR data extraction, WITH surveillance as the business model.

Guardian is different:
- The family controls the infrastructure
- No external company sees the data
- Incentives are aligned (your kids are YOUR kids, not users)
- **The architecture itself encodes the values**

---

## Getting Started with Headscale

The path forward:

1. **Headscale setup on home hardware** — Raspberry Pi, old laptop, or $5/month VPS
2. **WireGuard client configuration for family devices** — Works on iOS, Android, macOS, Windows, Linux
3. **Integration with Guardian's identity system** — Tailscale node ID becomes family member ID
4. **ACL enforcement without external servers** — You control what each device can access
5. **Path toward mesh network future** — Architecture ready for community mesh when available

If the goal is protecting your children's data, trusting another company — even a "good" one — is a compromise.

**Self-hosting the identity layer removes that compromise entirely.**

---

*Let's GrOw!*
