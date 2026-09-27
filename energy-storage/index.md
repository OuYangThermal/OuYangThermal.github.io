---
title: Energy Storage
description: Thermal materials for ESS, battery packs, liquid cooling plates, and BMS electronics.
permalink: /energy-storage/
---

Thermal materials for ESS, battery packs, liquid cooling plates, and BMS electronics.

<p><a href="{{ '/video-guide/thermal-management-materials-video-guide/#video-ess-battery-pack' | relative_url }}">Watch TIMs inside an ESS battery pack</a> — a video chapter showing where thermal interface materials sit between cells, modules and the liquid cooling plate.</p>

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "energy-storage" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
