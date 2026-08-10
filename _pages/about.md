---
permalink: /
title: "About Me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am currently a Ph.D. student in Artificial Intelligence in the [Faculty of Innovation Engineering](https://www.must.edu.mo/en/fie) at the [Macau University of Science and Technology](https://www.must.edu.mo/en), under the supervision of Prof. [Jinyu Tian](https://jinyutian.github.io/). I received my M.S. in Intelligent Technology from Macau University of Science and Technology in 2025 and my B.S. in Mathematics and Applied Mathematics (AI Innovation Class) from Foshan University in 2023. My research focuses on adversarial machine learning, data poisoning and data protection, and the security of AI-generated content, with a particular interest in protecting visual content from malicious generative editing.

🔬 Research Interests
======

- Adversarial Machine Learning
- Data Poisoning/Protection
- AI-Generated Content Security

📰 News
======

<ul>
{% for item in site.data.auto_news %}
  <li><strong>{{ item.date }}:</strong> {{ item.text }}</li>
{% endfor %}
{% for item in site.data.manual_news %}
  <li><strong>{{ item.date }}:</strong> {{ item.text }}{% if item.url %} <a href="{{ item.url }}">[{{ item.label | default: "Link" }}]</a>{% endif %}</li>
{% endfor %}
</ul>

📚 Publications
======

<ul class="compact-publication-list">
{% assign sorted_publications = site.publications | sort: "date" | reverse %}
{% for post in sorted_publications %}
  {% include publication-list-item.html publication=post %}
{% endfor %}
</ul>

🔗 Academic Profiles
======

[Google Scholar](https://scholar.google.com/citations?user=Ug6Zp5IAAAAJ) · [DBLP](https://dblp.org/pid/257/8328-1.html) · [ORCID](https://orcid.org/0009-0002-8778-5025) · [OpenReview](https://openreview.net/profile?id=~Yuhao_He2) · [GitHub](https://github.com/Anson-He)
