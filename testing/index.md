---
title: Testing
description: How methods and conditions affect reported thermal results.
permalink: /testing/
---

How methods and conditions affect reported thermal results.

<figure class="engineering-visual"><img src="{{ '/assets/images/visual-content/thermal-material-test-method-pressure-thickness.webp' | relative_url }}" width="1440" height="810" loading="lazy" decoding="async" alt="Thermal material test stack showing pressure, thickness, temperature and heat flow conditions"><figcaption><strong>Generic Engineering Diagram.</strong> Test method and boundary conditions—including thickness, pressure, temperature and surface condition—affect thermal results. This is not a representation of OUYANG THERMAL-owned laboratory equipment or test capability.</figcaption></figure>

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "testing" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
