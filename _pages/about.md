---
permalink: /
title: "About Me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I was born in Jiangmen, Guangdong, China, in 2001. I am currently a Ph.D. student in Artificial Intelligence in the [Faculty of Innovation Engineering](https://www.must.edu.mo/en/fie) at the [Macau University of Science and Technology](https://www.must.edu.mo/en), under the supervision of Prof. [Jinyu Tian](https://jinyutian.github.io/). My research focuses on adversarial machine learning, data poisoning and data protection, and AI-generated content security, with a particular interest in **protecting visual content from malicious generative editing**.

🎓 Education
======

- **Ph.D. in Artificial Intelligence**, Faculty of Innovation Engineering<br>
  Macau University of Science and Technology, Macau, China · Sept. 2025 – present
- **M.S. in Intelligent Technology**, Faculty of Innovation Engineering<br>
  Macau University of Science and Technology, Macau, China · Sept. 2023 – Jun. 2025
- **B.S. in Mathematics and Applied Mathematics (AI Innovation Class)**, Department of Mathematics and Big Data<br>
  Foshan University, Guangdong, China · Sept. 2019 – Jun. 2023

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

<div class="publication-list">
{% assign sorted_publications = site.publications | sort: "date" | reverse %}
{% for post in sorted_publications %}
  {% include publication-card.html publication=post heading_level="h3" %}
{% endfor %}
</div>

🔗 Academic Profiles
======

[Google Scholar](https://scholar.google.com/citations?user=Ug6Zp5IAAAAJ) · [DBLP](https://dblp.org/pid/257/8328-1.html) · [ORCID](https://orcid.org/0009-0002-8778-5025) · [OpenReview](https://openreview.net/profile?id=~Yuhao_He2) · [GitHub](https://github.com/Anson-He)
