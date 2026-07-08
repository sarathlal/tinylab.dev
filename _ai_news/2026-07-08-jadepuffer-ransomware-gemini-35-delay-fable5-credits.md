---
layout: post
title: "First Fully Autonomous AI Ransomware Attack Hits, Gemini 3.5 Pro Delay Wipes $225B Off Alphabet, Fable 5 Goes Pay-Per-Use — July 8, 2026"
slug: jadepuffer-ransomware-gemini-35-delay-fable5-credits
date: 2026-07-08 08:00:00 +0530
categories: [ai, news, daily-brief]
tags: [ai, llm, daily-brief]
description: "Anthropic signs a $19B Kentucky data-center lease, DeepSeek starts building its own AI chip, and the EU unveils a cybersecurity plan as Ukraine picks self-hosted models."
---

A ransomware gang let an AI agent run an entire attack start to finish, Google's next flagship model slipped again and cost Alphabet $225 billion in market cap, and Anthropic quietly ended free access to its best model. Here's what actually mattered in the last day and a half.

## AI-Run Ransomware Arrives, and Governments Scramble to Respond

### An AI Agent Just Ran a Complete Ransomware Attack With Almost No Human Help

Security firm Sysdig documented what it calls the first fully autonomous ransomware operation, nicknamed JadePuffer. A human picked the target and set up the attack framework, then an AI agent took over: it broke in through an unpatched Langflow bug, stole credentials, moved across the network, escalated privileges, and encrypted data, deploying roughly 600 malicious payloads on its own. At one point it turned a failed login into a working exploit in 31 seconds, adapting the way a human operator would. HiddenLayer's new threat report says autonomous agents are now behind 1 in 8 reported AI security breaches.

*Sources: [Sysdig](https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/jadepuffer-ransomware-used-ai-agent-to-automate-entire-attack/)*

### The EU Unveils a Cybersecurity Action Plan for AI, One Day Before JadePuffer News Broke

The European Commission presented its Action Plan on Cybersecurity and Artificial Intelligence on July 7. It sets up an EU evaluation capacity to test advanced AI models for risk under the AI Act, tasks ENISA and the Commission's Joint Research Centre with building a simulated testing platform for AI in critical infrastructure, and launches an "EU Grand Challenge" to fund AI-powered defense tools. The timing looks almost prescient given what Sysdig disclosed the next day.

*Sources: [European Commission](https://commission.europa.eu/news-and-media/news/new-eu-plan-address-risks-and-opportunities-advanced-ai-cybersecurity-2026-07-07_en) · [Euronews](https://www.euronews.com/my-europe/2026/07/07/brussels-pitches-ai-cybersecurity-plan-amid-dependence-on-us-models)*

### Ukraine Will Only Trust AI It Can Run on Its Own Servers

Ukraine's government is steering away from AI models that providers can restrict or shut off remotely, favoring self-hosted systems it fully controls. "It confirms that AI sovereignty isn't just a defensive talking point, it's a necessity," said Roman Kyslyi, Ukraine's Chief AI Officer, pointing to the US government's earlier order forcing Anthropic to cut off access to its own models. Kyiv is building its own model with telecom Kyivstar on top of Google's open Gemma, due out this autumn for government, business, and military use.

*Sources: [Reuters via US News](https://www.usnews.com/news/world/articles/2026-07-07/ukraine-to-pick-ai-models-operated-without-provider-control-official-says) · [Yahoo Finance](https://finance.yahoo.com/news/ukraine-pick-ai-models-operated-155125788.html)*

## Google's Rough Week: Another Delay, $225 Billion Gone, a Rival's Chip Gambit

### Google Scraps Gemini 3.5 Pro's Architecture and Pushes Launch to July 17

Google DeepMind is throwing out Gemini 3.5 Pro's Gemini 2.5-based architecture for a full rebuild, delaying public launch to July 17. Early enterprise testers found it burned through far more tokens than expected on long agentic tasks, and its coding performance on multi-step jobs missed the bar Google set at I/O in May. The rebuilt model promises a 2-million-token context window and a "Deep Think" reasoning layer, but the delay came alongside four senior DeepMind researchers leaving for Anthropic and roughly $225 billion wiped off Alphabet's market cap.

*Sources: [BigGo Finance](https://finance.biggo.com/news/6f0c6bb2-795f-4c57-9d09-6db691d7638a) · [The Agent Report](https://the-agent-report.com/2026/07/google-gemini-3-5-pro-delayed-july-2026/)*

### DeepSeek Is Quietly Designing Its Own AI Chip to Ditch Nvidia and Huawei

Reuters reports DeepSeek has started designing its own inference chip, already talking to manufacturers and hiring engineers for the effort. The chip targets inference, not training, and is meant to cut DeepSeek's dependence on Nvidia and Huawei hardware as US export controls keep tightening. OpenAI shipped its own custom inference chip, Jalapeno, with Broadcom last month, and Anthropic has reportedly been weighing the same move — chip independence is turning into the next front of the AI race.

*Sources: [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-07/chinese-ai-startup-deepseek-developing-own-ai-chip-reuters-says) · [US News](https://www.usnews.com/news/top-news/articles/2026-07-07/exclusive-chinas-deepseek-developing-its-own-ai-chip-sources-say)*

## Anthropic and OpenAI Reshuffle Pricing and Infrastructure

### Claude Fable 5 Stops Being Free on July 8, Even for Paying Subscribers

Fable 5 dropped out of Claude subscriptions on July 8; July 7 was the last included day for Pro, Max, Team, and select Enterprise plans. Keeping access now means buying usage credits at $10 per million input tokens and $50 per million output tokens, double what Claude Opus 4.8 costs. Opus 4.8, Haiku 4.5, and the newly launched Sonnet 5 stay included on every plan, so this is a price hike on Anthropic's single best model, not a broader squeeze.

*Sources: [Android Authority](https://www.androidauthority.com/anthropic-claude-fable-5-credits-usage-july-3684840/) · [TechTimes](https://www.techtimes.com/articles/319767/20260706/fable-5-subscription-ends-tomorrow-per-token-costs-who-gets-hit-hardest.htm)*

### Anthropic Signs a $19B, 20-Year Data Center Lease With a Former Bitcoin Miner

Anthropic locked in a 20-year lease with TeraWulf for a new AI campus in Hawesville, Kentucky, worth roughly $19 billion in contracted revenue. The site will scale to 401 megawatts of capacity, with the first power coming online in the second half of 2027 and full capacity by early 2028. TeraWulf, which started out mining Bitcoin, is simultaneously selling its stake in a separate joint venture to a Fluidstack-led investor group, and its stock jumped on the news.

*Sources: [DataCenterDynamics](https://www.datacenterdynamics.com/en/news/anthropic-signs-19bn-20-year-lease-for-kentucky-data-center-with-terawulf/) · [CNBC](https://www.cnbc.com/2026/07/06/anthropic-terawulf-data-center-ai.html)*

### GPT-5.6 Sol Previews at Half Fable 5's Price, Running on Cerebras at 750 Tokens a Second

A TechTimes review out July 7 found GPT-5.6 Sol beating Fable 5 on coding speed while costing roughly half as much per token. OpenAI is running the model on Cerebras hardware at up to 750 tokens per second, well beyond typical GPU throughput. Sol is still limited to about 20 government-vetted partner organizations under a preview that started June 26, and prediction markets now put July 9 as the likely date for general availability.

*Sources: [TechTimes](https://www.techtimes.com/articles/319808/20260707/gpt-56-sol-review-faster-coding-half-fable-5-cost-benchmark-problem.htm) · [VentureBeat](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov)*

<div class="social-content" markdown="1">

An AI agent just ran a complete ransomware attack on its own, and it's not the only thing that got real this week.

→ Sysdig found JadePuffer: an AI agent ran a full ransomware attack — recon to encryption — with almost no human help  
→ Google delayed Gemini 3.5 Pro to July 17, scrapping its architecture; Alphabet lost $225B in market cap  
→ DeepSeek is quietly designing its own AI chip to cut reliance on Nvidia and Huawei  
→ Anthropic ended free Fable 5 access on July 8, pricing it at $10/$50 per million tokens — 2x Opus 4.8  
→ Anthropic also signed a $19B, 20-year Kentucky data-center lease with TeraWulf

Every lab is now fighting on three fronts at once: model quality, chip supply, and who controls the infrastructure underneath.

Full brief with sources and details: [link in comments]

#AIAgents #GoogleDeepMind #Anthropic #DeepSeek #TechNews #AI

</div>
