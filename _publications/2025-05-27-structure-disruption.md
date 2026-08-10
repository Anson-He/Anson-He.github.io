---
title: "Structure Disruption: Subverting Malicious Diffusion-Based Inpainting via Self-Attention Query Perturbation"
collection: publications
category: preprints
permalink: /publication/structure-disruption
excerpt: "A proactive image-protection framework that disrupts diffusion-based inpainting by perturbing self-attention queries."
date: 2025-05-27
venue: "arXiv preprint"
paperurl: "https://arxiv.org/abs/2505.19425"
authors: "Yuhao He, Jinyu Tian, Haiwei Wu, and Jianqing Li"
abstract: "The rapid advancement of diffusion models has enhanced their image inpainting and editing capabilities but also introduced significant societal risks. Adversaries can exploit user images from social media to generate misleading or harmful content. While adversarial perturbations can disrupt inpainting, global perturbation-based methods fail in mask-guided editing tasks due to spatial constraints. To address these challenges, we propose Structure Disruption Attack (SDA), a powerful protection framework for safeguarding sensitive image regions against inpainting-based editing. Building upon the contour-focused nature of self-attention mechanisms of diffusion models, SDA optimizes perturbations by disrupting queries in self-attention during the initial denoising step to destroy the contour generation process. This targeted interference directly disrupts the structural generation capability of diffusion models, effectively preventing them from producing coherent images. We validate our motivation through visualization techniques and extensive experiments on public datasets, demonstrating that SDA achieves state-of-the-art (SOTA) protection performance while maintaining strong robustness."
image: "/images/publications/structure-disruption-figure-1.png"
image_alt: "Figure 1 from Structure Disruption, comparing unprotected and protected image editing."
links: [{"label": "Paper", "url": "https://arxiv.org/abs/2505.19425"}, {"label": "DBLP", "url": "https://dblp.org/rec/journals/corr/abs-2505-19425"}]
citation: "<strong>Yuhao He</strong>, Jinyu Tian, Haiwei Wu, and Jianqing Li. (2025). &quot;Structure Disruption: Subverting Malicious Diffusion-Based Inpainting via Self-Attention Query Perturbation.&quot; <i>arXiv preprint</i>."
dblp_key: "journals/corr/abs-2505-19425"
generated_by: dblp_sync
bibtex: |-
  @article{DBLP:journals/corr/abs-2505-19425,
    author       = {Yuhao He and
                    Jinyu Tian and
                    Haiwei Wu and
                    Jianqing Li},
    title        = {Structure Disruption: Subverting Malicious Diffusion-Based Inpainting
                    via Self-Attention Query Perturbation},
    journal      = {CoRR},
    volume       = {abs/2505.19425},
    year         = {2025},
    url          = {https://doi.org/10.48550/arXiv.2505.19425},
    doi          = {10.48550/ARXIV.2505.19425},
    eprinttype   = {arXiv},
    eprint       = {2505.19425},
    timestamp    = {Mon, 07 Jul 2025 01:00:00 +0200},
    biburl       = {https://dblp.org/rec/journals/corr/abs-2505-19425.bib},
    bibsource    = {dblp computer science bibliography, https://dblp.org}
  }
---

This work proposes Structure Disruption Attack, a proactive protection framework for safeguarding sensitive image regions against malicious diffusion-based inpainting. It targets self-attention queries during early denoising to disrupt coherent structure generation.

[[Paper]](https://arxiv.org/abs/2505.19425) [[DBLP]](https://dblp.org/rec/journals/corr/abs-2505-19425)
