---
title: Optical Module
description: Low-stress, controlled-gap interfaces for optical transceivers.
permalink: /optical-module/
---

Low-stress, controlled-gap interfaces for optical transceivers.

<figure class="evidence-figure evidence-portrait"><img src="{{ '/assets/images/real-evidence/05-optical-transceiver-tim-opened.jpg' | relative_url }}" width="997" height="1272" loading="lazy" decoding="async" alt="Opened optical transceiver showing thermal interface material contact locations"><figcaption><strong>Real Application Reference.</strong> An opened optical-transceiver assembly showing several interface locations between the PCB and housing.</figcaption></figure>

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "optical-module" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
