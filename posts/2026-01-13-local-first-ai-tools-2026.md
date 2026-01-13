---
title: "Four Years of Local AI: From Experiment to Infrastructure"
tags: local-llm, ai, tools, privacy, families, ollama, guardian
date: 2026-01-13
---

# Four Years of Local AI: From Experiment to Infrastructure

*2026-01-13*

I ran my first local LLM in 2022. Back then it felt like tinkering—an expensive curiosity. Now it's the foundation of how I believe we all deserve to access and build AI actions.

---

## The Journey: 2022 to 2026

When I started running language models locally in 2022, GPT-3 was the standard. Local inference (for me) meant serious hardware and output that was… cute, but not dependable.

Four years later, the landscape has inverted:

**2022**: Local AI was an experiment. Serious hardware, inconsistent results.
**2024**: Local AI became viable. A "normal" computer could run something useful.
**2026**: Local AI is increasingly the default. It runs on laptops. The output is genuinely good for daily use.

The shift was both technical and philosophical. Technical because the models got dramatically better at handling tools, long contexts, and real workflows—especially with a good harness. Philosophical because the question changed from "can I run this locally?" to:

**"Why would I let someone else control the AI I or my loved ones depend on?"**

---

## Why Local-First Matters Now

A lot of "AI privacy" talk stays abstract until it hits family life.

When you or a loved one ask an AI for help—learning support, creative projects, tough questions—that interaction is usually processed on someone else's servers in the cloud. Depending on the provider and plan, prompts may be logged for safety/abuse prevention, debugging, and product improvement. Policies differ, retention windows differ, opt-outs differ—but the core reality is the same:

**cloud-first puts your most human questions inside someone else's systems.**

For families, it gets real fast.

When a kid asks awkward questions about growing up, or someone needs a patient, judgment-free conversation during a hard week… I want those moments to be handled like a private conversation, not a product event.

So I went to work building something different.

**Cloud AI often means:**

* Prompts processed remotely (internet dependency)
* Logs retained for some period (policies vary)
* Provider-defined content rules and defaults
* Provider-defined incentives (business model matters)
* Subject to outages and account lockouts

**Local AI means you can choose:**

* Prompts stay on your hardware (or your home server)
* Your data doesn't have to train anything
* Your policies, your values, your boundaries
* Works offline (or works "home-first" over a private tunnel)
* More control over availability and failure modes

That word **choose** is the point.

---

## What I Actually Built: Guardian Protocol

Guardian Protocol started as a question:

**What if "parental controls" were about wellbeing and skill-building—without a surveillance model?**

Most parental monitoring software is built on surveillance: caregivers see everything, kids see nothing. That creates an adversarial relationship. Kids learn to hide rather than learn.

I want to flip it.

**Transparency over surveillance.** Kids see the same dashboard guardians do.
**Conversation over punishment.** Each block is a conversation opportunity, not a gotcha.
**Digital development over screen-time obsession.**

The architecture mirrors the harness patterns we see in bigger LLM stacks:

```text
Guardian Code (CLI)     = CLI equivalent
Guardian Desktop (App)  = Desktop equivalent
Guardian.ai (Web)       = Web.ai equivalent
Guardian Network        = Router/Pi running local AI
```

The differentiator is incentives: Guardian is built for family wellbeing, not ad targeting.

And the key capability is *local-first routing*: every AI query from any family device can route through **your home server**.

Kid at school asks a question → it can tunnel back to your home AI → responds with your family's boundaries and values embedded.

That's not hypothetical. That's exactly what mesh networking is for.

---

## The 2026 Stack: What Actually Works

After four years of experimentation, here's what I run daily.

### The Foundation: Many Good Options

Starting out, **Ollama** makes local AI accessible in the simplest possible way.

On Linux, the official install is literally a one-liner: ([Ollama Docs][1])

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Then pull and run a model:

```bash
ollama run qwen3:14b
```

That's it. You're running a local model. (And yes, Ollama supports macOS/Windows too—but the key point is: setup is now minutes, not days.) ([Ollama Docs][1])

### llama.cpp: Production-Grade Control

When I need more control—more tuning, more deployment options, more harness work—**llama.cpp** is my go-to.

Its stated goal is straight-up what local-first builders care about: minimal setup, strong performance, wide hardware support, and support for many quantization levels to reduce memory use. ([GitHub][2])

In practice, this is where "local AI as infrastructure" becomes real: repeatable installs, reproducible model formats (GGUF), and a stack you can ship as a service inside your home or your org.

---

## Models Worth Running (January 2026)

I'm not interested in model fandom. I'm interested in: *what runs well, what's licensable, what's teachable, and what families can actually own.*

### Qwen3: My default open-weight family right now

The Qwen team explicitly "open-weighted" **six dense models** (0.6B, 1.7B, 4B, 8B, 14B, 32B) plus two MoE models (including **Qwen3-30B-A3B** and **Qwen3-235B-A22B**) under the **Apache 2.0 license**. ([Qwen][3])

They also report a real "parameter efficiency" jump: Qwen3 base models performing comparably to larger Qwen2.5 base models (e.g., 1.7B ≈ 3B; 4B ≈ 7B; 8B ≈ 14B; 14B ≈ 32B; 32B ≈ 72B). That's not me hyping—it's their published claim, and it tracks with what I see in day-to-day work: you get a lot more usefulness per gigabyte than you used to. ([Qwen][3])

### What I recommend people actually run

Instead of arguing theoretical "best," I like tables you can reproduce.

These are **Ollama's listed download sizes and context windows** for the Qwen3 tags (so readers can verify quickly). ([Ollama][4])

| Model               | Approx download size | Context window shown in Ollama | Good for                                                  |
| ------------------- | -------------------: | -----------------------------: | --------------------------------------------------------- |
| **Qwen3 0.6B**      |               ~523MB |                            40K | Edge devices, Raspberry Pi demos, "runs anywhere" helpers |
| **Qwen3 1.7B**      |               ~1.4GB |                            40K | Quick queries, learning support, lightweight workflows    |
| **Qwen3 4B**        |               ~2.5GB |                           256K | Daily chat, drafting, surprisingly good long-context work |
| **Qwen3 8B**        |               ~5.2GB |                            40K | Daily driver for most people (coding + general use)       |
| **Qwen3 14B**       |               ~9.3GB |                            40K | Heavier reasoning + synthesis + research support          |
| **Qwen3 32B**       |                ~20GB |                            40K | Higher ceiling work if you have the RAM/VRAM              |
| **Qwen3 30B (MoE)** |                ~19GB |                           256K | MoE efficiency (big feel, different cost profile)         |

**My daily drivers:** Qwen3 8B and 14B.

### Deep reasoning: DeepSeek-R1

When I want "slow thinking" for research and hard reasoning, I reach for **DeepSeek-R1** and distill variants.

DeepSeek's own release notes frame R1 as "performance on par with OpenAI-o1," and they state that **code and models are MIT-licensed**, explicitly encouraging distillation and commercial use. ([DeepSeek API Docs][5])

Their GitHub repo also states plainly that DeepSeek-R1 supports commercial use and derivative works including distillation for training other LLMs. ([GitHub][6])

---

## LocalScore: Measure Reality, Not Vibes

Benchmarks can be silly. But **LocalScore** is one of the rare benchmarks that's actually aligned with the user experience.

LocalScore combines:

* prompt processing speed
* generation speed
* time-to-first-token

…and turns that into a single comparable score. ([LocalScore][7])

Their interpretation is also refreshingly practical:

* **1,000 is excellent**
* **250 is passable**
* **below 100 is likely a poor experience** ([LocalScore][7])

LocalScore is labeled as **"A Mozilla Builders Project"** on the site and accelerator pages, and it notes that it leverages **llamafile** under the hood for portability. ([LocalScore][8])

If you're teaching families, running workshops, or building anything you want to be repeatable, this matters: you can stop arguing and start measuring.

---

## Real Hardware, Real Numbers

Instead of "trust me," here are **public LocalScore submissions** you can click and verify.

### Example: RTX 4090

On a published RTX 4090 entry (23GB), LocalScore reports:

* **~1727** on the 8B-class test
* **~972** on the 14B-class test ([LocalScore][8])

A different RTX 4090 entry (24GB) shows:

* **~1421** (8B-class)
* **~714** (14B-class) ([LocalScore][9])

That variance is the point: settings and configs matter, but the order-of-magnitude story is stable.

### Example: Mac Studio M3 Ultra (256GB)

A published Apple M3 Ultra entry (256GB) reports:

* **~394** on the 8B-class test
* **~216** on the 14B-class test ([LocalScore][10])

This is why I like LocalScore: it forces honesty. Some machines are monsters at certain classes of workloads, and merely "fine" at others.

### What I tell people now

* If you want local AI to feel "normal," aim for **~250+ on the 8B test** on *your hardware*, with your runtime. ([LocalScore][7])
* If you're building for a household or workshop (multiple users), you want more headroom than "passable."

---

## Licensing: Ownership Is a Feature

This is where a lot of local-first writing gets hand-wavy. I'm not willing to be hand-wavy here.

### Qwen3: Apache 2.0

Qwen3 is published as Apache 2.0 in the official release. ([Qwen][3])

Apache 2.0 is permissive and widely used, but it does have real obligations around including the license text and handling notices. (Normal, manageable stuff.) ([Apache Software Foundation][11])

### DeepSeek-R1: MIT

DeepSeek-R1 states that the code and weights are MIT-licensed, and explicitly permits commercial use and derivative works including distillation. ([GitHub][6])

MIT is also permissive, with minimal conditions (generally: keep the copyright + license text). ([Open Source Initiative][12])

### Why I moved away from Meta's Llama for "build it and own it forever"

Meta's Llama models are strong. This is not a model-quality complaint.

It's a licensing and downstream simplicity complaint.

For example, the Llama 3.1 Community License (as published on the model card) includes redistribution requirements like:

* include the agreement when you redistribute
* **prominently display "Built with Llama"** in certain product/documentation contexts
* include "Llama" at the beginning of a model name if you use Llama materials/outputs to train a distributed model
* additional commercial terms tied to a **700 million monthly active user** threshold ([Hugging Face][13])

Separately, the Open Source Initiative has publicly argued that Meta's Llama licensing does **not** meet the Open Source Definition (they frame it as "open washing"). ([Open Source Initiative][14])

None of this means "never use Llama." It means: if you're teaching families and community orgs to build tools they can own forever, permissive licensing is not an ideological flex—it's a durability strategy.

---

## The Interface Layer

For my work, I'm primarily:

* in the terminal with llama.cpp
* building harnesses with FastAPI + HTMX
* deploying specialized setups for educators (e.g., local-first access patterns that avoid shipping student data to third parties)

For family setups and workshops, visual interfaces matter. Beginners need something they can click before they can love the terminal.

---

## The Family AI Architecture: Mobile as Mesh Node

Here's the Guardian Protocol "full picture" insight:

your phone isn't just a device—it's a **node**.

```text
┌─────────────────────────────────────────────────────────┐
│                      YOUR HOME                           │
│  ┌─────────────────┐    ┌─────────────────┐             │
│  │  llama.cpp      │    │  Guardian       │             │
│  │  - Local LLMs   │◄──▶│  - Consent layer│             │
│  │  - Your control │    │  - Family values│             │
│  │                 │    │  - Transparency │             │
│  └─────────────────┘    └────────┬────────┘             │
│                                  │                       │
└──────────────────────────────────┼───────────────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
        ┌─────▼─────┐        ┌─────▼─────┐       ┌─────▼─────┐
        │Kid's phone│        │Kid's tablet│       │Kid's laptop│
        │ at school │        │at friend's │       │at library │
        │ (MESH NODE)│       │(MESH NODE) │       │(MESH NODE) │
        └───────────┘        └───────────┘       └───────────┘

        ALL DEVICES ARE MESH NODES
        CONNECTING BACK TO HOME AI
        FAMILY AI, FAMILY VALUES, ANYWHERE
```

Tools like **Headscale** (an open source, self-hosted implementation of the Tailscale control server) exist specifically to exchange WireGuard keys and coordinate private networks without requiring a cloud control plane. ([GitHub][15])

And if you want a practical walkthrough of "local AI + secure remote access," Tailscale has published a step-by-step guide showing an offline AI lab wired up with Ollama + secure access. ([Tailscale][16])

This is what makes local AI portable: not "run a model on your phone," but "bring your home AI with you."

---

## Teaching Families to Build

Running local AI for my own family was step one.

Step two is teaching the **producer mindset**: families building tools, not just subscribing to someone else's interface.

The success metric I care about is simple:
**every participant builds 2–3 working AI tools they own forever.**

This only works economically because local AI works. If I had to provision cloud credits for every family, the economics would collapse.

---

## What Changed My Mind

In 2022, I thought local AI was a hobby. Something for tinkerers with more time than sense.

In 2026, I see it as infrastructure—like having a backup power source or a water filter.

**Quality rose.** Open-weight models got good enough to be trusted for real tasks.
**Tooling matured.** What used to take days now takes minutes.
**Licensing became central.** If you can't legally own what you build, you don't really own it.
**Privacy stakes rose.** AI is becoming part of daily life. Families deserve control.

And yes: the Axios prediction energy is real—2026 is being framed as the year AI has to prove ROI ("show me the money"). For families and communities, ROI isn't measured in dollars. It's measured in ownership, privacy, and capability. ([Axios][17])

---

## Getting Started Today

### Minimum Viable Setup (fast)

1. Install Ollama (Linux): ([Ollama Docs][1])

   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```
2. Run a model:

   ```bash
   ollama run qwen3:8b
   ```

No account. No API key. You're local.

### Family Setup (home-first)

* Put Ollama or llama.cpp on one "home" machine
* Add a simple UI
* Create shared prompts and guardrails
* Then add mesh access so devices can tunnel home

---

## The Tools I've Tried (And Verdicts)

| Tool                    | Verdict                    | Notes                                                                                     |
| ----------------------- | -------------------------- | ----------------------------------------------------------------------------------------- |
| **llama.cpp**           | Essential                  | Local-first inference with strong hardware support and quantization options ([GitHub][2]) |
| **Ollama**              | Essential for starting     | Fast install + model library; easiest on-ramp ([Ollama Docs][1])                          |
| **LocalScore**          | Essential for benchmarking | Measures what users feel; Mozilla Builders Project ([LocalScore][7])                      |
| **Tailscale/Headscale** | Essential for mesh         | "Home AI everywhere" becomes real ([GitHub][15])                                          |
| **vLLM/SGLang**         | Production servers         | Great when you're serving many users (bigger org deployments)                             |
| **LM Studio**           | Good for beginners         | Native UI is a huge unlock for families                                                   |
| **Jan**                 | Promising                  | Privacy-first vibes, still evolving                                                       |
| GPT4All                 | Dated (for my use)         | Ollama + llama.cpp became my defaults                                                     |
| Text Generation WebUI   | Too complex (for families) | Powerful, but steep for workshops                                                         |

---

## What's Next

Local AI is now "good enough" for most daily work. And "good enough" is getting better.

**What I'm watching:**

* Smaller models with better reasoning (and better post-training)
* Speculative decoding and other throughput boosts
* MoE architectures where only a fraction of parameters are active per token (Qwen3 explicitly ships MoE variants) ([Qwen][3])
* Better on-device inference across Apple Silicon and new PC chips
* Better family-first tooling (consent layers, transparency dashboards, shared norms)

**What I'm building:**

* Guardian Protocol (consent-based AI for families)
* Curriculum that makes families producers first
* Local-first educational deployments that keep data sovereign

Four years ago, running local AI took real commitment. Today, the tools are ready, the models are good, and the stakes are higher.

The technology exists. The only question is whether you'll use it.

**Let's GrOw!**

---

## Resources

(Names + proof links you can cite in a blog.)

* **LocalScore** (what it measures + how to interpret scores) ([LocalScore][7])
* **Qwen3 official release** (model lineup + Apache 2.0 + base-model comparison claims) ([Qwen][3])
* **Ollama Linux install** (official one-liner) ([Ollama Docs][1])
* **Ollama Qwen3 library listing** (sizes + context windows shown) ([Ollama][4])
* **llama.cpp** (core repo) ([GitHub][2])
* **Headscale** (self-hosted control server; WireGuard key exchange) ([GitHub][15])
* **Tailscale local AI stack guide** (practical "self-host local AI + access anywhere") ([Tailscale][16])
* **DeepSeek-R1 release** (MIT license; distill & commercialize freely) ([DeepSeek API Docs][5])
* **Llama 3.1 license excerpt** ("Built with Llama" + 700M MAU clause) ([Hugging Face][13])
* **OSI critique of Llama licensing** (why they say it's not Open Source) ([Open Source Initiative][14])

---

[1]: https://docs.ollama.com/linux "Linux"
[2]: https://github.com/ggml-org/llama.cpp "GitHub - ggml-org/llama.cpp: LLM inference in C/C++"
[3]: https://qwenlm.github.io/blog/qwen3/ "Qwen3: Think Deeper, Act Faster"
[4]: https://ollama.com/library/qwen3 "qwen3"
[5]: https://api-docs.deepseek.com/news/news250120 "DeepSeek-R1 Release"
[6]: https://github.com/deepseek-ai/DeepSeek-R1 "DeepSeek-R1"
[7]: https://www.localscore.ai/about "About LocalScore"
[8]: https://www.localscore.ai/accelerator/1704 "NVIDIA GeForce RTX 4090 Results"
[9]: https://www.localscore.ai/accelerator/77 "NVIDIA GeForce RTX 4090 Results"
[10]: https://www.localscore.ai/accelerator/1359 "Apple M3 Ultra 24P+8E+80GPU Results"
[11]: https://www.apache.org/licenses/LICENSE-2.0 "Apache License, Version 2.0"
[12]: https://opensource.org/license/mit "The MIT License"
[13]: https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct "meta-llama/Llama-3.1-8B-Instruct · Hugging Face"
[14]: https://opensource.org/blog/metas-llama-license-is-still-not-open-source "Meta's LLaMa license is still not Open Source – Open Source Initiative"
[15]: https://github.com/juanfont/headscale "juanfont/headscale: An open source, self-hosted ..."
[16]: https://tailscale.com/blog/self-host-a-local-ai-stack "Self-host a local AI stack and access it from anywhere"
[17]: https://www.axios.com/2026/01/01/ai-2026-money-openai-google-anthropic-agents "2026 is AI's \"show me the money\" year"
