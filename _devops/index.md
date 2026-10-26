---
title: "DevOps"
description: "A hands-on, plain-language course on the tools behind modern software: containers, Linux, networking, Kubernetes, pipelines, cloud and monitoring — every page in reading order."
permalink: /learn/devops/
toc: false
sitemap:
  priority: 0.9
  changefreq: 'weekly'
---

**DevOps** is the work of getting software from a developer's laptop to real users, and keeping it running once it is there. That means packaging programs so they run the same everywhere, setting up the servers and networks they live on, automating the steps between a code change and a release, and watching everything so problems are found before users notice.

This course teaches that work from the ground up. You do not need a computer science degree or a job in tech. You need a laptop, a terminal, and the willingness to type the commands yourself.

## How to use this course

- **Read in order.** Each page builds on the one before it; the numbered list below is the path.
- **Do the "Try it yourself" blocks.** Every page has commands you can run in a few minutes. The understanding comes from running them, not from reading them.
- **Start with an everyday picture.** Each topic opens with an analogy from ordinary life — offices, restaurants, lunchboxes — then explains the real mechanism in plain words.
- **Check yourself at the end.** Each page closes with a few questions. The answers are all in the page; open them only after you have tried.
- **Stop at the depth you need.** Pages are tagged <span class="badge badge-foundation">foundation</span> (assumes nothing), <span class="badge badge-intermediate">intermediate</span> (what you need to use the tool well) and <span class="badge badge-advanced">advanced</span> (how it works inside, and why).

### What you need

- A computer running Linux, macOS or Windows with [Docker Desktop](https://docs.docker.com/get-docker/) (or Docker Engine on Linux) installed.
- A terminal and basic comfort with `cd`, `ls` and editing a text file. If that is new, start with [Linux]({{ site.baseurl }}/learn/linux/) first.
- About 30–60 minutes per page, including the hands-on part.

### The subjects this course uses

DevOps is a way of working that uses several tools, and each tool is its own subject on this site. This course explains the practice and links to the subjects when you need them. The [learning path]({{ site.baseurl }}/learn/devops/getting-started/learning-path/) page gives a suggested order.

| Subject | What it gives you |
| --- | --- |
| [Linux]({{ site.baseurl }}/learn/linux/) | The machines everything runs on |
| [Networking]({{ site.baseurl }}/learn/networking/) | How requests travel and why they fail |
| [Scripting]({{ site.baseurl }}/learn/scripting/) | Bash, Python and Git for automating the rest |
| [Docker]({{ site.baseurl }}/learn/docker/) | Packaging software into containers |
| [Kubernetes]({{ site.baseurl }}/learn/kubernetes/) | Running containers across many machines |
| [Terraform]({{ site.baseurl }}/learn/terraform/) | Infrastructure described in files |
| [Prometheus]({{ site.baseurl }}/learn/prometheus/) | Metrics, dashboards and alerts |

## Contents

{% include track-contents.html track="devops" %}

## What the course covers

| Area | What you will be able to do |
| --- | --- |
| CI/CD and GitOps | Automate testing, building and releasing so a code change reaches users safely in minutes |
| Infrastructure as code | Choose and combine the tools that describe infrastructure in files, and manage machines with Ansible |
| Cloud | Use a cloud provider's building blocks — identity, networking, compute, storage — without surprises on the bill |
| Observability | Measure whether a system is healthy with metrics, logs and traces, set sensible alerts, and run on-call well |
| Security | Keep secrets out of code and images, give every component only the access it needs, and know what you are shipping |
| Reliability | Design for failure, plan capacity, find what is slow, and practise recovery before you need it |
| Platform engineering | Build the paved road other engineers use |

## A project to build along the way

One small project grows through the whole course: a tiny web application with a database and a background worker. You will containerise it, put it on Kubernetes, build a pipeline for it, provision its infrastructure as code, and add monitoring. By the end you will have a working, deployable system you built yourself and understand end to end — which is worth more than any certificate.
