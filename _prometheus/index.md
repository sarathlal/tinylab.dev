---
title: "Prometheus"
description: "Measure whether a system is healthy — metrics, PromQL, alerting rules, Alertmanager, Grafana dashboards and scaling out."
permalink: /learn/prometheus/
toc: false
sitemap:
  priority: 0.9
  changefreq: 'weekly'
---

**Prometheus** collects numbers about a running system — requests per second, error rates, memory in use, queue lengths — stores them over time, and lets you query and alert on them. It is the standard metrics system for containers and Kubernetes.

This subject starts with the data model and your first scrape, teaches PromQL properly, covers alerting and Alertmanager, dashboards in Grafana, and the production concerns: Kubernetes discovery, cardinality, retention and scaling out.

## How to use this subject

- **Read in order** — each page builds on the one before.
- **Run the commands** — every page has a hands-on part; that is where the understanding comes from.
- **Check yourself at the end** — each page closes with questions whose answers are in the page.
- **Stop at the depth you need** — pages are tagged <span class="badge badge-foundation">foundation</span>, <span class="badge badge-intermediate">intermediate</span> and <span class="badge badge-advanced">advanced</span>.

## Contents

{% include track-contents.html track="prometheus" %}
