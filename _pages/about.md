---
layout: default
title: "Yuhao He"
permalink: /
redirect_from:
  - /about/
  - /about.html
---

<header class="profile-header">
  <div class="profile-header__photo">
    <img src="{{ '/images/google-scholar-avatar.jpg' | relative_url }}" alt="Yuhao He | 何宇浩" width="190" height="190">
  </div>
  <div class="profile-header__info">
    <h1>Yuhao He <span class="chinese-name">何宇浩</span></h1>
    <p class="profile-role">Ph.D. Student in Artificial Intelligence</p>
    <p>
      Faculty of Innovation Engineering<br>
      Macau University of Science and Technology<br>
      Macau, China<br>
      Email: <a href="mailto:ansonhe2001@outlook.com">ansonhe2001@outlook.com</a>
    </p>
    <p class="profile-links">
      <a href="https://scholar.google.com/citations?user=Ug6Zp5IAAAAJ">[Google Scholar]</a>
      <a href="https://dblp.org/pid/257/8328-1.html">[DBLP]</a>
      <a href="https://orcid.org/0009-0002-8778-5025">[ORCID]</a>
      <a href="https://github.com/Anson-He">[GitHub]</a>
      <a href="{{ '/cv/' | relative_url }}">[CV]</a>
    </p>
  </div>
</header>

## Biography

I was born in Jiangmen, Guangdong, China, in 2001. I am currently a Ph.D. student in Artificial Intelligence in the [Faculty of Innovation Engineering](https://www.must.edu.mo/en/fie) at the [Macau University of Science and Technology](https://www.must.edu.mo/en), under the supervision of Prof. [Jinyu Tian](https://jinyutian.github.io/). My research focuses on secure and trustworthy AI, with a particular interest in **protecting visual content from malicious generative editing**.

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

## News

<ul class="news-list">
{% for item in site.data.auto_news %}
  <li><span>[{{ item.date }}]</span> {{ item.text }}</li>
{% endfor %}
{% for item in site.data.manual_news %}
  <li><span>[{{ item.date }}]</span> {{ item.text }}{% if item.url %} <a href="{{ item.url }}">[{{ item.label | default: "Link" }}]</a>{% endif %}</li>
{% endfor %}
</ul>

<h2 id="publications">Publications</h2>

<div class="publication-list">
{% assign sorted_publications = site.publications | sort: "date" | reverse %}
{% for post in sorted_publications %}
  {% include jemdoc-publication.html publication=post %}
{% endfor %}
</div>

<p class="more-link">Complete publication records: <a href="https://scholar.google.com/citations?user=Ug6Zp5IAAAAJ">Google Scholar</a> · <a href="https://dblp.org/pid/257/8328-1.html">DBLP</a> · <a href="{{ '/publications/' | relative_url }}">Publication archive</a></p>
