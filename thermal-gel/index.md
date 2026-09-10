---
title: Thermal Gel
description: Dispensable gap fillers for variable gaps, automation, rework, and stress-sensitive assemblies.
permalink: /thermal-gel/
---

Dispensable gap fillers for variable gaps, automation, rework, and stress-sensitive assemblies.

<figure class="engineering-visual"><img src="{{ '/assets/images/visual-content/thermal-gel-dispensing-variable-gap-assembly.webp' | relative_url }}" width="1440" height="810" loading="lazy" decoding="async" alt="Thermal gel dispensing and compression across variable component gaps"><figcaption><strong>Engineering Diagram.</strong> Engineering diagram showing thermal gel dispensing, assembly compression and the installed heat path.</figcaption></figure>

<figure class="evidence-figure evidence-portrait"><img src="{{ '/assets/images/real-evidence/03-pcb-thermal-gel-dispensing.jpg' | relative_url }}" width="1259" height="1280" loading="lazy" decoding="async" alt="Thermal gel deposits dispensed across components on a printed circuit board"><figcaption><strong>Real Application Reference.</strong> Controlled thermal-gel deposits on a PCB before mating with a cooling surface.</figcaption></figure>

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "thermal-gel" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>
