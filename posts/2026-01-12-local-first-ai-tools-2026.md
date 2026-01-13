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

The Qwen3 series represents the current state of the art for open-source local AI. Six dense models are open-weighted under Apache 2.0 license: Qwen3-32B, Qwen3-14B, Qwen3-8B, Qwen3-4B, Qwen3-1.7B, and Qwen3-0.6B. The Apache 2.0 license means unrestricted commercial use—no "Built with X" branding requirements, no downstream restrictions.

The overall performance of Qwen3 dense base models matches that of Qwen2.5 base models with more parameters. For instance, Qwen3-1.7B/4B/8B/14B/32B-Base performs comparably to Qwen2.5-3B/7B/14B/32B/72B-Base, respectively. That's roughly 50% density improvement—you get similar quality in half the size.

| Model | Size | Good For | Hardware Needed |
|-------|------|----------|-----------------|
| **Qwen3 0.6B** | ~400MB | Mobile, edge devices, Raspberry Pi | Any device |
| **Qwen3 1.7B** | ~1GB | Quick queries, learning, getting started | 4GB RAM |
| **Qwen3 4B** | ~2.5GB | Daily tasks, coding help, chat | 8GB RAM |
| **Qwen3 8B** | ~5GB | General use, reasoning, coding | 16GB RAM |
| **Qwen3 14B** | ~9GB | Complex tasks, research, near-cloud quality | 16-32GB RAM |
| **Qwen3 32B** | ~20GB | Frontier-level reasoning, creative work | 32-64GB RAM |
| **DeepSeek-R1-Distill 14B** | ~9GB | Deep reasoning, math, research | 16-32GB RAM |
| **Qwen3-30B-A3B** (MoE) | ~20GB | 30B total, 3B active—excellent efficiency | 32GB RAM |

Qwen3-8B runs smoothly on laptops with 8–12GB VRAM (MacBook M3 Pro, RTX 4070 mobile). It performs competitively with larger models like Gemma-2-27B and Phi-4-14B on current benchmarks.

Qwen3-14B rivals Qwen2.5-32B in efficiency. Quantized to Q4_0, it runs well on mobile devices.

**My daily drivers:** Qwen3 8B and 14B for most tasks. DeepSeek-R1 distillations for research and deep reasoning. For workshops at the Baltimore AI Producers Lab, I keep Qwen3 0.6B-4B loaded so families can see what runs on *their* hardware—phones, old laptops, Raspberry Pis.

**Why I moved away from Meta's Llama:** The licensing. The Qwen license is far more permissive than Llama. When you finetune a model built with Qwen, you can choose your license and add "built with Qwen" to the model documentation—but it's optional. DeepSeek ships under MIT with zero downstream obligations. For teaching families to build tools they own forever, license simplicity matters.

### The Interface Layer

For my work, I'm primarily in the terminal with llama.cpp or building custom harnesses with FastAPI + HTMX. **EduPilot** is a customized deployment for Maryland educators, giving teachers access to AI without sending student data to third parties.

For family setups and workshops, visual interfaces help—LM Studio for beginners who prefer native apps, or custom web interfaces for multi-user households.

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

Here's what actually runs local AI in 2026:

### Raspberry Pi 5 (8GB): $80-100
- **Models**: Models under 7 billion parameters work well. Qwen3 0.6B-1.7B, Gemma3 1B.
- **Speed**: 5-15 tokens/second
- **Use case**: Always-on family chat interface, edge device, learning platform
- **Note**: At minimum, you'll need a Raspberry Pi 5 with 8GB of RAM. 64-bit OS required.

### Any Laptop from 2020+ with 8GB RAM: $0 (what you have)
- **Models**: Qwen3 1.7B-4B (Q4 quantization)
- **Speed**: 15-30 tokens/second
- **Use case**: Getting started, quick queries, learning

### Practical Family Server: 16GB RAM System: $400-800 (used ThinkPad or Mac Mini)
- **Models**: Qwen3 8B (Q4_K_M quantization)
- **Speed**: 20-30+ tokens/sec depending on hardware
- **Use case**: Daily driver, homework help, general assistant

### Power User: 32GB+ RAM or GPU with 12GB+ VRAM: $1,500-2,500
- **Models**: Qwen3 14B-32B, DeepSeek-R1-Distill
- **Speed**: 20-40 tokens/second
- **Use case**: Near-cloud quality, research, production

### Workshop Powerhouse: Mac Studio M3 Ultra (256GB Unified Memory): ~$8,000
- **Models**: Everything. Qwen3-72B at full precision. DeepSeek-R1 full 671B (quantized). Multiple 32B models simultaneously.
- **Speed**: 40-80+ tokens/second on 70B models
- **Use case**: Multi-family workshops, running frontier-class models locally, serving dozens of concurrent users
- **Why it matters**: This is datacenter capability on a desktop. 256GB unified memory means no GPU memory limits. One machine serves an entire workshop. One machine runs what required a server rack four years ago.

The rule of thumb: 8GB of RAM to run the 7B models, 16GB to run the 13B models, and 32GB to run the 33B models. Quantization (Q4_K_M) cuts memory requirements by ~75% while maintaining quality.

---

## What Changed My Mind

In 2022, I thought local AI was a hobby. Something for tinkerers with more time than sense.

In 2026, I see it as essential infrastructure—like having your own backup power or water filter.

**Quality is catching up—especially with fine-tuning and specific data for specific tasks with the right harness.** Local models went from "amusing" to "actually useful" to "genuinely good." DeepSeek-R1 reasoning approaches frontier models. Qwen vision handles document analysis. A 4B dense model being competitive with much larger models is remarkable.

**Hardware requirements dropped.** A laptop with 16GB RAM runs genuinely useful models. A Raspberry Pi 5 (8GB, $80) can host a family chat interface. A four-year-old laptop is enough for starting out with local AI—Qwen3 4B runs on basically anything modern.

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
