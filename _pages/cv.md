---
layout: archive
title: "📄 CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

🎓 Education
======

- **Ph.D. in Artificial Intelligence**, Faculty of Innovation Engineering<br>
  Macau University of Science and Technology, Macau, China · Sept. 2025 – present<br>
  Supervisor: Prof. [Jinyu Tian](https://jinyutian.github.io/)
- **M.S. in Intelligent Technology**, Faculty of Innovation Engineering<br>
  Macau University of Science and Technology, Macau, China · Sept. 2023 – Jun. 2025
- **B.S. in Mathematics and Applied Mathematics (AI Innovation Class)**, Department of Mathematics and Big Data<br>
  Foshan University, Guangdong, China · Sept. 2019 – Jun. 2023

🔬 Research Interests
======

- Adversarial Machine Learning
- Data Poisoning/Protection
- AI-Generated Content Security

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

- [Google Scholar](https://scholar.google.com/citations?user=Ug6Zp5IAAAAJ)
- [DBLP](https://dblp.org/pid/257/8328-1.html)
- [ORCID](https://orcid.org/0009-0002-8778-5025)
- [OpenReview](https://openreview.net/profile?id=~Yuhao_He2)
- [GitHub](https://github.com/Anson-He)
