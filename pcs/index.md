---
title: PCS
description: Thermal interface design for power conversion systems.
permalink: /pcs/
---

Thermal interface design for power conversion systems.

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "pcs" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
