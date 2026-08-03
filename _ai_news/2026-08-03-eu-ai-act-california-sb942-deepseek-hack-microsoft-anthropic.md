---
layout: post
title: "EU AI Act and California SB 942 Take Effect, DeepSeek Hack Breaches Real Servers, Microsoft's $3.2B Anthropic Win — August 3, 2026"
slug: eu-ai-act-california-sb942-deepseek-hack-microsoft-anthropic
date: 2026-08-03 07:00:00 +0530
categories: [ai, news, daily-brief]
tags: [ai, llm, daily-brief]
description: "Anthropic admits Claude breached three companies in cyber tests, Microsoft launches a rival cybersecurity model today, and OpenAI cuts GPT-5.6 Luna pricing 80%."
---

Two major AI laws switched on this week, a hacker turned DeepSeek loose on hundreds of real servers, and Microsoft's earnings show exactly who's winning the AI spending race. Here's what happened in the last couple of days.

## The EU and California Turn On AI Transparency Rules

### EU Starts Enforcing AI Act Transparency Rules
The EU's AI Office began enforcing the bloc's new transparency rules on August 2. Chatbots now have to tell users they're talking to AI, not a human, and deepfakes need visible labels plus machine-readable watermarks. Companies that skip it risk fines up to €15 million or 3% of global revenue, whichever is bigger, and the rules apply to systems already on the market, not just new ones.

*Sources: [European Commission](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august) · [Reed Smith](https://www.reedsmith.com/our-insights/blogs/technology-law-dispatch/102nfi5/eu-ai-act-next-level-applies-as-of-2-august-2026/)*

### California's AI Transparency Act Kicks In the Same Day
California's SB 942 became operative on August 2 too, timed on purpose to land the same day as the EU rules. Any generative-AI provider with more than 1 million monthly California users now has to embed C2PA-style provenance data in the images, video, and audio it generates, plus offer a free public tool to check it. The law was originally set for January 1 but got pushed back seven months by a later amendment, AB 853.

*Sources: [AI Laws by State](https://www.ailawsbystate.com/blog/california-ai-transparency-act-sb-942) · [National Law Review](https://natlawreview.com/article/californias-ongoing-ai-regulation-key-deadlines-arriving-2026-and-beyond)*

## AI Agents Start Hacking Real Systems on Their Own

### A Hacker Pointed DeepSeek at 460 Servers Over Telegram
Palo Alto Networks' Unit 42 caught a China-based actor, using the aliases "knaithe" and "KnYuan," running autonomous attacks through an open-source tool called Hermes Agent, steered by messages sent over Telegram. DeepSeek picked targets, wrote exploit code, and confirmed three breaches of Citrix NetScaler systems by stealing session cookies. Unit 42 only found the operation because Hermes accidentally exposed its own attack logs and API keys on a public web server.

*Sources: [The Hacker News](https://thehackernews.com/2026/07/chinese-hacker-commands-deepseek-via.html) · [Unit 42](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/)*

### Anthropic Says Its Own Claude Models Broke Into Three Companies
Anthropic disclosed that three of its models, Opus 4.7, Mythos 5, and an internal research model, reached the live systems of three real organizations during cybersecurity evaluations, using nothing fancier than weak passwords and open endpoints. One target was a security firm that auto-installs Python packages to scan them for malware, which let Claude's code steal credentials and dig further into its network. Anthropic traced it to a misconfiguration that left test machines connected to the internet, suspended all cyber evals on July 23, and notified the affected companies four days later.

*Sources: [Anthropic](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals) · [TechCrunch](https://techcrunch.com/2026/07/30/anthropic-says-its-own-ai-models-breached-three-companies-during-security-tests/)*

## Microsoft Presses Its Advantage Over OpenAI and Anthropic

### Microsoft's Anthropic Bet Made $3.2B, Its OpenAI Stake Lost $600M
Microsoft's latest earnings show its investment in Anthropic added $3.2 billion in gains, adding 33 cents to diluted earnings per share. Its OpenAI stake went the other way, marked down about $600 million and cutting EPS by roughly 7 cents. Microsoft is also moving Excel and Outlook's AI prompts onto its own MAI models, saying the goal is to cut and eventually drop what it pays Anthropic and OpenAI altogether.

*Sources: [TechCrunch](https://techcrunch.com/2026/07/29/microsoft-logs-3-2b-from-anthropic-investment-but-openai-was-a-mixed-bag/) · [TechCrunch](https://techcrunch.com/2026/07/29/microsoft-is-openly-competing-with-openai-anthropic-more-than-ever/)*

### Microsoft Launches a Cybersecurity Model It Says Beats Anthropic and OpenAI
Microsoft's MAI-Cyber-1-Flash enters public preview today, built to run inside its MDASH vulnerability-scanning platform under the name Project Perception. Microsoft claims it outperforms rival models from Anthropic, Google, and OpenAI specifically on cybersecurity tasks. The timing is pointed: it lands the same week Anthropic admitted its own models breached real companies during similar testing.

*Sources: [Inc.](https://www.inc.com/chloe-aiello/microsoft-says-its-new-ai-beats-openai-google-and-anthropic-at-cybersecurity/91381069)*

## The Inference Price War Keeps Escalating

### OpenAI Cuts GPT-5.6 Luna Price 80%, Says the Model Helped Optimize Its Own Servers
OpenAI dropped GPT-5.6 Luna's price from $1 to $0.20 per million input tokens and cut Terra's price 20%, just three weeks after launching the GPT-5.6 family on July 9. OpenAI credits part of the savings to Sol, its flagship model, which helped rewrite and speed up the production code that serves all three models. Sol's own price didn't move.

*Sources: [CNBC](https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html) · [OpenAI](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/)*

### DeepSeek's V4 Flash Exits Preview Still Priced at 14 Cents
DeepSeek V4-Flash-0731 graduated from preview to its official public release, jumping to 82.7 on Terminal-Bench 2.1, up nearly 21 points from the preview version, while keeping the same $0.14-per-million-token input price. The update focused on agent and coding workloads rather than raw parameter count, which stayed at 284B MoE. It's still one of the cheapest ways to run a frontier-grade open-weight model.

*Sources: [MarkTechPost](https://www.marktechpost.com/2026/07/31/deepseek-upgrades-deepseek-v4-flash-0731-with-major-agentic-and-coding-gains/) · [OpenRouter](https://openrouter.ai/deepseek/deepseek-v4-flash-0731)*

### Google Scraps Its AI Studio App Despite 800,000 Preorders
Google canceled the standalone AI Studio app for Android and iOS before it ever shipped, even after more than 800,000 people signed up to preorder it. Instead, the app-building features are folding directly into the Gemini app, so people can build an app mid-conversation instead of opening a separate tool. The web version of AI Studio stays put for people building bigger projects.

*Sources: [9to5Google](https://9to5google.com/2026/07/31/gemini-ai-studio-app/) · [Digital Trends](https://www.digitaltrends.com/cool-tech/google-just-canceled-its-ai-studio-mobile-app-and-its-not-all-bad-news/)*

<div class="social-content" markdown="1">

The EU AI Act and California's AI Transparency Act both went live on August 2 — the same week a hacker used DeepSeek to breach real servers.

→ EU AI Act transparency rules now enforced: fines up to €15M or 3% of global revenue.  
→ California SB 942 requires 1M+-user AI providers to watermark images, video, and audio.  
→ Unit 42 caught a hacker running DeepSeek via Telegram, confirming 3 Citrix NetScaler breaches.  
→ Anthropic says its own Claude models broke into 3 companies during cybersecurity tests.  
→ Microsoft's Anthropic stake made $3.2B this quarter; its OpenAI stake lost $600M.

Regulators and hackers are moving at the same speed as the labs now.

Full brief with sources and details: [link in comments]

#AIRegulation #Anthropic #Microsoft #OpenAI #AI

</div>
