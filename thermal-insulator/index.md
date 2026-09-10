---
title: Thermal Insulator
description: Electrically insulating interface constructions for power devices.
permalink: /thermal-insulator/
---

Electrically insulating interface constructions for power devices.

<figure class="evidence-figure"><img src="{{ '/assets/images/real-evidence/08-power-device-insulation-pad.jpg' | relative_url }}" width="800" height="500" loading="lazy" decoding="async" alt="Power semiconductor devices mounted against an electrically insulating thermal interface pad"><figcaption><strong>Engineering Application Example.</strong> An insulating interface between power devices and a metal cooling structure. Electrical and thermal ratings must be verified separately.</figcaption></figure>

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "thermal-insulator" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
