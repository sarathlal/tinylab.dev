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
- A terminal and basic comfort with `cd`, `ls` and editing a text file. If that is new, start with the Linux section first.
- About 30–60 minutes per page, including the hands-on part.

## Contents

{% include track-contents.html track="devops" %}

## What the course covers

| Area | What you will be able to do |
| --- | --- |
| Linux | Read what a machine is doing — processes, memory, disk, services — and fix common problems from the terminal |
| Networking | Explain how a request travels from a browser to a server and back, and debug it when it doesn't |
| Docker | Package any program into an image that runs the same on any machine, and keep it small and safe |
| Kubernetes | Run many containers across many machines, scale them, update them without downtime, and recover from failures |
| CI/CD | Automate testing, building and releasing so a code change reaches users safely in minutes |
| Infrastructure as code | Describe servers, networks and clusters in files you can review, version and recreate |
| Cloud | Use a cloud provider's building blocks — identity, networking, compute, storage — without surprises on the bill |
| Observability | Measure whether a system is healthy, set sensible alerts, and find the cause when it isn't |
| Security | Keep secrets out of code and images, give every component only the access it needs, and know what you are shipping |

## A project to build along the way

One small project grows through the whole course: a tiny web application with a database and a background worker. You will containerise it, put it on Kubernetes, build a pipeline for it, provision its infrastructure as code, and add monitoring. By the end you will have a working, deployable system you built yourself and understand end to end — which is worth more than any certificate.
