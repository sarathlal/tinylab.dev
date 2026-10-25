---
title: "DevOps: the complete learning track"
description: "From Docker and Linux fundamentals to Kubernetes internals and platform design — an 8-week core plan plus an 8-week expert extension, built for senior DevOps interviews."
permalink: /learn/devops/
toc: false
sitemap:
  priority: 0.9
  changefreq: 'weekly'
---

This track takes you from "I can run a container" to "I can design, debug and defend a platform." It is written for people preparing for **senior DevOps engineer** interviews, but every page starts with a plain-language explanation, so it works just as well if you are new.

## How the track is organised

Each page follows the same shape, so you always know where you are:

1. **The everyday picture** — the idea explained with a non-technical analogy.
2. **What it actually is** — the same idea in technical terms, kept short.
3. **Try it yourself** — commands or a small lab so it becomes concrete.
4. **In the interview** — the question behind the question, and a model answer.
5. **Common mistakes** — what people get wrong, so you can spot the trap.

Pages are tagged <span class="badge badge-foundation">foundation</span>, <span class="badge badge-senior">senior</span> or <span class="badge badge-expert">expert</span>. Read foundation pages first; senior and expert pages assume you have.

## Time budget

The core plan is 8 weeks at 2–3 hours on weekdays and 4–5 hours on weekends (roughly 150 hours). The expert extension is another 8 weeks. If Linux and the terminal are new to you, add two weeks at the front for the Linux section.

Senior interviews test three things more than any single tool:

- **Depth on fundamentals** — you can explain what happens under the hood, not just which command to run.
- **Judgement** — given a messy scenario, you ask the right questions, weigh trade-offs and justify a decision.
- **Evidence** — you can point to real systems you built or fixed, with numbers. Every week ends in a lab that produces something you can talk about.

## Topic map

| Domain | Weight in interviews | Depth expected at senior level |
| --- | --- | --- |
| Linux & OS internals | High | Process/memory/disk troubleshooting from a shell, systemd, kernel namespaces and cgroups |
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

## The 8-week core schedule

| Week | Focus | Lab deliverable |
| --- | --- | --- |
| 1 | Linux internals, networking refresh, Bash | Debug a deliberately broken VM; write up the root cause |
| 2 | Docker fundamentals and internals | Containerise a 2-service app with Compose; multi-stage, non-root, under 100 MB |
| 3 | Docker advanced: security, networking, registries, CI builds | Private registry, scanning in CI, signed images, BuildKit cache |
| 4 | Kubernetes core: architecture, workloads, networking | Deploy the app on kind/k3s with Deployments, Services, Ingress, probes |
| 5 | Kubernetes advanced: storage, RBAC, Helm, autoscaling, upgrades | Helm chart, HPA, PDB, NetworkPolicies, RBAC; simulate a node failure |
| 6 | CI/CD and GitOps, Terraform | Pipeline that builds, tests, scans, pushes and promotes via Argo CD; Terraform for the cluster |
| 7 | Observability, security, cloud | Prometheus + Grafana + Loki, SLO dashboard, alerts; secrets via External Secrets |
| 8 | System design, scenarios, behavioural; final mocks | Two written designs, one postmortem, five STAR stories, three mock interviews |

## The expert extension (weeks 9–16)

Expert knowledge separates a senior who runs tools from one who can design, debug and extend the platform itself. The extension covers container and kernel internals, Kubernetes internals and operators, platform engineering, reliability engineering, security at depth, and infrastructure and cost at scale. Each area has a lab that proves it and the interview question that reveals it.

## Portfolio project

One public Git repo grows through the whole track: a small API with a database and a background worker, wrapped in progressively more platform. By week 8 it is the thing you demo in every round. Record numbers as you go (image size, pipeline time, p95 latency under load, scale-up time); interviewers trust specifics.

## Start here

The sidebar lists every section in reading order. If you are preparing for interviews and short on time, go straight to **Docker → What is a container?** and work forward; come back to Linux and networking when a Docker or Kubernetes page sends you there.
