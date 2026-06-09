---
layout: post
title: "Anthropic Files S-1 at $965B, Microsoft Builds 7 In-House AI Models, ChatGPT Gets Dreaming V3 Memory — June 6, 2026"
slug: anthropic-s1-965b-microsoft-mai-dreaming-v3
date: 2026-06-06 10:00:00 +0530
categories: [ai, news, daily-brief]
tags: [ai, llm, daily-brief]
description: "Alphabet raises $84.75B for AI compute with a $10B Berkshire bet, Trump signs a 30-day voluntary AI model review order, and DeepSeek V4 Pro's 1.6T-parameter open model matches GPT-5.5."
---

Two of the biggest capital events in AI history landed within 24 hours of each other this week. At the same time, three major labs shipped significant product updates — and the open-weights race is officially at the frontier.

## Two Historic Capital Raises Land in 24 Hours

### Anthropic Files Confidential S-1, Valued at $965B

Anthropic submitted a draft S-1 to the SEC on June 1, four days after closing a $65B Series H at a $965B post-money valuation — making it the first AI lab to surpass OpenAI in private market value. The filing doesn't set an IPO date; timing depends on market conditions after the SEC review. Roughly 80% of Anthropic's revenue comes from enterprise API contracts and cloud-provider deals, which is what Wall Street will price.

*Sources: [Anthropic](https://www.anthropic.com/news/confidential-draft-s1-sec) · [NPR](https://www.npr.org/2026/06/01/nx-s1-5843199/anthropic-ipo-filing-ai-large) · [CNBC](https://www.cnbc.com/2026/06/01/anthropic-ipo-s1-prospectus.html)*

### Alphabet Raises $84.75B for AI Infrastructure — Berkshire Commits $10B

Alphabet launched an $80B equity offering on June 1 to fund AI compute, which upsized to $84.75B within 24 hours. Berkshire Hathaway committed $10B through a private placement — buying Class A shares at $351.81 and Class C shares at $348.20. It's Berkshire's biggest tech bet since Apple, and it tells you that long-only investors now treat AI infrastructure the same way they treat railroads: boring, capital-intensive, and essential.

*Sources: [Bloomberg](https://www.bloomberg.com/news/articles/2026-06-01/alphabet-to-raise-80-billion-in-equity-capital-for-ai-spending) · [Axios](https://www.axios.com/2026/06/01/alphabet-80-billion-ai-buildout)*

## OpenAI and Microsoft Ship Major Product Updates

### OpenAI Rewrites ChatGPT Memory With Dreaming V3

OpenAI shipped Dreaming V3 to Plus and Pro users in the US on June 4, replacing the static saved-memories list with a background process that reads your full conversation history and synthesizes what it knows about you — without you doing anything. Factual recall on OpenAI's internal eval jumped from 41.5% in 2024 to 82.8%, and memory now stays current over time: "You're going to Singapore in July" becomes "You went to Singapore in July 2026" once the trip ends. Free users follow once a roughly 5x compute cost reduction makes it economical to scale.

*Sources: [OpenAI](https://openai.com/index/chatgpt-memory-dreaming/) · [TechTimes](https://www.techtimes.com/articles/317840/20260605/chatgpt-memory-dreaming-update-openai-rewrites-personalization-engine-limits-audit-trail.htm)*

### Microsoft Launches 7 In-House MAI Models, Aiming for "Long-Term Self-Sufficiency"

At Build 2026 on June 2, Microsoft unveiled seven models under the MAI brand — all trained from scratch, no OpenAI distillation. The flagship, MAI-Thinking-1, has 35B active parameters and a 256K-token context window; it matches Claude Sonnet 4.6 in blind human testing and ties Claude Opus 4.6 on one coding benchmark. Microsoft says it outperformed GPT 5-5 on a McKinsey engagement task at 10x lower cost.

*Sources: [CNBC](https://www.cnbc.com/2026/06/02/microsoft-unveils-new-ai-models-lessen-reliance-on-openai-lower-costs.html) · [GeekWire](https://www.geekwire.com/2026/microsoft-unveils-seven-homegrown-ai-models-in-bid-for-long-term-self-sufficiency/)*

### OpenAI Adds Lockdown Mode for Security-Sensitive Deployments

OpenAI shipped Lockdown Mode — an opt-in setting that disables web browsing, deep research, agentic workflows, and file downloads to cut prompt injection and data exfiltration risk. It's aimed at enterprise users handling sensitive data. The feature is a direct acknowledgment that connecting agents to live web content creates a real attack surface.

*Sources: [OpenAI Help Center](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)*

## Open-Weights Models Reach Frontier Territory

### DeepSeek V4 Pro: 1.6T Parameters, Open-Weights, Scores With GPT-5.5

DeepSeek released V4-Pro (1.6T total parameters, 49B active) and V4-Flash (284B) on April 24 as a preview with 1M-token context. V4-Pro is scoring alongside GPT-5.5 and Claude Opus 4.7 on agentic benchmarks, and it uses only 27% of the inference FLOPs of its predecessor at the same context length. Both are open-weights, which means any team with enough compute can run what is effectively frontier-class performance without a proprietary API.

*Sources: [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) · [DataCamp](https://www.datacamp.com/blog/deepseek-v4)*

### Mistral Ships Devstral 2 at 123B on Amazon Bedrock

Mistral released Devstral 2, a 123B coding model, on Amazon Bedrock at $0.40 per million input tokens. The pricing puts serious coding capacity within reach of enterprise teams without frontier API budgets. Devstral 2 joins a cluster of open-weights coding models from European and Chinese labs that have shipped in the past two weeks.

*Sources: [LLM Stats](https://llm-stats.com/llm-updates)*

## Washington and DeepMind Draw Lines

### Trump Signs AI Executive Order — Voluntary 30-Day Review, No Mandates

President Trump signed "Promoting Advanced Artificial Intelligence Innovation and Security" on June 2, asking frontier AI labs to voluntarily submit their most powerful models for government testing up to 30 days before public release. The order also creates an AI cybersecurity clearinghouse and tasks agencies with benchmarking AI cyber capabilities. An earlier draft proposed a mandatory 90-day window; industry pushback cut it to 30 days, voluntary — and the final text explicitly bans any mandatory licensing or pre-clearance regime.

*Sources: [NPR](https://www.npr.org/2026/06/02/nx-s1-5844347/ai-safety-trump-executive-order) · [White House](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/)*

### Demis Hassabis Puts 2030 on the AGI Calendar

DeepMind CEO Demis Hassabis said at Google I/O: "2030 is when I expect it to arrive, either plus or minus a year." He also disclosed that DeepMind hired more than 20 researchers from Contextual AI in an $80–90M licensing deal, the kind of talent consolidation you do when you have a specific timeline in mind. A public year from a sitting lab CEO is rare — investors and regulators now have a concrete milestone to track.

*Sources: [Fast Company](https://www.fastcompany.com/91544235/demis-hassabis-google-io-2026) · [HeyGoTrade](https://www.heygotrade.com/en/news/google-io-2026-gemini-deepmind-contextual-ai/)*

<div class="social-content" markdown="1">

Anthropic is now worth more on paper than OpenAI, and it just filed to go public.

→ Anthropic filed a confidential S-1 at a $965B valuation after closing a $65B Series H  
→ Alphabet raised $84.75B for AI compute, with Berkshire Hathaway committing $10B privately  
→ Microsoft's 7 in-house MAI models beat GPT 5-5 at 10x lower cost on a McKinsey benchmark  
→ OpenAI's Dreaming V3 pushed ChatGPT factual recall from 41.5% to 82.8%  
→ DeepSeek V4 Pro's 1.6T open-weights model now scores alongside GPT-5.5 on agent benchmarks

Demis Hassabis just put 2030 on the AGI calendar. The capital, the models, and the policy are converging.

Full brief with sources and details: [link in comments]

#Anthropic #Microsoft #OpenAI #AIStartups #LLM #AI

</div>
