---
title: TinyLab
layout: default
description: Learn essentail skills to start your first job or continue in your job.
sitemap:
  priority: 1
  changefreq: 'daily'
---

{% assign post = site.posts.first %}
{% assign content = post.content %}

<h1>
{% if post.title %}
    {{ post.title }}
{% endif %}
</h1>
{{ content }}

