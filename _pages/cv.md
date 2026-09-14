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
<a href="mailto:3250004430@student.must.edu.mo">3250004430@student.must.edu.mo</a></p>

<p><a href="{{ '/files/Yuhao_He_CV.pdf' | relative_url }}">[Download PDF CV]</a></p>

<p><strong>Research focus:</strong> Secure and trustworthy AI, with a particular interest in protecting visual content from malicious generative editing. Current directions include Adversarial Machine Learning, Data Poisoning and Protection, and AI-Generated Content Security.</p>

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

## Publications

<ol class="cv-publications">
{% assign sorted_publications = site.publications | sort: "date" | reverse %}
{% for post in sorted_publications %}
  <li>{{ post.citation }} {% for link in post.links %}{% assign link_label = link.label | downcase %}{% if link_label == "paper" or link_label == "code" %}<a href="{{ link.url }}">[{{ link.label }}]</a>{% endif %}{% endfor %}</li>
{% endfor %}
</ol>

## Honors & Awards

<ul class="honors-list">
  <li><span>[2023]</span> Outstanding Undergraduate Graduate, Foshan University.</li>
  <li><span>[2023]</span> Recipient of the Foshan Specialty Medical Catheters Innovation and Entrepreneurship Scholarship.</li>
  <li><span>[2021]</span> National Scholarship for Undergraduates.</li>
  <li><span>[2021]</span> National Second Prize, National College Students Mathematical Modeling Competition.</li>
  <li><span>[2020]</span> National Second Prize, Guangdong–Hong Kong–Macao Financial Mathematical Modeling Competition.</li>
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
    <div class="experience-row__logo">
      <img src="{{ '/images/companies/dayan-data-mark.svg' | relative_url }}" alt="Foshan Dayan Data text mark" width="88" height="88" loading="lazy">
    </div>
    <div class="experience-row__content">
      <p><strong>Foshan Dayan Data Technology Co., Ltd.</strong><span>Jun. 2021 – Aug. 2021</span></p>
      <p><em>Algorithm and Development Intern</em></p>
      <p>Curated a dataset of more than 30,000 images across 29 categories and developed an SE-ResNet50-based strawberry disease and pest classifier, achieving 89% accuracy across 14 categories. Led the development of a WeChat mini-program that received software copyright registration and was deployed in local plantations in Foshan.</p>
    </div>
  </div>
</div>

## Copyrights

<ul class="copyright-list">
  <li><strong>Strawberry Pest and Disease Identification Mini Program V1.0</strong>, Software Copyright Registration No. 2022SRA003183, National Copyright Administration of the People’s Republic of China.</li>
</ul>

## Academic Profiles

[Google Scholar](https://scholar.google.com/citations?user=Ug6Zp5IAAAAJ) · [DBLP](https://dblp.org/pid/257/8328-1.html) · [ORCID](https://orcid.org/0009-0002-8778-5025) · [OpenReview](https://openreview.net/profile?id=~Yuhao_He2) · [GitHub](https://github.com/Anson-He)
