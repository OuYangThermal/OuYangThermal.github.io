---
title: Structural Adhesive
description: Load-bearing bonds where thermal transfer is one of several requirements.
permalink: /structural-adhesive/
---

Load-bearing bonds where thermal transfer is one of several requirements.

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "structural-adhesive" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
