---
title: "Guardian Platform: Complete Architecture"
tags: guardian, family, local-first, ai, architecture, privacy
---

# Guardian Platform: Complete Architecture

## The Vision

**Guardian is not parental control software. It's a family learning network.**

| Traditional Tools (Bark, Gryphon, ASUS) | Guardian |
|----------------------------------------|----------|
| Track behavior | Teach behavior |
| Block/allow binary | Conversation about why |
| Punitive notifications | Supportive coaching |
| Data goes to company | Data stays local |
| One-size-fits-all | Family creates their own contracts |
| Admin dashboard (warden) | Chat interface (guide) |
| Reactive alerts | Proactive learning |

---

## Core Philosophy

```
┌─────────────────────────────────────────────────────────────────┐
│                    GUARDIAN PRINCIPLES                          │
├─────────────────────────────────────────────────────────────────┤
│  1. LOCAL-FIRST: Data never leaves the home network            │
│  2. AI AS TEACHER: Not surveillance, but supportive learning   │
│  3. FAMILY CONTRACTS: Families define their own agreements     │
│  4. CONVERSATION > CONFIGURATION: Chat to manage, not dashboards│
│  5. MODEL AGNOSTIC: Works with any LLM (local or cloud)        │
│  6. CONSENT-BASED: Kids understand and participate in rules    │
│  7. NETWORK-LEVEL: One place to manage all devices             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Architecture Overview

```
                         ┌─────────────────────────────────────┐
                         │         GUARDIAN NETWORK            │
                         │      (Home Router/Pi/NAS)           │
                         │                                     │
                         │  ┌─────────────────────────────┐   │
                         │  │     Local AI Runtime        │   │
                         │  │  (llama.cpp / Ollama)       │   │
                         │  │                             │   │
                         │  │  Models:                    │   │
                         │  │  - Llama 3.2 (fast)        │   │
                         │  │  - Mistral (reasoning)     │   │
                         │  │  - Custom fine-tuned       │   │
                         │  └──────────┬──────────────────┘   │
                         │             │                       │
                         │  ┌──────────▼──────────────────┐   │
                         │  │     Guardian Core           │   │
                         │  │                             │   │
                         │  │  - Family Contracts Engine  │   │
                         │  │  - Network Policy Manager   │   │
                         │  │  - Consent Protocol         │   │
                         │  │  - Learning Tracker         │   │
                         │  │  - MCP Server Hub           │   │
                         │  └──────────┬──────────────────┘   │
                         │             │                       │
                         └─────────────┼───────────────────────┘
                                       │
          ┌────────────────────────────┼────────────────────────────┐
          │                            │                            │
          ▼                            ▼                            ▼
   ┌─────────────┐            ┌─────────────┐            ┌─────────────┐
   │ Guardian CLI│            │Guardian App │            │Guardian Web │
   │             │            │  (Desktop)  │            │   (Local)   │
   │ Parents/    │            │             │            │             │
   │ Tech-savvy  │            │ Family Hub  │            │ Any Device  │
   │             │            │ Dashboard   │            │ Browser     │
   └─────────────┘            └─────────────┘            └─────────────┘
```

---

## Why This Matters

**Comparison: Guardian vs Current Tools**

| Feature | Bark | Gryphon | ASUS | Guardian |
|---------|------|---------|------|----------|
| Monitoring | Yes | Yes | Yes | Yes |
| Blocking | Yes | Yes | Yes | Yes |
| **Conversation** | No | No | No | Yes |
| **Teaching** | No | No | No | Yes |
| **Family contracts** | No | No | No | Yes |
| **Earned time** | No | No | No | Yes |
| **Local AI** | No | No | No | Yes |
| **Data stays home** | No | No | No | Yes |
| **Open source** | No | No | No | Yes |
| **Chat interface** | No | No | No | Yes |
| **Kid participation** | No | No | No | Yes |

---

## The Key Insight

Guardian helps families raise healthy humans in a digital world - not by blocking and tracking, but by teaching, conversing, and growing together.

- **Local-first**: Your data never leaves home
- **AI as teacher**: Not surveillance, but support
- **Family contracts**: Kids participate in rules
- **Conversation > Configuration**: Chat, don't dashboard
- **Model agnostic**: Use any LLM (local or cloud)
- **Open source**: Community-driven, transparent

---

*This is what the Baltimore AI Producers Lab philosophy demands: not consumers of surveillance tech, but producers of supportive family technology.*

**Let's GrOw!**
