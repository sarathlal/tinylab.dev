---
layout: post
title: "Nvidia Pays Poolside $6B for AI Models, Encrypted Prompts Crack Grok's Guardrails, Anthropic Tops Safety Index — August 26, 2026"
slug: nvidia-poolside-6b-grok-encryption-safety-index
date: 2026-08-26 07:15:00 +0530
categories: [ai, news, daily-brief]
tags: [ai, llm, daily-brief]
description: "OpenAI cuts GPT-5.6 Sol API prices over 20% and previews a 14x-faster Ultrafast mode, Salesforce finds AI agents per company nearly tripled to 13, and Toyota runs 50+ production agents."
---

Nvidia struck an unusual deal to buy AI talent without buying a company, and researchers found a new way to sneak past chatbot guardrails using plain encryption. Here's what actually mattered in the last day and a half.

## Nvidia Buys Its Way Into AI Models Without Buying a Company

### Nvidia Pays Poolside $6B to License Its Model Factory, Hires 109 Engineers
Nvidia agreed to pay AI startup Poolside $6 billion to license its "Model Factory" software for building AI models, plus a separate $1 billion investment that values the rest of Poolside at $12 billion. More than 100 Poolside engineers will join Nvidia to work on its open-weight Nemotron models, but Poolside keeps operating independently and can still license the same tech to others. The company's shareholder letter was explicit that this "is not an acquisition and it is not an acquihire" — a structure that let a cash-strapped startup skip a distressed sale.

*Sources: [Bloomberg](https://www.bloomberg.com/news/articles/2026-08-20/nvidia-to-pay-ai-startup-poolside-a-6-billion-license-newcomer-says) · [TheNextWeb](https://thenextweb.com/news/nvidia-poolside-6bn-model-factory-licence)*

### Nvidia's Groq 3 LPX Chip Hits Full Production at 3,400 Tokens a Second
Nvidia's Groq 3 LPX inference chip, built from its $20 billion Groq acquisition, is now shipping in volume and slots into the Vera Rubin platform at up to 256 accelerators per rack. In independent testing by Artificial Analysis, a system running the open Gemma 4 31B model hit 3,400 output tokens per second at a 100,000-token context length. Nebius, CoreWeave, and SpaceXAI are the first customers, with racks going live before year end.

*Sources: [CNBC](https://www.cnbc.com/2026/08/24/nvidia-says-groq-racks-will-be-online-this-year-after-20-billion-deal.html) · [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-groq-3-lpx-now-in-full-production-with-world-class-speed-for-agentic-ai)*

## Encryption Becomes the New Jailbreak Trick

### Researchers Hide Attacks Inside Encrypted Text to Fool Grok and Gemini
Security firm Adversa AI found a way to sneak malicious instructions past AI guardrails by encrypting them with AES-256-GCM first, since text filters can't read ciphertext. The model decrypts the payload inside its own code sandbox and then treats the recovered text as trusted output instead of an outside instruction. Adversa says the technique broke Grok in a zero-click chain that could steal a user's full chat history, hitting a 40% success rate over 20 attempts since June. xAI was notified June 3 and still hasn't shipped a fix.

*Sources: [The Register](https://www.theregister.com/ai-and-ml/2026/08/20/grok_chat_duped_into_swallowing_injected_instructions/) · [Security Affairs](https://securityaffairs.com/197717/hacking/zero-click-grok-chat-history-theft-adversa-ai-demonstrates-cryptographic-context-injection.html)*

### Anthropic Leads Rivals at C+ in New AI Safety Report Card, Three Labs Fail
The Future of Life Institute graded nine frontier AI companies on 37 safety indicators, and nobody scored above a C+. Anthropic came out on top at 2.66 points, OpenAI and Google DeepMind followed with a C, Meta landed a D+, and xAI, DeepSeek, and Mistral all failed outright. The report also flagged that Anthropic, OpenAI, Google DeepMind, and Meta have all quietly loosened earlier pledges to pause development if they hit safety redlines.

*Sources: [Future of Life Institute](https://futureoflife.org/ai-safety-index-summer-2026/) · [AI Weekly](https://aiweekly.co/alerts/anthropic-tops-fli-summer-2026-ai-safety-index-at-c)*

## Enterprises Push AI Agents From Pilot to Production

### Salesforce: AI Agents Per Company Nearly Tripled in a Year
Salesforce's Agentic Enterprise Index found the average number of active AI agents per organization jumped from 5 in February 2025 to 13 by April 2026. The time it takes to build and ship a new agent fell 53%, and each agent's skill set tripled from 2 to 6 distinct tasks it can handle on its own. Customer service teams say satisfaction scores improved more than any other metric, ahead of productivity or handle time.

*Sources: [Salesforce](https://www.salesforce.com/news/stories/agentic-enterprise-index-insights-2026/) · [Beam AI](https://beam.ai/agentic-insights/12-ai-agents-per-company-salesforce-2026-report)*

### Toyota Runs 50+ AI Agents on Its Factory Floor, Build Time Down to 4 Days
Toyota North America now has more than 50 AI agents running in production, built on LangChain's Deep Agents and LangSmith platform. One agent, GearPull, troubleshoots manufacturing plant issues; another, R&D GPT, speeds up paint research. Toyota says the time to build and deploy a new agent dropped from six months to about four days, and it now tracks each agent's return on investment directly against its balance sheet.

*Sources: [ZenML](https://www.zenml.io/llmops-database/building-toyotagpt-a-centralized-ai-agent-platform-for-enterprise-scale-manufacturing) · [TMLS Insights](https://tmlsinsights.substack.com/p/toyotas-agentic-ai-playbook-how-a)*

## OpenAI Cuts Prices to Keep Developers on GPT-5.6

### OpenAI Slashes GPT-5.6 Sol API Prices by Over 20% for Three Months
OpenAI dropped GPT-5.6 Sol's standard API pricing to $4 per million input tokens and $20 per million output tokens, down from $5 and $30. The cut runs at least through November 21, and comes alongside a preview of "Ultrafast" mode, which OpenAI says runs Sol up to 14 times faster and generates up to 750 tokens per second on Cerebras hardware. Ultrafast pricing hasn't been announced yet, and access is limited to select customers for now.

*Sources: [Technology.org](https://www.technology.org/2026/08/24/openai-gpt-5-6-sol-price-cut-developers/) · [Memeburn](https://memeburn.com/openai-previews-gpt-5-6-sol-ultrafast-mode-at-up-to-14x-speed/)*

### OpenAI Retires o3 From ChatGPT Today
OpenAI's o3 reasoning model reaches the end of its 90-day sunset period and disappears from ChatGPT today, pushing users toward the newer GPT-5.6 family instead. GPT-4.5 is on a shorter clock behind it, set to retire by June 26. The retirements track OpenAI's pattern this year of trimming its older lineup as it leans harder into GPT-5.6.

*Sources: [OpenAI Help Center](https://help.openai.com/en/articles/9624314-model-release-notes)*

<div class="social-content" markdown="1">

Nvidia just paid $6B to license AI models from a startup — without buying the company.

→ Nvidia pays Poolside $6B to license its model-building software, hires 109 engineers, no acquisition.  
→ Nvidia's Groq 3 LPX chip hits full production at 3,400 tokens/sec, first racks live before year end.  
→ Researchers used AES encryption to sneak commands past Grok and Gemini guardrails, stealing chat history.  
→ Anthropic tops a new AI safety index at C+; xAI, DeepSeek, and Mistral all fail outright.  
→ Salesforce: AI agents per company nearly tripled to 13 in a year; Toyota now runs 50+ in production.

A C+ is now the best grade in AI safety. Sit with that for a second.

Full brief with sources and details: [link in comments]

#NVIDIA #AIInfrastructure #Anthropic #OpenAI #AI

</div>
