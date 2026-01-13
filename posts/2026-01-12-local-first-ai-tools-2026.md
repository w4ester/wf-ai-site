---
title: "Four Years of Local AI: From Experiment to Infrastructure"
tags: local-llm, ai, tools, privacy, families, ollama, guardian
date: 2026-01-12
---

# Four Years of Local AI: From Experiment to Infrastructure

*I ran my first local LLM in 2022. Back then it felt like tinkering—an expensive curiosity. Now it's the foundation of how I believe we all deserve to access and build AI actions.*

---

## The Journey: 2022 to 2026

When I started running language models locally in 2022, GPT-3 was the standard. Local inference meant a $10K GPU and output that barely passed muster. Four years later, the landscape has completely inverted:

**2022**: Local AI was an experiment. Serious hardware, mediocre results.
**2024**: Local AI became viable. A gaming PC could run something useful.
**2026**: Local AI is the default. It runs on a laptop. The output is genuinely good.

The shift was both technical and philosophical. Technical because the models got better at handling features and actions, and started to gain on larger models—especially with a really good harness. Philosophical because the question changed from "can I run this locally?" to "why would I let someone else control the AI I or my loved ones depend on?"

---

## Why Local-First Matters Now

Every query to a cloud AI is logged somewhere. It's training someone else's model. It's subject to someone else's content policies. It's dependent on someone else's business model.

For most users, this is an abstract concern. For families, it's concrete.

When you or a loved one ask an AI for support or help—learning support, creative projects, difficult questions—that query lives in a corporate database. When they ask awkward questions about growing up, those get logged too. When they're working through something difficult and need a patient, judgment-free conversation, do you want that in someone's training data?

I didn't want that for my loved ones, or for me, or for you. So I went to work building something different for those types of motivations.

**Cloud AI gives you:**
- Queries logged forever
- Data training their models
- Their content policies
- Their values embedded
- Internet dependency
- Subject to outages

**Local AI gives you:**
- Queries stay on your device
- Data trains nothing
- YOUR content policies
- Your values configurable
- Works offline
- Always available

---

## What I Actually Built: Guardian Protocol

Guardian Protocol started as a question: what if parental controls were about wellbeing rather than surveillance—for teaching and supporting young people?

Most parental monitoring software is built on a surveillance model. Caregivers see everything, kids see nothing. It creates an adversarial relationship. Kids learn to hide rather than think critically about their digital lives.

I want to give more choice to flip this. Transparency over surveillance. Kids see the same dashboard guardians do. Each block is a conversation opportunity rather than just a restriction. Digital development over just tracking screen time.

The architecture mirrors larger LLM harnesses and structures:

```
Guardian Code (CLI)     = CLI equivalent
Guardian Desktop (App)  = Desktop equivalent
Guardian.ai (Web)       = Web.ai equivalent
Guardian Network        = Router/Pi running local AI
```

The key differentiator: Guardian is incentivized by family wellbeing rather than advertising.

Every AI query from any family device routes through your home server. Your kid at school asks a question—it goes through your home AI, responds with your family's AI built with your child in mind and with your child (age-appropriate projects built into the AI platform), your values embedded. Secure mesh networking (Headscale/WireGuard) makes this work anywhere.

This only works because the AI runs locally. If I depended on a cloud provider, I'd be back to trusting someone else's content policies, someone else's data handling, someone else's business model, and someone else's incentives.

---

## The 2026 Stack: What Actually Works

After four years of experimentation, here's what I run daily.

### The Foundation: Many Good Options

Starting out, **Ollama** makes local AI quite accessible. One command to download, one command to run:

```bash
# Install
curl -fsSL https://ollama.com/install.sh | sh

# Run a model
ollama run qwen3:14b

# That's it. You're running local AI.
```

Ollama is simple, works on Mac, Linux, Windows, and the community keeps the model library growing.

### llama.cpp: Production-Grade Control

**llama.cpp** is something I use often with more actions and features. With large language models becoming quite good with large context windows, you can trust that if you give the GitHub repo of a project and ask for support to use either platform, you will get results within the same minute to setup and have running locally on your device.

I've done many workshops with many backgrounds, and within a 1-hour workshop everyone—seriously everyone—left with local AI running on their machine(s).

For me this leads into languages... and well, since 2008 Python was my choice. The Zen of Python applies to local AI: explicit over implicit, simplest approach first, flat over nested. Start with zero-shot prompting, only add Chain of Thought when needed, only add RAG when you must, only reach for agents as a last resort.

However, I will say that with plugins—MCP servers, tools, hooks, skills (folder/file systems explaining how to do something and chaining together with models)—the complexity ceiling has risen dramatically while the floor stays simple.

### Models Worth Running (January 2026)

If you only want to learn *one* open-weight family deeply right now, I'd bet on **Qwen3**.

Qwen3 is open-weighted across a full range: **six dense models** (0.6B → 32B) plus **two MoE models** (including a 30B model with ~3B activated parameters). It's released under **Apache 2.0**, and it's designed for a practical reality: sometimes you want fast answers, and sometimes you want deliberate step-by-step reasoning. Qwen3 supports **hybrid thinking modes** you can toggle depending on the moment. [1]

In the real world, I don't pick models based on internet discourse. I pick them based on *what I'm doing*:

* **Small + snappy**: quick questions, lightweight tutoring, "I just need a second brain."
* **Mid-size daily driver**: homework support, life admin, coding help, writing.
* **Bigger reasoning / multi-user**: heavier synthesis, deep research, more simultaneous users.

Here's a **practical Qwen3 shortlist** you can actually run (these sizes/context windows are shown in the Ollama library, which makes them easy to verify and reproduce). [2]

| Model (Ollama tag) | Download size | Context window | What it's great at |
| ------------------ | ------------: | -------------: | ------------------ |
| `qwen3:0.6b` | ~523MB | 40K | "Runs anywhere" demos, edge devices, simple helpers |
| `qwen3:1.7b` | ~1.4GB | 40K | Fast Q&A, learning support, light drafting |
| `qwen3:4b` | ~2.5GB | 256K | Surprisingly capable general assistant, long-context projects |
| `qwen3:8b` | ~5.2GB | 40K | The *daily driver sweet spot* for most people |
| `qwen3:14b` | ~9.3GB | 40K | Heavier synthesis + better "stay on task" performance |
| `qwen3:30b` | ~19GB | 256K | MoE efficiency (big brain feel without always paying full cost) |
| `qwen3:32b` | ~20GB | 40K | Higher ceiling reasoning + writing, when you can afford the RAM/VRAM |
| `qwen3:235b` | ~142GB | 256K | "Bring a server" territory (included here for completeness) |

**My daily drivers:** Qwen3 **8B** and **14B**.

And when I want more "slow thinking" for research and reasoning tasks, I reach for **DeepSeek-R1** (or its distill variants). DeepSeek-R1's repo states the **code + weights are MIT-licensed**, and explicitly permits **commercial use, modification, derivative works, and distillation for training other LLMs** — which is exactly the kind of clarity you want when you're building tools meant to last. [3] DeepSeek also publicly framed the release as **MIT** with "distill & commercialize freely." [4]

For workshops at the Baltimore AI Producers Lab, I keep Qwen3 0.6B-4B loaded so families can see what runs on *their* hardware—phones, old laptops, Raspberry Pis.

### The Interface Layer

For my work, I'm primarily in the terminal with llama.cpp or building custom harnesses with FastAPI + HTMX. **EduPilot** is a customized deployment for Maryland educators, giving teachers access to AI without sending student data to third parties.

For family setups and workshops, visual interfaces help—LM Studio for beginners who prefer native apps, or custom web interfaces for multi-user households.

---

## LocalScore: Benchmark the Experience

I'm done arguing "this laptop can run local AI" in the abstract.

**Run a benchmark that measures what users actually feel.** That's what **LocalScore** does: it combines three metrics into one comparable number:

* **Prompt processing speed** (tokens/sec)
* **Generation speed** (tokens/sec)
* **Time to first token** (latency) [5]

LocalScore also gives you an interpretation that maps cleanly to real life:

* **1,000 = excellent**
* **250 = passable**
* **below 100 = likely a poor experience** [5]

Under the hood, LocalScore leverages **llamafile**, which helps keep benchmarking portable across setups. [5]

If you're building a family setup, a school lab, a community workshop, or anything multi-user: **LocalScore is a sanity check** before you buy gear or promise performance.

---

## The Family AI Architecture

Here's the full picture of what Guardian Protocol enables:

<!-- Diagram: Family AI Architecture - For users of screen readers: This diagram shows a home server running llama.cpp and Guardian, connecting to family devices anywhere via a mesh network. AI queries from kids at school or friends' houses route back through the family's own infrastructure with family values embedded. -->

```
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
        └───────────┘        └───────────┘       └───────────┘

        ALL AI QUERIES ROUTE HOME
        FAMILY AI, FAMILY VALUES
```

The mesh network connects everything. Kid at school asks a question, it routes through your home AI, responds with your family's values embedded.

The consent layer is key. Guardian tracks agreements between family members—what's allowed, what triggers a conversation, what's earned through responsibility. It's about teaching autonomy incrementally.

---

## Teaching Families to Build

Running local AI for my own family was step one. Step two is the Baltimore AI Producers Lab—an initiative teaching families to build AI tools rather than consume them.

The producer mindset matters more than the technical skills. Many teens use ChatGPT for homework, but few understand how it works. Families pay monthly subscriptions to be AI consumers with no ownership. By age 18, consumer habits are already solidified.

We start at age 12. That's when producer identity forms—before consumer habits lock in. And we teach families together because household culture change sticks.

**Youth (12-17)** build AI games, homework helpers, creative tools.
**Young Adults (18-25)** create resume builders, job automators, portfolio generators.
**Caregivers** develop budget tools, benefits navigators, side-hustle assistants.
**Families Together** solve real community problems with AI.

Success metric: every participant builds 2-3 working AI tools they own forever.

The hardware is modest: workshop systems for group learning, loaner laptops, take-home kits. The models that matter run on phones (Qwen3 0.6B-1.7B) and any laptop from the last five years (Qwen3 4B-8B).

This only works because local AI works. If I had to provision cloud API credits for every family, the economics would collapse.

---

## Real Hardware, Real Numbers

Here's the part people skip: *what "good" looks like depends on the model size you care about.*

LocalScore publishes real submissions by accelerator. So instead of hand-wavy claims, you can point to actual results.

### Example: RTX 4090 (8B + 14B)

A submitted **RTX 4090** entry shows LocalScore around:

* **~1727** for an **8B** class test
* **~972** for a **14B** class test [6]

Using LocalScore's own interpretation, that's **excellent** on 8B and very strong on 14B. [5]

### Example: Apple M3 Ultra (8B + 14B)

A submitted **Apple M3 Ultra (256GB)** entry shows LocalScore around:

* **~394** for **8B**
* **~216** for **14B** [7]

That's **comfortably "passable"** on 8B and **near-passable** on 14B by LocalScore's thresholds — and that framing is way more honest than pretending every machine is "near-cloud." [5]

### What I recommend in practice

* If your goal is **"local AI feels normal"** for one person, aim for **250+ on the 8B score**. [5]
* If your goal is **multi-user household / workshop**, you're looking for more headroom — and LocalScore makes that visible immediately. [5]

### Quick hardware guide

| Hardware | Approx. Cost | Best For |
|----------|-------------:|----------|
| Raspberry Pi 5 (8GB) | $80-100 | Always-on helpers, edge demos, learning |
| Any laptop 2020+ (8GB RAM) | $0 (what you have) | Getting started, Qwen3 1.7B-4B |
| 16GB system (used ThinkPad/Mac Mini) | $400-800 | Daily driver, Qwen3 8B |
| 32GB+ or GPU 12GB+ VRAM | $1,500-2,500 | Qwen3 14B-32B, serious work |
| Mac Studio M3 Ultra (256GB) | ~$8,000 | Workshop powerhouse, frontier models locally |

The rule of thumb: 8GB of RAM to run the 7B models, 16GB to run the 13B models, and 32GB to run the 33B models. Quantization (Q4_K_M) cuts memory requirements by ~75% while maintaining quality.

---

## Licensing: Own It Forever

Licenses are the difference between "we built something our family owns forever" and "we built something that becomes legally awkward the moment it leaves our laptop."

### Why I bias toward Apache 2.0 and MIT for family/community tools

**Qwen3 is Apache 2.0.** That's permissive, commercial-friendly, and sane for downstream builders. [1]

Apache 2.0 still has real obligations (this is a feature): you generally need to **include the license text** in distributions and handle **NOTICE** requirements appropriately. The Apache Software Foundation provides clear guidance on how LICENSE/NOTICE work in real distributions. [8] [9]

**DeepSeek-R1 is MIT.** MIT is also permissive and commercially usable, and DeepSeek explicitly calls out distillation and derivative works as allowed — which matters if you're teaching, fine-tuning, or shipping. [3] [4]

### Why I moved away from Meta's Llama (even though the models are strong)

Meta's **Llama 3 Community License** includes additional conditions that matter the moment you redistribute or productize:

* You must display **"Built with Meta Llama 3"** in certain distribution contexts
* There are **naming requirements** for derived AI model names in some cases
* There's a restriction against using the model's **outputs to improve other LLMs**
* And there's a special commercial clause tied to **700M monthly active users** [10]

None of that makes Llama unusable. But if your mission is "families build tools they own forever," then license simplicity is part of the product.

---

## What Changed My Mind

In 2022, I thought local AI was a hobby. Something for tinkerers with more time than sense.

In 2026, I see it as essential infrastructure—like having your own backup power or water filter.

**Quality caught up—especially with fine-tuning and specific data for specific tasks with the right harness.** Local models went from "amusing" to "actually useful" to "genuinely good."

**Hardware requirements dropped.** A laptop with 16GB RAM runs genuinely useful models. A Raspberry Pi 5 (8GB, $80) can host a family chat interface.

**Tooling matured.** What took weeks, then days, then hours of configuration now takes minutes. I remember when it took months.

**AI stands for Accessible Intelligence and Accelerated Intelligence** given the right mindset.

**Privacy stakes rose.** As AI became integrated into daily life, the data implications became clearer. Kids using AI for learning, for questions, for exploration. That's data worth controlling.

**The business models clarified.** Cloud AI providers need to monetize your queries. They need to train on your data. They need to align their content policies with their advertisers. The incentives favor their business rather than your family.

---

## Getting Started Today

### Minimum Viable Setup (30 minutes)

1. Install Ollama: `curl -fsSL https://ollama.com/install.sh | sh`
2. Pull a model: `ollama pull qwen3:8b`
3. Run it: `ollama run qwen3:8b`

You now have local AI. No account. No API key. No data leaving your machine.

### Family Setup (2-3 hours)

1. Install Ollama on a home server (old laptop, Raspberry Pi 5, NAS)
2. Set up a simple interface (LM Studio for visual, or just terminal—kids learn fast)
3. Create shared prompts for family use cases
4. Pull age-appropriate models
5. Set up local network access so everyone can reach it

### Guardian-Ready Setup (ongoing project)

Everything above, plus:
- Headscale for anywhere access
- Guardian Protocol for contracts and transparency
- Family values embedded in system prompts
- Consent layer for age-appropriate boundaries

---

## The Tools I've Tried (And Verdicts)

| Tool | Verdict | Notes |
|------|---------|-------|
| **llama.cpp** | Essential | Production-grade, offline-first, vendor-neutral |
| **Ollama** | Essential for starting | Foundation of everything, best for workshops and getting started |
| **LM Studio** | Good for beginners | Native app, easy to explore, auto-detects hardware |
| **vLLM/SGLang** | Production servers | For deployment at scale |
| **Jan** | Promising | Privacy-first, open-source, offline-first design |
| GPT4All | Dated | Ollama surpassed it |
| Text Generation WebUI | Too complex | Overkill for families |

---

## What's Next

Local AI in 2026 is good enough for most daily use. And "good enough" keeps getting better.

**What I'm watching:**
- Smaller models with better reasoning (Qwen3 distillations, DeepSeek-R1 variants)
- Speculative decoding—using tiny models to pre-predict for large models, boosting throughput
- MoE architectures that activate only needed parameters (Qwen3-30B-A3B fits on consumer hardware)
- On-device inference improvements (Apple Silicon, Qualcomm Snapdragon X)
- Better tooling for families new to this

**What I'm building:**
- Guardian Protocol integration with local LLMs (consent-based AI for families)
- Shannon Protocol (compression layer for local-first cloud acceleration—when you need cloud power, you control what leaves your device)
- Baltimore AI Producers Lab curriculum (teaching families to be producers first, users second)
- Maryland CTE crosswalks (local RAG for career and technical education pathways)
- Edinfinite platform (multi-tenant educational AI that keeps data sovereign)

---

Four years ago, running local AI took real commitment—expensive hardware, rough tooling, patience with mediocre output. That work laid the foundation.

Today, the tools have matured. The models have caught up. And the stakes keep rising.

Here's what I know: the choice is real now. You can run AI that rivals the best cloud services on hardware you already own. You can teach your kids to build with AI rather than just consume it. You can keep your family's conversations, questions, and growth inside your own walls.

This is what I built. This is what my family uses. And this is what you can have too.

The technology exists. The tools are ready. The only question is whether you'll use them.

---

*Let's GrOw!*

---

## Sources

[1] Qwen3 official blog (Apache 2.0, model lineup, MoE active params, hybrid thinking):
https://qwenlm.github.io/blog/qwen3/

[2] Ollama Qwen3 library (download sizes + listed context windows by tag):
https://ollama.com/library/qwen3

[3] DeepSeek-R1 GitHub (MIT license + explicitly allows distillation/derivatives):
https://github.com/deepseek-ai/DeepSeek-R1

[4] DeepSeek API docs "DeepSeek-R1 Release" (MIT, "distill & commercialize freely" framing):
https://api-docs.deepseek.com/news/news250120

[5] LocalScore "About" (what it measures + thresholds + llamafile under the hood):
https://www.localscore.ai/about

[6] LocalScore accelerator page: NVIDIA GeForce RTX 4090 (example 8B/14B LocalScore numbers):
https://www.localscore.ai/accelerator/1704

[7] LocalScore accelerator page: Apple M3 Ultra 256GB (example 8B/14B LocalScore numbers):
https://www.localscore.ai/accelerator/1359

[8] Apache License 2.0 (how to apply; include LICENSE text; NOTICE guidance):
https://www.apache.org/licenses/LICENSE-2.0

[9] Apache guidance on assembling LICENSE + NOTICE files:
https://infra.apache.org/licensing-howto.html

[10] Meta Llama 3 Community License text (redistribution requirements, "Built with Meta Llama 3", output restriction, 700M MAU clause):
https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
