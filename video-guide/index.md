---
title: Video Guide
description: Video guides showing where thermal interface materials are actually used inside electronic products, with engineering selection notes.
permalink: /video-guide/
---

Video guides showing where thermal interface materials are actually used inside electronic products — ESS battery packs, optical modules, laptops and more — with the engineering context needed to select the right TIM.

<ul class="article-list">
{% assign items = site.articles | where: "category_slug", "video-guide" | sort: "date" | reverse %}
{% for item in items %}<li><a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a><br><span>{{ item.description }}</span></li>{% endfor %}
</ul>

<p>Prefer a hands-on tool? Try the <a href="{{ '/engineering-resources/tim-selection-tool/' | relative_url }}">TIM selection tool</a> or the <a href="{{ '/engineering-resources/thermal-resistance-calculator/' | relative_url }}">thermal resistance calculator</a> in <a href="{{ '/engineering-resources/' | relative_url }}">engineering resources</a>.</p>
