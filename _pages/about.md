---
permalink: /
title: "👋 About Me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am a Ph.D. student in the [Faculty of Innovation Engineering](https://www.must.edu.mo/en/fie) at the [Macau University of Science and Technology](https://www.must.edu.mo/en). My research focuses on **AIGC security**, **visual content protection**, and **LLM security**.

My current work focuses on protecting visual content from malicious generative editing and improving the security and trustworthiness of modern AI systems. I am particularly interested in robust content protection, AIGC security, and the safety of large language models.

🔬 Research Interests
======

- AIGC security and visual content protection
- Adversarial robustness of generative models
- Large language model security and safety
- Secure and trustworthy AI

📰 News
======

<ul>
{% for item in site.data.auto_news %}
  <li><strong>{{ item.year }}:</strong> 📄 <em>{{ item.title }}</em>{% if item.venue %} — {{ item.venue }}{% endif %}. {% if item.paperurl %}<a href="{{ item.paperurl }}">[Paper]</a>{% endif %}{% if item.codeurl and item.codeurl != "" %} <a href="{{ item.codeurl }}">[Code]</a>{% endif %}</li>
{% endfor %}
{% for item in site.data.manual_news %}
  <li><strong>{{ item.year }}:</strong> {{ item.text }}{% if item.url %} <a href="{{ item.url }}">[{{ item.label | default: "Link" }}]</a>{% endif %}</li>
{% endfor %}
</ul>

🎓 Education
======

- **Ph.D. in Artificial Intelligence**, Faculty of Innovation Engineering<br>
  Macau University of Science and Technology, Macau, China · Sept. 2025 – present
- **M.S. in Intelligent Technology**, Faculty of Innovation Engineering<br>
  Macau University of Science and Technology, Macau, China · Sept. 2023 – Jun. 2025
- **B.S. in Mathematics and Applied Mathematics (AI Innovation Class)**, Department of Mathematics and Big Data<br>
  Foshan University, Guangdong, China · Sept. 2019 – Jun. 2023

🔗 Academic Profiles
======

[Google Scholar](https://scholar.google.com/citations?user=Ug6Zp5IAAAAJ) · [DBLP](https://dblp.org/pid/257/8328-1.html) · [ORCID](https://orcid.org/0009-0002-8778-5025) · [OpenReview](https://openreview.net/profile?id=~Yuhao_He2) · [GitHub](https://github.com/Anson-He)
