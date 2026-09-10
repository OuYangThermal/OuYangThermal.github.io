---
title: "Thermal Pad"
display_title: Thermal Pad
description: Compressible sheet-form gap fillers: selection, thickness, hardness, compression, and reliability.
permalink: /thermal-pad/
---

Compressible sheet-form gap fillers: selection, thickness, hardness, compression, and reliability.

<figure class="evidence-figure"><img src="{{ '/assets/images/real-evidence/02-obc-thermal-pad-layout.jpg' | relative_url }}" width="750" height="479" loading="lazy" decoding="async" alt="Pre-cut thermal pads positioned between OBC electronics and the mating housing"><figcaption><strong>Real Application Reference.</strong> Pre-cut thermal pads positioned at multiple OBC interface locations. No material grade or performance is inferred from the photograph.</figcaption></figure>

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "thermal-pad" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
