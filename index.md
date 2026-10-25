---
title: TinyLab
layout: page
description: Plain-language tutorials for people building a career in tech — DevOps, Docker, Kubernetes, Linux, Python, Go, Rust and React — plus a daily AI news brief.
sitemap:
  priority: 1
  changefreq: 'daily'
---

# Learn tech the plain-language way

TinyLab explains technical topics the way you'd explain them to a friend: an everyday example first, the real mechanism second, then something you can try yourself. Each track is organised as a tutorial series you can read in order, and every page ends with a few questions to check what you learned.

## Learning tracks

{% include track-grid.html %}

## Latest AI news

{% assign news = site.ai_news | sort: "date" | reverse %}
<ul class="archive">
{% for entry in news limit: 5 %}
  <li class="archive-item">
    <span class="archive-date text-muted">{{ entry.date | date: "%b %-d" }}</span>
    <a href="{{ site.baseurl }}{{ entry.url }}">{{ entry.title }}</a>
  </li>
{% endfor %}
</ul>

[All AI news →]({{ site.baseurl }}/news/ai/)
