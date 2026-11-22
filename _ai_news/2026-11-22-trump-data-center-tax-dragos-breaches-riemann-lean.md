---
layout: post
title: "Trump Threatens 'Tremendous Tax' on Offshore Data Centers, Dragos Catches 3 AI Providers Breached, Riemann Proof Passes Lean Checks — November 22, 2026"
slug: trump-data-center-tax-dragos-breaches-riemann-lean
date: 2026-11-22 07:15:00 +0530
categories: [ai, news, daily-brief]
tags: [ai, llm, daily-brief]
description: "Signal blocks in-app screenshots on iOS and Android, Amazon nears a $7.5B Decart deal, and a House panel says Commerce cleared 879,000 Nvidia and AMD AI chips for China."
---

The weekend news was about where AI runs and who can see what goes into it. Washington wants the compute at home, and a security firm just showed how leaky the prompt pipeline is.

## Washington wants to control where AI compute lives

### Trump says US companies can't build data centers abroad, threatens a "tremendous tax"
"We're not going to allow our companies to build data centers outside of our country," Trump said Friday. He promised "a tremendous tax" on anyone who does, but named no rate, no start date and no legal mechanism. He also said he hadn't told his own officials about the plan yet. Only Congress can set federal taxes, and Forbes notes it's unclear whether the threat would even reach Gulf projects run by foreign owners.

*Sources: [CNBC](https://www.cnbc.com/2026/11/20/trump-data-centers-ai-companies-tax.html) · [Axios](https://www.axios.com/2026/11/20/us-ai-trump-data-centers-overseas) · [NBC News](https://www.nbcnews.com/business/corporations/trump-data-centers-overseas-penalties-rcna610445) · [Forbes](https://www.forbes.com/sites/guneyyildiz/2026/11/21/trump-wants-ai-data-centers-in-west-virginia-the-gulf-wants-them-too-and-needs-his-permission/)*

### House panel: Commerce cleared 879,000 Nvidia and AMD AI chips for China
Export-license data released by House Foreign Affairs chair Brian Mast shows approvals for more than 879,000 chips between December 2025 and May 2026. Chinese buyers asked for 3.4 million. Tencent got 150,000, Alibaba 75,000, Baidu 43,000 and BYD 4,000, and all four sit on the Pentagon's list of alleged military-linked firms. Nvidia says that despite some licenses, "we have since stopped shipping H200s to China."

*Sources: [CNBC](https://www.cnbc.com/2026/11/19/nvidia-amd-china-chip-sales-congress.html) · [Seeking Alpha](https://seekingalpha.com/news/4675059-trump-administration-signed-off-nearly-900000-nvidia-amd-ai-chips-for-china-in-six-months)*

## Your prompts and chats are less private than you think

### Dragos seeded 2 million prompts with fake secrets and caught 3 AI providers breached
HD Moore's team at Dragos sent about two million prompts with unique canary URLs and AWS keys to AI services from July through November. Secrets from at least three providers turned up in break-in attempts on Dragos test systems. One attacker seems to have hit two providers at once, using both sets of secrets from a single rented server. Dragos says none of the three knew until it told them, and some leaked requests were marked zero-data-retention.

*Sources: [Dragos](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens) · [Cybr Sec Media](https://www.cybrsecmedia.com/two-million-ai-prompts-expose-breaches-data-theft-and-supply-chain-failures/)*

### Signal starts blocking screenshots on iPhone and Android
Signal said Friday it's limiting screenshots inside its mobile apps. President Meredith Whittaker calls OS-level AI agents an "existential threat" to private messaging, since many agents work by reading the screen. The timing isn't random. Days earlier, Reuters reported Meta staff found its Muse agent reading encrypted Signal messages through notification and screenshot permissions.

*Sources: [TechCrunch](https://techcrunch.com/2026/11/21/signal-restricts-mobile-screenshots-as-it-confronts-existential-threat-of-ai-surveillance) · [CTV News (Reuters)](https://www.ctvnews.ca/sci-tech/article/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/)*

## Anthropic's first weekend under the microscope

### The Claude-built Riemann proof compiles, but nobody's calling it solved
Levent Alpöge posted his claimed proof Friday only as Lean code, with no human-readable paper. MIT's Andrew Sutherland compiled it on his own and says it rests on just "the three standard axioms." Three independently written Lean kernels also accepted it. The open question is whether the formal statement really matches the Riemann hypothesis. Skeptics point to July, when a Lean "disproof" of Collatz slipped past the checker through a kernel bug.

*Sources: [Scientific American](https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/) · [Nacionale](https://www.nacionale.com/en/articles/when-will-we-know-riemann-hypothesis-proof-verified-alpoge-claude-lean-what-happens-next)*

### Anthropic's record IPO didn't save the AI trade
The Nasdaq 100 fell 10% this week, even with Anthropic's record-breaking listing. ANT closed Friday at $88.30, about 6% above its $83 offer price after nearly touching it. Capital Economics' Joe Maher put it bluntly: the IPO "has failed to rekindle enthusiasm for tech stocks." Wall Street now has to work out what could turn the AI trade around.

*Sources: [Bloomberg](https://www.bloomberg.com/news/articles/2026-11-21/wall-street-asks-what-can-save-ai-trade-after-anthropic-wipeout) · [Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-friday-november-19-dow-sp-500-nasdaq-anthropic-nvidia-141644188.html)*

## Big Tech goes shopping for AI startups

### Amazon nears a deal worth up to $7.5B for Decart
Amazon is close to buying Israeli AI startup Decart for more than $7 billion. Earn-outs could push the total to nearly $7.5 billion, paid in cash, stock and deferred payments. Decart's software helps move models between chips, including Amazon's Trainium. Decart was worth about $4 billion in May. Anthropic reportedly looked at a $6 billion bid in August and then walked away.

*Sources: [TechRepublic](https://www.techrepublic.com/article/news-amazon-decart-ai-acquisition-talks/) · [FourWeekMBA](https://fourweekmba.com/ai-amazon-nears-7b-decart-deal-1-75x-its-may-valuation/)*

### Nvidia is close to buying diffusion-LLM startup Inception for over $500M
The Information reports Nvidia is near a deal for Inception, which builds language models that use diffusion instead of word-by-word generation. The aim is to strengthen Nvidia's Nemotron open models. Neither company has confirmed it. It would land while Nvidia's stock sits about 47% below its October peak.

*Sources: [The Information](https://theinformation.com/articles/nvidia-nears-acquisition-diffusion-ai-developer-500-million) · [Newsquawk](https://www.newsquawk.com/headlines/nvidia-nvda-is-near-to-acquiring-diffusion-ai-developer-inception-for-over-usd-500mln-according-to-the-information)*

<div class="social-content" markdown="1">

Trump says US companies won't be allowed to build AI data centers abroad, and he's threatening a "tremendous tax" with no details attached.

→ House panel: Commerce cleared 879,000 Nvidia and AMD AI chips for China, out of 3.4M requested  
→ Dragos sent 2M prompts with fake secrets and caught 3 AI providers breached  
→ Signal now blocks screenshots on iOS and Android, citing AI agents  
→ The Claude-built Riemann proof compiles in Lean, but experts aren't calling it solved  
→ Amazon nears a deal worth up to $7.5B for Decart

The US wants AI compute at home and fewer chips going to China. The harder question may be who can see the prompts flowing through it.

Full brief with sources and details: [link in comments]

#Anthropic #NVIDIA #AIPolicy #AIInfrastructure #AI

</div>
