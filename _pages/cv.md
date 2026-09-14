---
layout: default
title: "CV"
permalink: /cv/
redirect_from:
  - /resume
---

<h1 class="page-title">Curriculum Vitae</h1>

<p><strong>Yuhao He | 何宇浩</strong><br>
Ph.D. Student in Artificial Intelligence<br>
Macau University of Science and Technology · Macau, China<br>
<a href="mailto:ansonhe2001@outlook.com">ansonhe2001@outlook.com</a></p>

## Education

<div class="timeline">
  <div class="timeline__item">
    <p><strong>Macau University of Science and Technology</strong><span>Sept. 2025 – present</span></p>
    <p>Ph.D. in Artificial Intelligence, Faculty of Innovation Engineering</p>
    <p>Supervisor: Prof. <a href="https://jinyutian.github.io/">Jinyu Tian</a></p>
  </div>
  <div class="timeline__item">
    <p><strong>Macau University of Science and Technology</strong><span>Sept. 2023 – Jun. 2025</span></p>
    <p>M.S. in Intelligent Technology, Faculty of Innovation Engineering</p>
    <p>Supervisor: Prof. <a href="https://jinyutian.github.io/">Jinyu Tian</a></p>
  </div>
  <div class="timeline__item">
    <p><strong>Foshan University</strong><span>Sept. 2019 – Jun. 2023</span></p>
    <p>B.S. in Mathematics and Applied Mathematics (AI Innovation Class), Department of Mathematics and Big Data</p>
  </div>
</div>

## Research Interests

- Adversarial Machine Learning
- Data Poisoning/Protection
- AI-Generated Content Security

## Publications

<ol class="cv-publications">
{% assign sorted_publications = site.publications | sort: "date" | reverse %}
{% for post in sorted_publications %}
  <li>{{ post.citation }} {% for link in post.links %}{% assign link_label = link.label | downcase %}{% if link_label == "paper" or link_label == "code" %}<a href="{{ link.url }}">[{{ link.label }}]</a>{% endif %}{% endfor %}</li>
{% endfor %}
</ol>

## Academic Profiles

[Google Scholar](https://scholar.google.com/citations?user=Ug6Zp5IAAAAJ) · [DBLP](https://dblp.org/pid/257/8328-1.html) · [ORCID](https://orcid.org/0009-0002-8778-5025) · [OpenReview](https://openreview.net/profile?id=~Yuhao_He2) · [GitHub](https://github.com/Anson-He)
