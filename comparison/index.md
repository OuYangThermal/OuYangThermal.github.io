---
title: Comparison Hub
description: Objective, parameter-led comparisons between TIM families and grades.
permalink: /comparison/
---

Objective, parameter-led comparisons between TIM families and grades.

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "comparison" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
