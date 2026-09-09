---
title: Thermal Insulator
description: Electrically insulating interface constructions for power devices.
permalink: /thermal-insulator/
---

Electrically insulating interface constructions for power devices.

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "thermal-insulator" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
