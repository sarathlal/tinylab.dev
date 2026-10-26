---
title: "Docker"
description: "Package any program so it runs the same on any machine — images, containers, volumes, networks, Compose, security, and what happens inside the kernel."
permalink: /learn/docker/
toc: false
sitemap:
  priority: 0.9
  changefreq: 'weekly'
---

**Docker** packages a program together with everything it needs — libraries, settings, a filesystem — into an *image*, and runs that image as a *container*: an isolated process that behaves the same on your laptop, a colleague's machine and a server in the cloud. It is the first tool most people meet on the way into DevOps, and the foundation Kubernetes is built on.

This subject starts with what a container actually is, builds up through images, Dockerfiles, volumes, networking and Compose, covers security and debugging, and ends inside the kernel with namespaces, cgroups and the OCI runtimes.

## How to use this subject

- **Read in order** — each page builds on the one before.
- **Run the commands** — every page has a hands-on part; that is where the understanding comes from.
- **Check yourself at the end** — each page closes with questions whose answers are in the page.
- **Stop at the depth you need** — pages are tagged <span class="badge badge-foundation">foundation</span>, <span class="badge badge-intermediate">intermediate</span> and <span class="badge badge-advanced">advanced</span>.

## Contents

{% include track-contents.html track="docker" %}
