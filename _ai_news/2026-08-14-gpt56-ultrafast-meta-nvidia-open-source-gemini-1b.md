---
layout: post
title: "OpenAI's GPT-5.6 Sol Hits 14x Speed With Cerebras, Meta and Nvidia Open-Source Models, Gemini Tops 1B Users — August 14, 2026"
slug: gpt56-ultrafast-meta-nvidia-open-source-gemini-1b
date: 2026-08-14 08:00:00 +0530
categories: [ai, news, daily-brief]
tags: [ai, llm, daily-brief]
description: "DeepSeek ships its 1.6T-parameter V4 Pro under an MIT license, Anthropic makes Claude Code's auto mode the default, Cognition talks a $40B valuation, and Vantage Data Centers eyes a $100B IPO."
---

OpenAI made its flagship model 14 times faster, Meta and Nvidia both open-sourced models to chase China, and Gemini quietly crossed a billion monthly users. Here's what actually mattered in AI over the last day and a half.

## OpenAI's GPT-5.6 Sol Hits 14x Speed, DeepSeek Ships Its Flagship

### OpenAI and Cerebras Launch "Ultrafast" Mode, 14x Faster Than Standard

OpenAI's new Ultrafast mode pushes GPT-5.6 Sol to 750 output tokens per second, 14 times the standard mode's roughly 53 tokens/s, with no drop in quality. Cerebras' wafer-scale chips keep all 44GB of the model's weights on-chip, skipping the memory-bandwidth bottleneck that slows regular GPU inference. It's live now in limited preview on OpenAI's API, and on GDP-Val, a benchmark of real knowledge work like legal briefs and financial models, it cut task time 5.6x.

*Sources: [TechCrunch](https://techcrunch.com/2026/08/13/openai-introduces-ultrafast-a-new-mode-that-makes-gpt-5-6-sol-work-at-14x-the-speed/) · [OpenAI](https://openai.com/index/previewing-ultrafast/)*

### DeepSeek's V4 Pro Leaves Preview, Undercuts on Price

DeepSeek's V4 Pro 0813 exited a four-month preview this week: a 1.6-trillion-parameter model with 49 billion active per token, released under the permissive MIT license. It struggled on some general benchmarks but jumped hard on security-flavored ones — CyberGym went from 52.7 to 83.3, Terminal-Bench 2.1 from 72.1 to 87.9. Output costs $0.87 per million tokens for now, though DeepSeek says a "significant" price hike is coming.

*Sources: [Unite.AI](https://www.unite.ai/deepseek-ships-v4-pro-as-its-flagship-model-leaves-preview/) · [South China Morning Post](https://www.scmp.com/tech/big-tech/article/3363895/deepseeks-updated-v4-pro-ai-model-struggles-benchmarks-shines-cybersecurity)*

## Meta and Nvidia Go Open-Weight to Counter China

### Meta Opens Muse Glimmer, Reverses Course on Muse Spark 1.2

Meta released Muse Glimmer's weights under Apache 2.0 on August 10: a 30B dense multimodal model compressed under 20GB, small enough to run on a laptop. Zuckerberg also said Meta will open the weights for Muse Spark 1.2, its bigger 1M-context model, reversing what had been a proprietary strategy for the Muse line. The move comes as Chinese labs like DeepSeek and Qwen dominate the open-weight leaderboard.

*Sources: [CNBC](https://www.cnbc.com/2026/08/10/meta-muse-glimmer-open-weight-ai.html) · [Constellation Research](https://www.constellationr.com/insights/news/meta-releases-open-weight-muse-glimmer-model-open-muse-spark-12-tap)*

### Nvidia Ships Its First Open-Source Model, Nemotron 3.5 Lightning

Nvidia's Nemotron 3.5 Lightning is a 30B mixture-of-experts model with just 3B active parameters, light enough to run on a single consumer GPU. Nvidia says it's up to 4x faster than comparable models, cutting task completion time 30%. It shipped under the permissive OpenMDW-1.1 license with training data and recipes included, alongside NeMo Switchyard, a router that sends each step of an agent workflow to the cheapest model that can handle it.

*Sources: [CNBC](https://www.cnbc.com/2026/08/11/nvidia-releases-nemotron-3point5-lightning-open-source-ai-model-.html) · [MarkTechPost](https://www.marktechpost.com/2026/08/11/nvidia-ai-releases-nemotron-3-5-lightning-and-nemo-switchyard/)*

## AI Coding Agents Get Bolder and Pricier

### Claude Code Turns Auto Mode On by Default

Starting today, new Claude Code sessions on Pro, Max, and Team plans default to "auto mode," where Claude acts without stopping for approval at every step. It still pauses for anything "irreversible, destructive, or aimed outside your environment," and any default a user or org already set stays in place. It's the clearest signal yet that Anthropic sees step-by-step approval as the exception now, not the rule.

*Sources: [TechCrunch](https://techcrunch.com/2026/08/09/anthropic-is-turning-claude-codes-auto-mode-on-by-default/) · [Digital Applied](https://www.digitalapplied.com/blog/claude-code-auto-mode-default-permission-model-shift)*

### Devin-Maker Cognition in Talks at $40B, Up From $26B in May

Cognition, maker of the AI coding agent Devin, is in early talks to raise more than $1 billion at a $40 billion valuation. That's up from $26 billion just three months ago, tied to reports the company has hit a $1 billion annualized revenue run rate. At its May raise, co-founder Scott Wu said enterprise usage of Devin had grown 50% month-over-month for six straight months.

*Sources: [TechCrunch](https://techcrunch.com/2026/08/12/ai-coding-startup-cognition-reportedly-already-in-talks-to-raise-at-40b-valuation/) · [Bloomberg](https://www.bloomberg.com/news/articles/2026-08-12/ai-startup-cognition-in-new-funding-talks-at-40-billion-value)*

## Gemini Hits a Billion Users, Data Center Bets Get Bigger

### Gemini Crosses 1 Billion Monthly Users, Google's Fastest-Growing Product Ever

Google's Gemini app hit 1 billion monthly active users on August 11, up from 750 million earlier this year and 950 million in July. That's the fastest climb to a billion of any Google product in the company's history. It's not quite parity with ChatGPT, though: OpenAI cleared 1 billion monthly users three months earlier and hit the harder weekly-user mark back in July.

*Sources: [TechCrunch](https://techcrunch.com/2026/08/11/googles-gemini-app-surges-to-one-billion-users/) · [Forbes](https://www.forbes.com/sites/antoniopequenoiv/2026/08/11/gemini-becomes-googles-fastest-growing-product-ever-after-hitting-1-billion-monthly-users/)*

### Vantage Data Centers Weighs $100B IPO, Would Be Largest Ever

Vantage Data Centers, backed by Silver Lake and DigitalBridge, is exploring an IPO or sale that could value it around $100 billion and raise roughly $10 billion. No formal process has launched yet, and the timing, size, and structure could still change. If it happens, it would be the largest data center IPO on record, ahead of rival Switch, which filed for a $50 billion listing earlier this month.

*Sources: [CTV News (Reuters)](https://www.ctvnews.ca/business/article/vantage-data-centers-explores-ipo-at-us100-billion-valuation-or-sale-sources-say/) · [BNN Bloomberg](https://www.bnnbloomberg.ca/business/company-news/2026/08/13/vantage-data-centers-explores-ipo-at-us100-billion-valuation-or-sale-sources-say/)*

<div class="social-content" markdown="1">

OpenAI just made its flagship model 14x faster — and that's not even the biggest AI story of the week.

→ OpenAI's Ultrafast mode runs GPT-5.6 Sol at 750 tokens/sec, 14x standard speed, zero quality loss  
→ Meta open-sourced Muse Glimmer and will open Muse Spark 1.2, reversing its proprietary bet  
→ Nvidia shipped its first open-source model, Nemotron 3.5 Lightning, runs on one GPU  
→ DeepSeek's 1.6T-parameter V4 Pro left preview under an MIT license, undercutting on price  
→ Gemini crossed 1 billion monthly users, Google's fastest-growing product ever

Three US labs went open-weight in a single week. That's not a coincidence — it's a response to China's lead.

Full brief with sources and details: [link in comments]

#OpenSourceAI #OpenAI #Meta #NVIDIA #DeepSeek #AI

</div>
