---
layout: post
title: "Microsoft's MAI-Thinking-1 Breaks from OpenAI, Anthropic IPO at $965B Valuation, Devin Coding Agent Raises $1B — June 3, 2026"
slug: microsoft-mai-thinking-anthropic-ipo-cognition-devin-1b
date: 2026-06-03 18:00:00 +0530
categories: [ai, news, daily-brief]
tags: [ai, llm, daily-brief]
description: "Google Gemini 3.5 Flash hits GA beating last year's Pro model, Colorado rewrites its AI law delaying enforcement to 2027, and DeepMind's Co-Scientist deploys to all 17 DOE National Labs."
---

Microsoft Build 2026 dominated Tuesday's news, delivering the company's first in-house reasoning model and announcing that GitHub Copilot cuts its OpenAI dependency by August. Alongside that, Anthropic filed its IPO paperwork and Cognition's Devin agent landed a $1 billion raise.

## Microsoft Declares Model Independence at Build 2026

### MAI-Thinking-1: Microsoft's First In-House Reasoning Model

Microsoft's first home-grown reasoning model, MAI-Thinking-1, scored 97.0% on AIME 2025 at Build 2026 on June 2 — matching Claude Sonnet 4.6 on SWE-Bench Pro while costing up to 10x less than GPT-5.5. The 35-billion-active-parameter mixture-of-experts model was trained entirely on commercially licensed data, with no distillation from OpenAI or any third-party model. It's in private preview on Microsoft Foundry starting today.

*Sources: [Microsoft AI](https://microsoft.ai/news/introducing-mai-thinking-1/) · [Neowin](https://www.neowin.net/news/microsoft-unveils-mai-thinking-1-reasoning-and-mai-code-1-flash-models/)*

### Project Polaris Replaces GPT-4 Turbo in GitHub Copilot Starting August

Microsoft also announced Project Polaris, its own mixture-of-experts coding model, which replaces GPT-4 Turbo as the default engine for all GitHub Copilot subscribers in August 2026. It outperforms GPT-4 Turbo on HumanEval and MBPP, with bigger gains in lower-resource languages like Rust and Haskell. Subscribers get automatic migration and an optional 90-day fallback to the old model.

*Sources: [TechTimes](https://www.techtimes.com/articles/317596/20260602/github-copilot-replaces-gpt-4-project-polaris-ships-multi-agent-vs-code-build.htm) · [AI Weekly](https://aiweekly.co/alerts/microsoft-targets-claude-code-with-project-polaris)*

### Windows Agent Framework Goes MIT Open-Source; Azure Agent Mesh Ships

Microsoft open-sourced Windows Agent Framework 1.0 under the MIT license and launched Azure Agent Mesh, a runtime for federated multi-agent execution across clouds and devices. VS Code now ships multi-agent Copilot support, letting it spawn parallel subagents for linting, testing, documentation, and security review simultaneously rather than sequentially.

*Sources: [WindowsNews](https://windowsnews.ai/article/microsoft-build-2026-homegrown-ai-models-to-power-github-copilot.420887) · [ChatForest](https://chatforest.com/builders-log/microsoft-build-2026-recap-windows-agent-platform-project-polaris-copilot-workspace/)*

## The AI IPO Race Is On

### Anthropic Files Confidential S-1 at a $965B Valuation

Anthropic filed a confidential S-1 with the SEC on June 1, four days after closing a $65 billion Series H — led by Altimeter, Dragoneer, Greenoaks, and Sequoia — that pushed its post-money valuation to $965 billion, past OpenAI's $852 billion for the first time. The filing kicks off a public listing countdown, though no official timeline has been confirmed.

*Sources: [US News](https://www.usnews.com/news/top-news/articles/2026-06-01/ai-giant-anthropic-confidentially-files-for-us-ipo) · [Bloomberg](https://www.bloomberg.com/news/articles/2026-06-01/anthropic-s-first-mover-ipo-edge-set-to-widen-lead-over-openai)*

### OpenAI Targets September IPO with Goldman Sachs and Morgan Stanley

OpenAI is drafting its own S-1 with Goldman Sachs and Morgan Stanley, targeting a September 2026 listing. The company closed a $122 billion round in March at an $852 billion valuation. Enterprise now accounts for more than 40% of OpenAI's revenue and is on pace to match its consumer business by year-end.

*Sources: [Bloomberg](https://www.bloomberg.com/news/articles/2026-06-01/can-openai-and-anthropic-ipos-live-up-to-expectations)*

### Cognition's Devin Raises $1B at $26B — 90% of Its Own Code Now AI-Written

Cognition closed over $1 billion led by Lux Capital, General Catalyst, and 8VC, lifting Devin's post-money valuation to $26 billion — up from $10 billion just eight months ago. Annualized revenue runs at $492 million with 50% month-over-month growth for the past six months. Customers include Mercedes-Benz, NASA, Goldman Sachs, and Santander, and the company says 90% of its own codebase is now written by Devin.

*Sources: [TechCrunch](https://techcrunch.com/2026/05/27/ai-coding-startup-cognition-raises-1b-at-25b-pre-money-valuation/) · [The Next Web](https://thenextweb.com/news/cognition-just-raised-1-billion-at-a-26-billion-valuation-and-90-of-its-own-code-is-written-by-its-ai)*

## Google Pushes Gemini Deeper Into Science and Enterprise

### Gemini 3.5 Flash Hits GA, Beating Last Year's Pro on Coding and Agents

Gemini 3.5 Flash is now generally available at $1.50 per million input tokens — three times the price of the previous Flash but 40% cheaper than Gemini 3.1 Pro, which it outperforms on coding and agentic benchmarks. It scores 76.2% on Terminal-Bench 2.1 and runs 4x faster than comparable frontier models. Gemini 3.5 Pro is expected next month.

*Sources: [MarkTechPost](https://www.marktechpost.com/2026/05/20/google-introduces-gemini-3-5-flash-at-i-o-2026-a-faster-and-cheaper-model-for-ai-agents-and-coding/) · [OpenRouter](https://openrouter.ai/google/gemini-3.5-flash)*

### DeepMind's Co-Scientist Lands in Nature, Then Deploys to All 17 DOE Labs

Google DeepMind published a formal paper on Co-Scientist in Nature on May 19, then announced deployment to all 17 US Department of Energy National Labs as part of the Genesis Mission. The multi-agent Gemini system compresses scientific hypothesis generation from years to days. A Calico Life Sciences team confirmed a novel Co-Scientist hypothesis about the integrated stress response in aging biology.

*Sources: [Nature](https://www.nature.com/articles/s41586-026-10644-y) · [Google DeepMind](https://deepmind.google/blog/google-deepmind-supports-us-department-of-energy-on-genesis/)*

### Google Launches Gemini Spark and CodeMender for Enterprise Customers

Google's Gemini Enterprise Agent Platform now includes Gemini Spark — a 24/7 personal agent for Google Workspace — and CodeMender, a security agent that finds, tests, and applies code patches autonomously. A new Managed Agents API lets developers spin up custom agents in Google-hosted secure environments with a single API call. Most features roll out to Gemini Enterprise customers over the coming weeks.

*Sources: [Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/innovations-from-google-io-26-on-google-cloud)*

## State AI Laws in Flux

### Colorado Rewrites Its AI Act, Pushes Enforcement Back to January 2027

Colorado Governor Jared Polis signed a replacement AI law (SB 26-189) on May 14, repealing the original Colorado AI Act just weeks before its June 30 effective date. The new law substantially reduces obligations on employers and developers and won't take effect until January 1, 2027. Violations are treated as deceptive trade practices under Colorado consumer law, carrying up to $20,000 per violation.

*Sources: [Ropes & Gray](https://www.ropesgray.com/en/insights/alerts/2026/05/colorado-scales-back-ai-law-with-targeted-implications-for-health-care) · [Norton Rose Fulbright](https://www.nortonrosefulbright.com/en-us/knowledge/publications/18733d31/colorado-enacts-revised-ai-law)*

### White House Pushes Congress to Preempt State AI Laws

The White House's March 2026 National AI Policy Framework recommends that Congress preempt state AI laws that "impose undue burdens," aiming for a single federal standard. At least 20 states have active AI legislation in 2026, including California laws that took effect January 1 requiring frontier AI developers to publish risk frameworks and training data summaries. The federal push sets up a direct collision with state-level momentum.

*Sources: [Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/03/white-house-releases-a-national-policy-framework-for-artificial) · [Verifywise](https://verifywise.ai/blog/state-of-ai-governance-regulations-united-states-2026)*

<div class="social-content" markdown="1">

Microsoft just shipped its first reasoning model — trained without a single line of OpenAI data.

→ MAI-Thinking-1 scores 97% on AIME 2025, matches Claude Sonnet 4.6 on SWE-Bench, costs 10x less than GPT-5.5  
→ Project Polaris replaces GPT-4 Turbo in GitHub Copilot for millions of devs starting August  
→ Anthropic filed a confidential S-1 at $965B valuation — past OpenAI for the first time ever  
→ Cognition's Devin hit $492M ARR and raised $1B at $26B; 90% of its own code is AI-written  
→ Google's Co-Scientist published in Nature and is now running across all 17 US DOE National Labs

Three major AI labs shipping their own reasoning models within 90 days looks less like competition and more like a structural shift in who controls the stack.

Full brief with sources and details: [link in comments]

#Microsoft #Anthropic #AIStartups #LLM #AI

</div>
