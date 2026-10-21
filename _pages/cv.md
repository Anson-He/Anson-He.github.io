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

<p><a href="{{ '/files/Yuhao_He_CV.pdf' | relative_url }}">[Download CV (English)]</a> · <a href="{{ '/files/Yuhao_He_CV_CN.pdf' | relative_url }}" lang="zh-CN">[下载中文简历]</a></p>

<p><strong>Research focus:</strong> Secure and trustworthy AI, with a particular interest in protecting visual content from malicious generative editing. Current directions include Adversarial Machine Learning, Data Poisoning and Protection, and AI-Generated Content Security.</p>

## Education

<div class="timeline">
  <div class="timeline__item">
    <p><strong>Macau University of Science and Technology</strong><span>Sept. 2025 – present</span></p>
    <p>Ph.D. in Artificial Intelligence, Faculty of Innovation Engineering</p>
    <p>GPA: 3.85/4.0</p>
    <p>Supervisor: Prof. <a href="https://jinyutian.github.io/">Jinyu Tian</a></p>
  </div>
  <div class="timeline__item">
    <p><strong>Macau University of Science and Technology</strong><span>Sept. 2023 – Jun. 2025</span></p>
    <p>M.S. in Intelligent Technology, Faculty of Innovation Engineering</p>
    <p>GPA: 3.71/4.0</p>
    <p>Supervisor: Prof. <a href="https://jinyutian.github.io/">Jinyu Tian</a></p>
  </div>
  <div class="timeline__item">
    <p><strong>Foshan University</strong><span>Sept. 2019 – Jun. 2023</span></p>
    <p>B.S. in Mathematics and Applied Mathematics (AI Innovation Class), Department of Mathematics and Big Data</p>
    <p>GPA: 86.8/100 · Ranking: 5/72</p>
    <p>Supervisor: Prof. <a href="https://www.researchgate.net/profile/Xianwei-Zheng-2">Xianwei Zheng</a></p>
  </div>
</div>

## Publications

<ol class="cv-publications">
{% assign sorted_publications = site.publications | sort: "date" | reverse %}
{% for post in sorted_publications %}
  {% unless post.visible == false %}
  <li>{{ post.citation }} {% for link in post.links %}{% assign link_label = link.label | downcase %}{% if link_label == "paper" or link_label == "code" %}<a href="{{ link.url }}">[{{ link.label }}]</a>{% endif %}{% endfor %}</li>
  {% endunless %}
{% endfor %}
</ol>

## Honors & Awards

<ul class="honors-list">
  <li><span>[2021]</span> <strong>National Scholarship for Undergraduates.</strong></li>
  <li><span>[2021]</span> National Second Prize, China Undergraduate Mathematical Contest in Modeling.</li>
  <li><span>[2020]</span> Second Prize, Guangdong–Hong Kong–Macao Mathematical and Financial Modeling Competition.</li>
  <li><span>[2023]</span> Outstanding Undergraduate Graduate, Foshan University.</li>
  <li><span>[2023]</span> Recipient of the Foshan Specialty Medical Catheters Innovation and Entrepreneurship Scholarship.</li>
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
      <p>Improved the detection of policy-violating promotional content on social media platforms by optimizing content filtering rules, reducing the false-negative rate from 12% to 5%.</p>
    </div>
  </div>
  <div class="experience-row">
    <a class="experience-row__logo" href="https://dayandata.cn/" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/images/companies/dayan-data-logo.png' | relative_url }}" alt="Foshan Dayan Data logo" width="88" height="88" loading="lazy">
    </a>
    <div class="experience-row__content">
      <p><strong>Foshan Dayan Data Technology Co., Ltd.</strong><span>Jun. 2021 – Aug. 2021</span></p>
      <p><em>Algorithm and Development Intern</em></p>
      <ul>
        <li>Contributed to the development of a deep learning-based strawberry disease and pest recognition system, achieving 89% accuracy across 14 categories.</li>
        <li>Led the development of a WeChat mini-program deployed in local strawberry farms, resulting in a registered software copyright.</li>
      </ul>
    </div>
  </div>
</div>

## Copyrights

<ul class="copyright-list">
  <li><strong>Strawberry Pest and Disease Identification Mini Program V1.0</strong>, Software Copyright Registration No. 2022SRA003183, National Copyright Administration of the People’s Republic of China.</li>
</ul>

## Academic Profiles

[Google Scholar](https://scholar.google.com/citations?user=Ug6Zp5IAAAAJ) · [OpenReview](https://openreview.net/profile?id=~Yuhao_He2) · [GitHub](https://github.com/Anson-He)
