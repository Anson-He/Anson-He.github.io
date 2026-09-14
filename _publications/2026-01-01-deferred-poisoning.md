---
title: "Deferred Poisoning: Making the Model More Vulnerable via Hessian Singularization"
collection: publications
category: conferences
permalink: /publication/deferred-poisoning
excerpt: "A stealthy training-time poisoning attack that preserves normal validation behavior while increasing model vulnerability to small perturbations."
date: 2026-01-01
venue: "Proceedings of the 40th AAAI Conference on Artificial Intelligence (AAAI 2026)"
paperurl: "https://doi.org/10.1609/aaai.v40i26.39318"
authors: "Yuhao He, Jinyu Tian, Xianwei Zheng, Li Dong, Yuanman Li, and Jiantao Zhou"
author_links: [{"name": "Yuhao He", "url": "https://anson-he.github.io/", "affiliation": "Faculty of Innovation Engineering, Macau University of Science and Technology"}, {"name": "Jinyu Tian", "url": "https://jinyutian.github.io/", "affiliation": "Faculty of Innovation Engineering, Macau University of Science and Technology"}, {"name": "Xianwei Zheng", "url": "https://www.researchgate.net/profile/Xianwei-Zheng-2", "affiliation": "School of Mathematics, Foshan University"}, {"name": "Li Dong", "url": "https://nbudongli.github.io/", "affiliation": "Faculty of Electrical Engineering and Computer Science, Ningbo University"}, {"name": "Yuanman Li", "url": "https://yuanmanli.github.io/", "affiliation": "College of Electronics and Information Engineering, Shenzhen University"}, {"name": "Jiantao Zhou", "url": "https://www.fst.um.edu.mo/personal/jtzhou/", "affiliation": "Department of Computer and Information Science, University of Macau"}]
abstract: "Recent studies have shown that deep learning models are very vulnerable to poisoning attacks. Many defense methods have been proposed to address this issue. However, traditional poisoning attacks are not as threatening as commonly believed. This is because they often cause differences in how the model performs on the training set compared to the validation set. Such inconsistency can alert defenders that their data has been poisoned, allowing them to take the necessary defensive actions. In this paper, we introduce a more threatening type of poisoning attack called the Deferred Poisoning Attack. This new attack allows the model to function normally during the training and validation phases but makes it very sensitive to evasion attacks or even natural noise. We achieve this by ensuring the poisoned model's loss function has a similar value as a normally trained model at each input sample but with a large local curvature. A similar model loss ensures that there is no obvious inconsistency between the training and validation accuracy, demonstrating high stealthiness. On the other hand, the large curvature implies that a small perturbation may cause a significant increase in model loss, leading to substantial performance degradation, which reflects a worse robustness. We fulfill this purpose by making the model have singular Hessian information at the optimal point via our proposed Singularization Regularization term. We have conducted both theoretical and empirical analyses of the proposed method and validated its effectiveness through experiments on image classification tasks. Furthermore, we have confirmed the hazards of this form of poisoning attack under more general scenarios using natural noise, offering a new perspective for research in the field of security."
image: "/images/publications/deferred-poisoning-figure-1.png"
image_alt: "Figure 1 from Deferred Poisoning, showing the deferred poisoning deployment scenario."
links: [{"label": "Paper", "url": "https://doi.org/10.1609/aaai.v40i26.39318"}, {"label": "arXiv", "url": "https://arxiv.org/abs/2411.03752"}, {"label": "Code", "url": "https://github.com/Anson-He/Deferred-Poisoning-Attack"}, {"label": "MUST News", "url": "https://sgs.must.edu.mo/news.school.news/article/view/id-39098.html"}, {"label": "DBLP", "url": "https://dblp.org/rec/conf/aaai/HeTZDLZ26"}]
citation: "<strong>Y. H. He</strong>, J. Y. Tian, X. W. Zheng, L. Dong, Y. M. Li, J. T. Zhou, &ldquo;Deferred Poisoning: Making the Model More Vulnerable via Hessian Singularization&rdquo;, <i>AAAI</i>. (CCF A)"
dblp_key: "conf/aaai/HeTZDLZ26"
generated_by: dblp_sync
bibtex: |-
  @article{he2026deferred,
    author  = {He, Yuhao and Tian, Jinyu and Zheng, Xianwei and Dong, Li and Li, Yuanman and Zhou, Jiantao},
    title   = {Deferred Poisoning: Making the Model More Vulnerable via Hessian Singularization},
    journal = {Proceedings of the AAAI Conference on Artificial Intelligence},
    volume  = {40},
    number  = {26},
    pages   = {21681--21689},
    year    = {2026},
    doi     = {10.1609/aaai.v40i26.39318},
    url     = {https://doi.org/10.1609/aaai.v40i26.39318}
  }
---

This work introduces the Deferred Poisoning Attack, which makes a trained model highly sensitive to evasion attacks or natural noise while maintaining apparently normal behavior during training and validation. The method uses singularization regularization to reshape local curvature near the optimum.

[[Paper]](https://doi.org/10.1609/aaai.v40i26.39318) [[arXiv]](https://arxiv.org/abs/2411.03752) [[Code]](https://github.com/Anson-He/Deferred-Poisoning-Attack) [[MUST News]](https://sgs.must.edu.mo/news.school.news/article/view/id-39098.html) [[DBLP]](https://dblp.org/rec/conf/aaai/HeTZDLZ26)
