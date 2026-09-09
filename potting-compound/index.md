---
title: Potting Compound
description: Encapsulation considered across thermal, dielectric, process, mass, and repair requirements.
permalink: /potting-compound/
---

Encapsulation considered across thermal, dielectric, process, mass, and repair requirements.

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "potting-compound" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
