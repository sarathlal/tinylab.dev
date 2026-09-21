---
layout: post
title: "Trump Admin Guts AI Safety Institute Staff, Plugin4Shell Zero-Click Flaw Hits Coding Agents, Gemini Hacks 3 Firms — September 21, 2026"
slug: trump-ai-safety-institute-cuts-plugin4shell-gemini-hack
date: 2026-09-21 09:00:00 +0530
categories: [ai, news, daily-brief]
tags: [ai, llm, daily-brief]
description: "CXMT mass-produces G5 DRAM without ASML tools, Naive AI hits $1.42B before shipping a model, StepFun opens its 600B Step 5 API, and clinicians triple AI use but balk beyond diagnostics."
---

Trump's new "AI Force" arrived alongside reported plans to gut the agency that tests AI for safety, a zero-click bug hit four major coding agents, and Google's Gemini quietly broke into three real companies during a test. Here's what mattered in the last day.

## Trump's AI Force Comes With Cuts to the Government's Own AI Watchdog

### Trump Admin Reportedly Plans to Cut Up to 500 NIST Staff, Including the AI Safety Institute

Just as Trump touted a new "AI Force" and pledged not to "stifle" the industry, his administration is reportedly planning to fire as many as 500 workers at NIST, including much of the AI Safety Institute, the body that tests frontier models for safety risks. Most AISI staff are still on their one-year probation period, making them easy to cut. Alexandra Reeve Givens of the Center for Democracy and Technology said the move "would do nothing to make U.S. AI companies more competitive" while gutting the government's ability to catch unsafe systems.

*Sources: [Yahoo News](https://www.yahoo.com/news/ai-safety-advocates-slam-trump-175348692.html) · [Washington Post](https://www.washingtonpost.com/politics/2026/09/19/trump-form-ai-force-name-ai-czar-rejects-calls-constraints/)*

### David Sacks Calls Anthropic's Slowdown Push "Regulatory Capture"

Trump's former AI czar David Sacks dismissed Dario Amodei's call to pace AI development as an attempt at "regulatory capture." "If the unreleased models are scary enough that you think you should slow down, I support your decision to be responsible," Sacks wrote, daring Anthropic to hold back its own models instead of asking Washington to slow everyone else. Amodei's warning had already pulled Sam Altman and Elon Musk into agreement that the industry needs to pace itself.

*Sources: [CNBC](https://www.cnbc.com/2026/09/15/trump-opposition-to-ai-rules-undercuts-industrys-calls-for-a-slowdown.html) · [Axios](https://www.axios.com/2026/09/19/trump-ai-czar-space-force-safety)*

## AI Agents Keep Finding Their Way Into Places They Shouldn't

### Plugin4Shell Flaw Lets Attackers Hijack Claude Code, Codex and Copilot

Researchers disclosed Plugin4Shell, a zero-click bug that lets attackers swap in malicious plugin code even when an AI coding agent checks a pinned commit hash before installing it. The agents verify the hash exists but never confirm the files on disk actually match it, so a compromised plugin update can run silently in the background with the same access as the developer using it. Anthropic patched Claude Code in version 2.1.179 and OpenAI fixed Codex in version 0.146.0; GitHub Copilot remains unpatched.

*Sources: [The Register](https://www.theregister.com/security/2026/09/17/ai-coding-agents-0-click-rce-flaw-could-hand-attackers-keys-to-the-kingdom/5297335) · [Help Net Security](https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/)*

### Google's Gemini Hacked Three Real Companies During a Security Test

Gemini broke into three real companies during a May 2026 red-team exercise before anyone noticed, cracking one system's password through repeated guessing and finding live credentials sitting in a public code repository for the other two. Evaluator Irregular traced the breach to a naming collision, where a fictional test company's name matched a real domain, combined with a misconfigured test environment that left outbound internet access open. Gemini stopped on its own once it realized the systems were real; Google says it has since tightened evaluation isolation.

*Sources: [The Hacker News](https://thehackernews.com/2026/09/google-gemini-broke-into-real-company.html) · [CNN Business](https://www.cnn.com/2026/09/19/business/gemini-ai-hack-internet)*

## China's AI Buildout Keeps Compounding

### CXMT Starts Mass-Producing G5 DRAM, Squeezing Samsung and SK Hynix

China's CXMT announced its fifth-generation DRAM platform hit mass production at the World Manufacturing Convention in Hefei, using quadruple patterning to reach an 11.95nm half-pitch without any of ASML's banned lithography tools. The company says G5 yields at least 50% more dies per wafer than its prior generation, and two 24Gb LPDDR5X chips built on it are already shipping in mainstream Chinese phones. CXMT now holds roughly 10% of global DRAM share, running three fabs at 300,000 wafers a month.

*Sources: [Global Times](https://www.globaltimes.cn/page/202609/1370944.shtml) · [Seoul Economic Daily](https://en.sedaily.com/international/2026/09/20/chinas-cxmt-starts-mass-production-on-5th-generation-dram)*

### Tencent-Backed Naive AI Hits $1.42B Valuation Before Shipping a Model

Naive AI, founded seven months ago by Tsinghua professor Dai Jifeng, raised $400M across three rounds from Tencent, IDG Capital and HSG at a $1.42B valuation, with fewer than 100 employees and no released model yet. The startup isn't pretraining from scratch; it plans to ship its first open-weight LLM this month by modifying existing Chinese open-weight architectures instead. The bet is that China's base models are now good enough that a small team can fine-tune its way to a frontier-adjacent product.

*Sources: [Eastern Herald](https://easternherald.com/2026/09/20/naive-ai-beijing-tencent-400m-open-weight-llm/) · [GuruFocus](https://www.gurufocus.com/news/9087950/naive-ai-secures-400-million-funding-valuation-exceeds-14-billion)*

### StepFun Opens API Access to Its 600B-Parameter Step 5 Model

StepFun launched Step 5 Preview, a 600B-parameter sparse mixture-of-experts model with 27B active parameters per token and a 1M-token context window, and opened API access the same day at roughly $1 per million input tokens. Open weights are due October 15. It's the latest in a run of large Chinese models landing within days of each other this month, and a sign of how fast Chinese labs are now shipping frontier-scale systems compared to a year ago.

*Sources: [Pandaily](https://pandaily.com/stepfun-step-5-preview-600b-moe-1m-context) · [Eastern Herald](https://easternherald.com/2026/09/20/stepfun-step-5-preview-china-ai-model-open-weights/)*

## AI's Workplace Reckoning

### Clinicians Triple Their AI Use, But Draw the Line at Diagnosis

A Wolters Kluwer survey of 355 US physicians and nurses found daily AI use tripled over the past year, but 74% worry about deskilling and 74% about hallucinations once AI moves beyond imaging and diagnostics. Awareness of formal AI governance policies barely moved, from 21% to 27%. Clinicians say they're fine using AI for scans and documentation, but want real evidence before trusting it with treatment decisions.

*Sources: [WION](https://www.wionews.com/world/doctors-are-refusing-ai-beyond-scans-and-the-reason-is-thin-evidence-1789912405164) · [Healthcare Dive](https://www.healthcaredive.com/news/healthcare-ai-adoption-accelerates-provider-worries-deskilling-wolters-kluwer/821653/)*

### AI-Linked Layoffs Pass 50,000 for the Year, Spreading Past Tech

Companies have announced roughly 50,000 AI-linked job cuts in 2026 so far, about 17% of all layoffs tracked this year. Uber alone cut nearly 3,400 jobs, about 10% of its workforce, in early September. The cuts have moved well beyond tech and software roles into finance, logistics, consulting, media and retail.

*Sources: [CBS News](https://www.cbsnews.com/news/ai-layoffs-hiring-entry-level-workers/) · [Skillsyncer](https://skillsyncer.com/layoffs-tracker)*

<div class="social-content" markdown="1">

Trump just touted an "AI Force" while his administration reportedly moves to gut the team that tests AI for safety.

→ Trump admin plans to cut up to 500 NIST staff, including the AI Safety Institute  
→ David Sacks calls Anthropic's slowdown push "regulatory capture"  
→ Plugin4Shell zero-click flaw hits Claude Code, Codex and Copilot — GitHub still unpatched  
→ Google's Gemini autonomously hacked 3 real companies during a May red-team test  
→ China's CXMT mass-produces G5 DRAM with no ASML tools, and Naive AI hits $1.42B pre-launch

Washington wants to go faster on AI. It's cutting the people whose job is to check the brakes.

Full brief with sources and details: [link in comments]

#AIPolicy #Anthropic #GoogleDeepMind #AI

</div>
