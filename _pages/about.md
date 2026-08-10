---
permalink: /
title: "👋 About Me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am a Ph.D. student in the [Faculty of Innovation Engineering](https://www.must.edu.mo/en/fie) at the [Macau University of Science and Technology](https://www.must.edu.mo/en). My research focuses on **adversarial machine learning**, **AIGC security**, and **LLM security**.

My current work investigates how learning systems can be compromised at training time and how visual content can be protected from malicious generative editing. I am interested in both the foundations of model vulnerability and practical defenses for secure and trustworthy AI.

🔬 Research Interests
======

- Adversarial machine learning and model robustness
- Data poisoning and training-time attacks
- Security and safety of AI-generated content
- Large language model security

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

🏫 Current Affiliation
======

- **Ph.D. student**, Faculty of Innovation Engineering, Macau University of Science and Technology

🔗 Academic Profiles
======

[Google Scholar](https://scholar.google.com/citations?user=Ug6Zp5IAAAAJ) · [DBLP](https://dblp.org/pid/257/8328-1.html) · [ORCID](https://orcid.org/0009-0002-8778-5025) · [OpenReview](https://openreview.net/profile?id=~Yuhao_He2) · [GitHub](https://github.com/Anson-He)
