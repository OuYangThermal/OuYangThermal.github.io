---
title: Thermal Pad
description: Compressible sheet-form gap fillers: selection, thickness, hardness, compression, and reliability.
permalink: /thermal-pad/
---

Compressible sheet-form gap fillers: selection, thickness, hardness, compression, and reliability.

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "thermal-pad" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
