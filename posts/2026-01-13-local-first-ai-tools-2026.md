---
title: "Four Years of Local AI: From Experiment to Infrastructure"
tags: local-llm, ai, tools, privacy, families, ollama, guardian
date: 2026-01-13
---

# Four Years of Local AI: From Experiment to Infrastructure

*2026-01-13*

I ran my first local LLM in 2022. Back then it felt like tinkering—an expensive curiosity. Now it's the foundation of how I think we should be able to **access AI**, **shape it**, and **build actions with it**—without handing our private lives to someone else.

This is a story about a technical shift, but also a values shift.

---

## The Journey: 2022 to 2026

When I started running language models locally in 2022, GPT-3 was still the mainstream reference point. Local inference (for me) meant pricey hardware and output that was *interesting*, but not something I'd trust day-to-day.

Four years later, the landscape has inverted:

**2022**: Local AI was an experiment. Serious hardware, mixed results.
**2024**: Local AI became genuinely viable. A gaming PC could run something *useful*.
**2026**: Local AI is often the default for privacy-first workflows. It can run on a laptop—and the output can be genuinely good.

The shift was both technical and philosophical.

Technical because the open model ecosystem got dramatically better—especially at instruction following, tool-use patterns, and long-context workflows. Qwen's own Qwen3 release notes call out the efficiency jump: smaller dense models matching older larger models in overall performance, and MoE models delivering strong results with far fewer *active* parameters.[^1]

Philosophical because the question changed from:

> "Can I run this locally?"

to:

> "Why would I outsource control over an AI my family depends on?"

---

## Why Local-First Matters Now

A lot of consumer cloud AI experiences involve prompts and/or metadata being retained under the provider's policies, with different defaults depending on product tier and settings. Even when providers say they don't "train on your data," many still log *something* for abuse monitoring, rate limiting, debugging, or product improvement.

For most users, that's abstract.

For families, it's concrete.

When you (or your kid) ask an AI for learning support, creative help, or a patient conversation through something awkward or difficult, that's **real life**—and I'd rather those moments live inside our walls by default.

So the goal isn't paranoia. It's sovereignty.

**Cloud AI often means:**
- Some level of logging/retention under someone else's policies
- Dependence on someone else's content rules
- Dependence on internet + uptime
- Incentives you don't control

**Local AI often means:**
- Prompts can stay on your device (or your server) by default
- You decide what gets stored, shared, or deleted
- You set household boundaries and values
- It still works when the internet doesn't

Local-first isn't "anti-cloud." It's **pro-control**.

---

## What I Actually Built: Guardian Protocol

Guardian Protocol started as a question:

**What if "parental controls" were about wellbeing and autonomy—not surveillance?**

Most parental monitoring software is built on an adversarial model:
- Caregivers see everything
- Kids see nothing
- Everyone learns to hide instead of think

I want to flip that.

**Transparency over surveillance.** Kids see the same dashboard guardians do.
**Conversations over punishments.** A block is a starting point, not a shutdown.
**Digital development over tracking.** Autonomy is taught incrementally, not forced.

The architecture mirrors the "harness" idea from larger LLM deployments:

```text
Guardian Code (CLI)     = CLI equivalent
Guardian Desktop (App)  = Desktop equivalent
Guardian.ai (Web)       = Web.ai equivalent
Guardian Network        = Router/Pi running local AI
```

The differentiator is incentives: Guardian is incentivized by family wellbeing—not ads, not engagement metrics, not data extraction.

### The "home AI" pattern

Every AI query from any family device can route through your home server:

- Kid at school asks a question → it tunnels back to home → answered by **your family AI**
- Family values embedded
- Local consent layer
- Age-appropriate scaffolding built into the platform

A mesh network (Headscale/WireGuard) is how that becomes "anywhere access." Headscale is a self-hosted control server for a Tailscale/WireGuard-style mesh.[^12]

This only works cleanly because the AI runs locally. Otherwise you're right back to trusting someone else's policies, data handling, incentives, and uptime.

---

## The 2026 Stack: What Actually Works

After four years of experimentation, here's what I run daily.

### The Foundation: Start Simple

**Ollama** makes local AI unusually accessible. Install, pull, run—done.[^18]

```bash
# Install (Linux)
curl -fsSL https://ollama.com/install.sh | sh

# Run a model
ollama run qwen3:14b

# That's it. You're running local AI.
```

The point is not that Ollama is "the best" at everything.

The point is the floor is low enough that families can start without a 3-week ops project.

### llama.cpp: Control + Portability

When I want more control or I'm building a harness with tools, **llama.cpp** is still one of the most important projects in local inference.[^2]

My workflow is usually:

* Start with the simplest prompt that works
* Add structure only when needed (system prompt, schemas)
* Add retrieval only when the model truly needs outside context
* Treat agents as a *last resort*, not a first instinct

---

## Models Worth Running (January 2026)

Here's my updated shortlist, with an emphasis on:

* **Quality per compute**
* **Licensing clarity**
* **What normal people can actually run**

### The state of the open model stack: Qwen3

Qwen's official Qwen3 release notes spell out the lineup (dense + MoE), context lengths, and the Apache 2.0 licensing for the open-weight release.[^1] They also explicitly claim an efficiency jump vs Qwen2.5.

### OpenAI's open-weight gpt-oss models

OpenAI released **gpt-oss-20b** and **gpt-oss-120b** as open-weight models under Apache 2.0.[^3] They're MoE models (sparse active params) with **128k context**. The launch post states:

* gpt-oss-20b can run with **~16 GB memory** in some setups
* gpt-oss-120b can run efficiently on a **single 80 GB GPU** (deployment-dependent)

OpenAI's "run locally with Ollama" guide gives practical consumer guidance:

* 20b best with **≥16 GB VRAM/unified memory**
* 120b best with **≥60 GB VRAM/unified memory** (CPU offload works but slower)[^4]

### Quick model table

The "Size (download)" column uses **Ollama tag sizes** for common quantized builds.[^2][^5][^6]

| Model (Ollama tag)  | Class              | Size (download) | Context | Why I reach for it                              |
| ------------------- | ------------------ | --------------: | ------- | ----------------------------------------------- |
| `qwen3:4b`          | Dense              |         ~2.6 GB | 32K     | Fast daily helper, good "family laptop" floor   |
| `qwen3:8b`          | Dense              |         ~5.2 GB | 128K    | My default "general" local model                |
| `qwen3:14b`         | Dense              |         ~9.3 GB | 128K    | Better reasoning + writing; strong all-rounder  |
| `qwen3:30b-a3b`     | MoE                |          ~19 GB | 128K    | Efficiency monster: 30B total / 3B active       |
| `qwen3:235b`        | MoE                |         ~142 GB | 128K    | "Home frontier": big reasoning, big creativity  |
| `gpt-oss:20b`       | MoE                |          ~14 GB | 128K    | Go-to for tool use + reasoning on consumer gear |
| `gpt-oss:120b`      | MoE                |          ~65 GB | 128K    | Serious reasoning + agent workflows (big memory)|
| `gemma3:27b`        | Dense (multimodal) |          ~17 GB | 128K    | When I want vision + big model vibes            |

**My daily drivers:** Qwen3 8B, 14B, and gpt-oss:20b for tool-heavy work.

### Licensing reality

When you teach families to build tools they own forever, licensing isn't a footnote—it's the foundation.

* **Qwen3**: Open-weight under **Apache 2.0**[^1]
* **gpt-oss**: Open-weight under **Apache 2.0**[^3]
* **DeepSeek R1**: MIT-licensed (clean and permissive for downstream)[^16]
* **Meta Llama**: A community license with additional terms (including restrictions tied to user scale). Read before you build a business on it.[^15]

That's why I've leaned harder into Qwen + gpt-oss + MIT-style releases for "build it and keep it" teaching.

---

## LocalScore: Real Benchmarks, Not Vibes

When people ask "will this run on my machine?" I point them to **LocalScore**.

LocalScore measures:

* prompt processing speed (tokens/sec)
* generation speed (tokens/sec)
* time to first token (latency)
…then combines them into a single score.[^7]

LocalScore gives a simple rule of thumb:

* **1,000 is excellent**
* **250 is passable**
* **below 100 is likely a poor experience**[^7]

LocalScore is a **Mozilla Builders** project.[^8][^9]

If you're teaching families, this matters: it's the difference between "AI is magical" and "AI is measurable."

---

## Real Hardware, Real Numbers

I'm not interested in theoretical FLOPS. I'm interested in **what people can feel**.

### RTX 4090 (example)

On LocalScore's "Small" 8B benchmark, an RTX 4090 result shows:

* Prompt: **~7,594 tokens/s**
* Generation: **~120 tokens/s**
* TTFT: **~176 ms**
* LocalScore: **~1,727**[^8]

### Mac Studio M3 Ultra (256GB)

LocalScore has a public result entry for an Apple M3 Ultra system with **256 GB** showing (8B benchmark):

* Prompt: **~1,062 tokens/s**
* Generation: **~63.3 tokens/s**
* TTFT: **~1.10 s**
* LocalScore: **~394**[^9]

That's why I keep saying: Apple unified memory changes what "local" can mean for families and workshops.

Apple states Mac Studio with M3 Ultra can be configured up to **512 GB unified memory**.[^10]

This is exactly the tier where models like `gpt-oss:120b` and `qwen3:235b` stop being fantasy and start being "infrastructure."

### Raspberry Pi 5: Not a Meme, Just a Different Tier

A Raspberry Pi 5 (8GB) board is still around **$95** at common retailers.[^11]

Is it going to run a 235B MoE? No.

But for:

* always-on family portal
* lightweight models (Qwen3 0.6B, 1.7B)
* routing + consent + simple UI

…it's a legitimate building block.

---

## The Family AI Architecture: Mobile as Mesh Node

Here's the mental model I teach:

Your mobile device isn't just a "runner" for AI. It's a **node** in your mesh that gives you access to home infrastructure from anywhere.

```text
┌─────────────────────────────────────────────────────────┐
│                      YOUR HOME                           │
│  ┌─────────────────┐    ┌─────────────────┐             │
│  │  Local LLMs      │    │  Guardian       │             │
│  │  - llama.cpp     │◄──▶│  - Consent layer│             │
│  │  - Ollama        │    │  - Transparency │             │
│  │  - Your control  │    │  - Family values│             │
│  └─────────────────┘    └────────┬────────┘             │
│                                  │                       │
└──────────────────────────────────┼───────────────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
        ┌─────▼─────┐        ┌─────▼─────┐       ┌─────▼─────┐
        │Kid's phone│        │Kid's tablet│       │Kid's laptop│
        │ at school │        │at friend's │       │at library │
        │ (MESH NODE)│        │(MESH NODE) │       │(MESH NODE) │
        └───────────┘        └───────────┘       └───────────┘
```

Headscale/WireGuard makes the mesh real.[^12]
Tailscale has published a "self-host a local AI stack and access it anywhere" walkthrough.[^13]

The consent layer is the point. Guardian tracks agreements between family members—what's allowed, what triggers a conversation, what's earned through responsibility. It's about teaching autonomy, not enforcing obedience.

---

## Teaching Families to Build

Running local AI for my own family was step one.

Step two is the Baltimore AI Producers Lab—a grant-funded initiative teaching families to build AI tools instead of only consuming them.

The producer mindset matters more than technical skills:

* Teens can be consumers by default
* Producers take longer—but they own what they build

We start early (around 12) because identity forms early.

**Youth (12-17)** build AI games, homework helpers, creative tools.
**Young Adults (18-25)** create resume builders, job automators, portfolio generators.
**Caregivers** develop budget tools, benefits navigators, side-hustle assistants.
**Families Together** solve real community problems with AI.

Success metric: every participant builds 2–3 working AI tools they own forever.

This only works because local AI works. If I had to provision cloud credits for every family, the economics collapse.

---

## What Changed My Mind

In 2022, I thought local AI was a hobby.

In 2026, I see it as **infrastructure**—like a backup battery or a water filter.

What actually changed:

* **Quality caught up.** Qwen's release notes emphasize big efficiency gains and practical performance across sizes.[^1]
* **Tooling matured.** Ollama made "start here" real.[^18]
* **Benchmarks got better.** LocalScore makes performance measurable, and gives usable thresholds.[^7]
* **Open-weight got serious.** gpt-oss is Apache 2.0, 128k context, and explicitly aimed at local deployment.[^3][^4]
* **Stakes rose.** AI moved from novelty to daily companion. Families deserve control.

Axios framed 2026 as a "show me the money" year for AI in the enterprise.[^17] For families and communities, ROI isn't just dollars. It's privacy, capability, and ownership.

---

## Getting Started Today

### Minimum viable setup (often under an hour)

1. Install Ollama (Linux):
   `curl -fsSL https://ollama.com/install.sh | sh`[^18]
2. Pull a model: `ollama pull qwen3:8b`
3. Run it: `ollama run qwen3:8b`

No account. No API key. You're running local AI.

### Family setup (an afternoon)

1. Put Ollama on a home machine (old laptop, mini PC, etc.)
2. Add a simple UI (LM Studio is great for families)[^14]
3. Build shared prompts for family use cases
4. Add a mesh so it works anywhere (Tailscale or Headscale)[^12][^13]

### Guardian-ready setup (the direction I'm building)

* Self-hosted mesh (Headscale)
* Consent contracts
* Family values embedded
* Transparent dashboards that kids can see too

---

## The Tools I've Tried (And Verdicts)

| Tool                    | Verdict                  | Notes                                          |
| ----------------------- | ------------------------ | ---------------------------------------------- |
| **llama.cpp**           | Essential                | Control, portability, vendor-neutral inference |
| **Ollama**              | Essential for starting   | Lowest barrier to "it's running"[^18]          |
| **LM Studio**           | Great for families       | Cross-platform, uses llama.cpp/MLX[^14]        |
| **LocalScore**          | Essential for benchmarks | Real measurements + practical thresholds[^7]   |
| **Tailscale/Headscale** | Essential for mesh       | "Home AI everywhere" pattern[^12][^13]         |
| **vLLM/SGLang**         | Production servers       | When serving at scale is the goal              |
| **Jan**                 | Promising                | Privacy-first direction, watch this space      |

---

## What's Next

Local AI in 2026 is good enough for most daily use. And "good enough" keeps getting better.

**What I'm watching:**

* Smaller models with better reasoning (distillations, MoE improvements)
* Speculative decoding and throughput tricks
* Better on-device inference (Apple Silicon, Snapdragon-class NPUs)
* Family-first UX: consent, transparency, developmental scaffolding

**What I'm building:**

* Guardian Protocol integration with local LLMs (consent-based AI for families)
* Shannon Protocol (compression layer for local-first cloud acceleration—only when you choose)
* Baltimore AI Producers Lab curriculum
* Maryland CTE crosswalks (local RAG for education pathways)
* Edinfinite platform (multi-tenant educational AI that keeps data sovereign)

Four years ago, running local AI took commitment—expensive hardware, rough tooling, patience with mediocre output.

Today the tools are mature. The models are strong. And the stakes are higher.

Here's what I know:

You can run AI that's *good enough to matter* on hardware you already own.
You can teach your kids to build with AI instead of only consuming it.
You can keep your family's questions, growth, and private moments in-house by default.

The technology exists. The tools are ready.

**Let's GrOw.**

---

## Resources

* LocalScore.ai — benchmark + public results database: [localscore.ai](https://localscore.ai)
* LocalScore scoring explanation: [localscore.ai/about](https://www.localscore.ai/about)
* Qwen3 official release notes: [qwenlm.github.io/blog/qwen3](https://qwenlm.github.io/blog/qwen3/)
* Ollama Qwen3 tags: [ollama.com/library/qwen3/tags](https://ollama.com/library/qwen3/tags)
* OpenAI gpt-oss intro: [openai.com/index/introducing-gpt-oss](https://openai.com/index/introducing-gpt-oss/)
* OpenAI "run gpt-oss locally with Ollama": [cookbook.openai.com/articles/gpt-oss/run-locally-ollama](https://cookbook.openai.com/articles/gpt-oss/run-locally-ollama)
* Ollama gpt-oss tags: [ollama.com/library/gpt-oss/tags](https://ollama.com/library/gpt-oss/tags)
* Ollama Gemma3 tags: [ollama.com/library/gemma3/tags](https://ollama.com/library/gemma3/tags)
* Headscale (self-hosted mesh control server): [github.com/juanfont/headscale](https://github.com/juanfont/headscale)
* Tailscale local AI stack guide: [tailscale.com/blog/self-host-a-local-ai-stack](https://tailscale.com/blog/self-host-a-local-ai-stack)
* LM Studio docs: [lmstudio.ai/docs/app](https://lmstudio.ai/docs/app)
* Meta Llama license: [llama.com/llama3_1/license](https://www.llama.com/llama3_1/license/)
* DeepSeek R1 listing (MIT noted): [ollama.com/library/deepseek-r1](https://ollama.com/library/deepseek-r1)
* Raspberry Pi 5 (8GB) example pricing: [canakit.com/raspberry-pi-5-8gb.html](https://www.canakit.com/raspberry-pi-5-8gb.html)
* LocalScore RTX 4090 example: [localscore.ai/accelerator/1704](https://www.localscore.ai/accelerator/1704)
* LocalScore M3 Ultra 256GB example: [localscore.ai/accelerator/1359](https://www.localscore.ai/accelerator/1359)
* Apple Mac Studio (unified memory up to 512GB): [apple.com/shop/buy-mac/mac-studio](https://www.apple.com/shop/buy-mac/mac-studio)
* Axios AI Predictions 2026: [axios.com/2025/01/06/ai-predictions-2026-show-me-the-money](https://www.axios.com/2025/01/06/ai-predictions-2026-show-me-the-money)
* Ollama install docs: [docs.ollama.com/linux](https://docs.ollama.com/linux)
* llama.cpp: [github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)

---

## Footnotes

[^1]: Qwen team release notes: model lineup, context lengths, Apache 2.0 licensing, and efficiency/performance claims vs Qwen2.5.

[^2]: llama.cpp: LLM inference in C/C++ with minimal setup and wide hardware support.

[^3]: OpenAI gpt-oss launch post + model card: Apache 2.0, 128k context, memory/deployment guidance, and positioning for local inference.

[^4]: OpenAI Cookbook: "run gpt-oss locally with Ollama" (consumer VRAM/unified memory guidance for 20b and 120b).

[^5]: Ollama gpt-oss tags: practical pull sizes for 20b and 120b variants.

[^6]: Ollama Gemma3 tags: 27B variant, multimodal support, 128k context, and pull sizes.

[^7]: LocalScore about/blog: what it measures, how scoring works, and the 1000/250/100 thresholds.

[^8]: LocalScore RTX 4090 results page: concrete prompt/gen/TTFT/LocalScore numbers.

[^9]: LocalScore Apple M3 Ultra 256GB results page: concrete prompt/gen/TTFT/LocalScore numbers.

[^10]: Apple Mac Studio pages: configuration details (unified memory up to 512GB).

[^11]: CanaKit Raspberry Pi 5 8GB pricing example.

[^12]: Headscale GitHub: open-source self-hosted control server for a Tailscale/WireGuard-style mesh.

[^13]: Tailscale blog: "self-host a local AI stack and access it from anywhere."

[^14]: LM Studio docs: cross-platform support and llama.cpp/MLX runtime notes.

[^15]: Meta Llama license page (community license terms).

[^16]: Ollama DeepSeek R1 listing notes MIT license.

[^17]: Axios AI Predictions 2026 ("show me the money" framing).

[^18]: Ollama docs/download pages: supported OSes + install script command.
