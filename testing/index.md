---
title: Testing
description: How methods and conditions affect reported thermal results.
permalink: /testing/
---

How methods and conditions affect reported thermal results.

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "testing" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
