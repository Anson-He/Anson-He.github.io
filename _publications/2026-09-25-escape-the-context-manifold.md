---
title: "Escape the Context Manifold: Preventing DiT In-Context Editing via Conditional Flow Hijacking"
collection: publications
category: conferences
permalink: /publication/escape-the-context-manifold
excerpt: "Conditional Flow Hijacking protects reference images from malicious DiT-based in-context editing while preserving prompt alignment and image quality."
date: 2026-09-25
venue: "NeurIPS"
paperurl: "https://neurips.cc/virtual/2026/poster/156139"
authors: "Yuhao He and Jinyu Tian"
abstract: "Diffusion Transformers enable powerful in-context image editing from a reference image and a text prompt, but also make it easier to maliciously edit public images while preserving the private identity of the reference. Existing DiT-oriented protection methods, such as DeContext, mainly suppress target-to-context attention to weaken reference utilization. However, this strategy can be insufficient for complex edits where prompt semantics already dominate generation. Instead, we study proactive protection for DiT-based editors from a conditional-flow perspective, and use a local geometric interpretation of in-context editing, where the denoising trajectory is empirically characterized as being steered by prompt-consistent and reference-consistent directions. Thus, effective protection should not simply corrupt the output, but should drive it away from the original context manifold. To this end, we propose Conditional Flow Hijacking, which adds perturbations to the reference image. Instead of suppressing context attention, our method preserves the context pathway, but redirects the context-induced steering signals in the intermediate transformer layers, causing the final trajectory to drift away from the reference consistent solution region. Experiments on FLUX.1-Kontext with different datasets and prompts including attribute and complex scene editing show that our method significantly suppresses reference identity leakage while maintaining image quality and prompt alignment, outperforming prior protection baselines, especially under complex scene editing prompts. We further verify the robustness of the proposed protection method as well as its transferability across other models, highlighting the need for proactive defenses for in-context generative models. Code is available at https://github.com/Anson-He/Escape-the-Context-Manifold."
image: "/images/publications/escape-the-context-manifold-insight.png"
image_alt: "Conditional Flow Hijacking redirects context steering away from the reference-consistent manifold."
links: [{"label": "NeurIPS", "url": "https://neurips.cc/virtual/2026/poster/156139"}, {"label": "Poster", "url": "/files/posters/neurips-2026-escape-the-context-manifold.png"}, {"label": "Code", "url": "https://github.com/Anson-He/Escape-the-Context-Manifold"}]
citation: "<strong>Y. H. He</strong>, J. Y. Tian, &ldquo;Escape the Context Manifold: Preventing DiT In-Context Editing via Conditional Flow Hijacking&rdquo;, <i>NeurIPS 2026</i>."
visible: true
generated_by: curated
source_url: "https://neurips.cc/virtual/2026/poster/156139"
bibtex: |-
  @inproceedings{he2026escape,
    title     = {Escape the Context Manifold: Preventing {DiT} In-Context Editing via Conditional Flow Hijacking},
    author    = {Yuhao He and Jinyu Tian},
    booktitle = {The Fortieth Annual Conference on Neural Information Processing Systems},
    year      = {2026},
    url       = {https://neurips.cc/virtual/2026/poster/156139}
  }
---

Conditional Flow Hijacking protects reference images from malicious DiT-based in-context editing while preserving prompt alignment and image quality.

[[NeurIPS]](https://neurips.cc/virtual/2026/poster/156139) [[Poster]](/files/posters/neurips-2026-escape-the-context-manifold.png) [[Code]](https://github.com/Anson-He/Escape-the-Context-Manifold)
