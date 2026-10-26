---
title: "Kubernetes"
description: "Run containers across many machines — scheduling, networking, storage, scaling, zero-downtime updates, and the control plane that makes it work."
permalink: /learn/kubernetes/
toc: false
sitemap:
  priority: 0.9
  changefreq: 'weekly'
---

**Kubernetes** runs containers across a fleet of machines. You tell it what you want running — "three copies of this image, reachable at this address, with this much memory" — and it finds room, starts the containers, restarts them when they die, spreads traffic across them and replaces them without downtime when you ship a new version.

This subject assumes you know Docker. It starts with why orchestration exists and how the control plane is built, then covers each kind of object you will use, how traffic and storage work, how to run workloads well, packaging with Helm and Kustomize, day-two operations, and finally the internals.

## How to use this subject

- **Read in order** — each page builds on the one before.
- **Run the commands** — every page has a hands-on part; that is where the understanding comes from.
- **Check yourself at the end** — each page closes with questions whose answers are in the page.
- **Stop at the depth you need** — pages are tagged <span class="badge badge-foundation">foundation</span>, <span class="badge badge-intermediate">intermediate</span> and <span class="badge badge-advanced">advanced</span>.

## Contents

{% include track-contents.html track="kubernetes" %}
