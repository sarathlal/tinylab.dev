---
title: "DevOps"
description: "From Docker and Linux fundamentals to Kubernetes internals and platform design — every page in reading order, built for senior DevOps interviews."
permalink: /learn/devops/
toc: false
sitemap:
  priority: 0.9
  changefreq: 'weekly'
---

Read the pages below in order. Each one starts with an everyday analogy, explains the real mechanism, gives you something to try, and ends with the interview questions it answers. Pages are tagged <span class="badge badge-foundation">foundation</span>, <span class="badge badge-senior">senior</span> or <span class="badge badge-expert">expert</span>; stop at the depth you need.

## Contents

{% include track-contents.html track="devops" %}

## About this track

This track is written for people preparing for **senior DevOps engineer** interviews, but it assumes nothing beyond basic terminal use. The core is an 8-week plan at 2–3 hours on weekdays and 4–5 hours on weekends; an 8-week expert extension follows for internals, platform design and scale.

Senior interviews test three things more than any single tool: **depth on fundamentals** (what happens under the hood, not which command to run), **judgement** (weighing trade-offs in a messy scenario), and **evidence** (real systems you built or fixed, with numbers). Every section ends in a lab that produces something you can talk about, and one portfolio repository grows through the whole track.

| Domain | Weight in interviews | Depth expected at senior level |
| --- | --- | --- |
| Linux & OS internals | High | Process/memory/disk troubleshooting from a shell, systemd, namespaces and cgroups |
| Networking | High | TCP/IP, DNS, TLS, HTTP, load balancing, NAT; debug with tcpdump/dig/curl |
| Docker & containers | High | Image internals, build optimisation, runtime security, registries, debugging |
| Kubernetes | Very high | Architecture, scheduling, networking, storage, RBAC, Helm, operators, upgrades |
| CI/CD | High | Pipeline design, caching, artifact promotion, GitOps, rollout strategies |
| Infrastructure as Code | High | Terraform modules, state, drift; config management |
| Cloud | High | IAM, VPC, compute, managed Kubernetes, storage, cost control |
| Observability | High | Metrics/logs/traces, SLOs and error budgets, alert design, on-call |
| Security | Medium-high | Secrets, supply chain (SBOM, signing), least privilege, scanning |
| Scripting | Medium | Bash fluency; Python or Go for automation |
| System design & reliability | Very high | Multi-region, scaling, failure modes, capacity, incidents, postmortems |
| Behavioural / leadership | High | Ownership, mentoring, driving change, handling incidents and disagreement |
