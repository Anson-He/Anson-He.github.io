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
      Email: <a href="mailto:3250004430@student.must.edu.mo">3250004430@student.must.edu.mo</a>
    </p>
    <p class="profile-links">
      <a href="https://scholar.google.com/citations?user=Ug6Zp5IAAAAJ">[Google Scholar]</a>
      <a href="https://dblp.org/pid/257/8328-1.html">[DBLP]</a>
      <a href="https://orcid.org/0009-0002-8778-5025">[ORCID]</a>
      <a href="https://github.com/Anson-He">[GitHub]</a>
      <a href="{{ '/files/Yuhao_He_CV.pdf' | relative_url }}">[CV]</a>
    </p>
  </div>
</header>

## Biography

I was born in Jiangmen, Guangdong, China, in 2001. I am currently a Ph.D. student in Artificial Intelligence in the [Faculty of Innovation Engineering](https://www.must.edu.mo/en/fie) at the [Macau University of Science and Technology](https://www.must.edu.mo/en), under the supervision of Prof. [Jinyu Tian](https://jinyutian.github.io/).

My research works toward secure and trustworthy AI, with a particular interest in **protecting visual content from malicious generative editing**. My current research directions include:

- Adversarial Machine Learning
- Data Poisoning and Protection
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

## Copyrights

<ul class="copyright-list">
  <li><strong>Strawberry Pest and Disease Identification Mini Program V1.0</strong>, Software Copyright Registration No. 2022SRA003183, National Copyright Administration of the People’s Republic of China.</li>
</ul>

## Internship Experience

<div class="experience-list">
  <div class="experience-row">
    <a class="experience-row__logo" href="https://www.joyy.com/" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/images/companies/joyy-logo.jpg' | relative_url }}" alt="JOYY logo" width="112" height="64" loading="lazy">
    </a>
    <div class="experience-row__content">
      <p><strong>JOYY, Guangzhou</strong><span>Feb. 2023 – Jun. 2023</span></p>
      <p><em>Algorithm Intern</em></p>
      <p>Developed and maintained risk-control algorithms for social products. Monitored market data and refined risk-control rules, reducing the false-negative rate from 12% to 5%.</p>
    </div>
  </div>
  <div class="experience-row">
    <a class="experience-row__logo" href="https://dayandata.cn/" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/images/companies/dayan-data-logo.png' | relative_url }}" alt="Foshan Dayan Data logo" width="88" height="88" loading="lazy">
    </a>
    <div class="experience-row__content">
      <p><strong>Foshan Dayan Data Technology Co., Ltd.</strong><span>Jun. 2021 – Aug. 2021</span></p>
      <p><em>Algorithm and Development Intern</em></p>
      <p>Curated a dataset of more than 30,000 images across 29 categories and developed an SE-ResNet50-based strawberry disease and pest classifier, achieving 89% accuracy across 14 categories. Led the development of a WeChat mini-program that received software copyright registration and was deployed in local plantations in Foshan.</p>
    </div>
  </div>
</div>

## Education

<div class="education-list">
  <div class="education-row">
    <a class="education-row__logo" href="https://www.must.edu.mo/en" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/images/institutions/must-emblem.jpg' | relative_url }}" alt="Macau University of Science and Technology emblem" width="88" height="88" loading="lazy">
    </a>
    <div class="education-row__content">
      <p><strong>Macau University of Science and Technology</strong><span>Sept. 2025 – present</span></p>
      <p>Ph.D. in Artificial Intelligence, Faculty of Innovation Engineering</p>
      <p>Supervisor: Prof. <a href="https://jinyutian.github.io/">Jinyu Tian</a></p>
    </div>
  </div>
  <div class="education-row">
    <a class="education-row__logo" href="https://www.must.edu.mo/en" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/images/institutions/must-emblem.jpg' | relative_url }}" alt="Macau University of Science and Technology emblem" width="88" height="88" loading="lazy">
    </a>
    <div class="education-row__content">
      <p><strong>Macau University of Science and Technology</strong><span>Sept. 2023 – Jun. 2025</span></p>
      <p>M.S. in Intelligent Technology, Faculty of Innovation Engineering</p>
      <p>Supervisor: Prof. <a href="https://jinyutian.github.io/">Jinyu Tian</a></p>
    </div>
  </div>
  <div class="education-row">
    <a class="education-row__logo" href="https://www.fosu.edu.cn/" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/images/institutions/foshan-university-logo.png' | relative_url }}" alt="Foshan University emblem" width="88" height="88" loading="lazy">
    </a>
    <div class="education-row__content">
      <p><strong>Foshan University</strong><span>Sept. 2019 – Jun. 2023</span></p>
      <p>B.S. in Mathematics and Applied Mathematics (AI Innovation Class), Department of Mathematics and Big Data</p>
      <p>Undergraduate advisor: Prof. <a href="https://www.researchgate.net/profile/Xianwei-Zheng-2">Xianwei Zheng</a></p>
    </div>
  </div>
</div>

## Honors & Awards

<ul class="honors-list">
  <li><span>[2023]</span> Outstanding Undergraduate Graduate, Foshan University.</li>
  <li><span>[2023]</span> Recipient of the Foshan Specialty Medical Catheters Innovation and Entrepreneurship Scholarship.</li>
  <li><span>[2021]</span> National Scholarship for Undergraduates.</li>
  <li><span>[2021]</span> National Second Prize, National College Students Mathematical Modeling Competition.</li>
  <li><span>[2020]</span> National Second Prize, Guangdong–Hong Kong–Macao Financial Mathematical Modeling Competition.</li>
</ul>
