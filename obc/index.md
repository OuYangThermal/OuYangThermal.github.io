---
title: OBC & EV
description: TIM selection for on-board chargers, DC/DC converters, IGBTs, and MOSFETs.
permalink: /obc/
---

TIM selection for on-board chargers, DC/DC converters, IGBTs, and MOSFETs.

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "obc" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
