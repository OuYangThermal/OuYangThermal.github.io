---
title: Thermal Gel
description: Dispensable gap fillers for variable gaps, automation, rework, and stress-sensitive assemblies.
permalink: /thermal-gel/
---

Dispensable gap fillers for variable gaps, automation, rework, and stress-sensitive assemblies.

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "thermal-gel" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
