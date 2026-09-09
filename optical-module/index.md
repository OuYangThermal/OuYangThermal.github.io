---
title: Optical Module
description: Low-stress, controlled-gap interfaces for optical transceivers.
permalink: /optical-module/
---

Low-stress, controlled-gap interfaces for optical transceivers.

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "optical-module" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
