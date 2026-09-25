---
title: "TFA-CLSTMNN: Novel Convolutional Network for Sound-Based Diagnosis of COVID-19"
collection: publications
category: manuscripts
permalink: /publication/tfa-clstmnn
excerpt: "A convolutional and recurrent neural network for sound-based COVID-19 diagnosis."
date: 2023-01-01
venue: "International Journal of Wavelets, Multiresolution and Information Processing"
paperurl: "https://doi.org/10.1142/S0219691322500588"
authors: "Yuhao He, Xianwei Zheng, and Qing Miao"
abstract: "The outbreak of the global COVID-19 pandemic has become a public crisis and is threatening human life in every country. Recently, researchers have developed testing methods via patients cough recordings. In order to improve the testing accuracy, in this paper, we establish a novel COVID-19 sound-based diagnosis framework, i.e. TFA-CLSTMNN, which integrates time-frequency domain features of the recorded cough with the Attention-Convolution Long Short-Term Memory Neural Network. Specifically, we calculate the Mel-frequency cepstrum coefficient (MFCC) of the cough data to extract the time-frequency domain features. We then apply the convolutional neural network and the attentional mechanism on the time-frequency features, which is followed by the long short-term memory neural network to analyze the MFCC features of the data. The recognition and classification can be then carried out to evaluate the positiveness or negativeness of the tested samples. Experimental results show that the proposed TFA-CLSTMNN framework outperforms the baseline neural networks in sound-based COVID-19 diagnosis and derives an accuracy over 0.95 on the public real-world datasets."
image: "/images/publications/tfa-clstmnn-figure-3.png"
image_alt: "Figure 3 from TFA-CLSTMNN, comparing colorful audio spectrograms and waveforms under data augmentation."
links: [{"label": "Paper", "url": "https://doi.org/10.1142/S0219691322500588"}, {"label": "Code", "url": "https://github.com/Anson-He/TFA-CLSTMNN-Novel-convolutional-network-for-sound-based-diagnosis-of-COVID-19"}, {"label": "DBLP", "url": "https://dblp.org/rec/journals/ijwmip/HeZM23"}]
citation: "<strong>Y. H. He</strong>, X. W. Zheng, Q. Miao, &ldquo;TFA-CLSTMNN: Novel Convolutional Network for Sound-Based Diagnosis of COVID-19&rdquo;, <i>IJWMIP</i>."
dblp_key: "journals/ijwmip/HeZM23"
semantic_scholar_id: "acfc88df21d831c282be5af014fd1096b274e6ac"
visible: true
generated_by: dblp_sync
bibtex: |-
  @article{he2023tfa,
    author  = {He, Yuhao and Zheng, Xianwei and Miao, Qing},
    title   = {TFA-CLSTMNN: Novel Convolutional Network for Sound-Based Diagnosis of COVID-19},
    journal = {International Journal of Wavelets, Multiresolution and Information Processing},
    volume  = {21},
    number  = {3},
    pages   = {2250058},
    year    = {2023},
    doi     = {10.1142/S0219691322500588},
    url     = {https://doi.org/10.1142/S0219691322500588}
  }
---

This paper presents a neural architecture for sound-based COVID-19 diagnosis that combines time-frequency analysis, convolutional feature extraction, and long short-term memory modeling.

[[Paper]](https://doi.org/10.1142/S0219691322500588) [[Code]](https://github.com/Anson-He/TFA-CLSTMNN-Novel-convolutional-network-for-sound-based-diagnosis-of-COVID-19) [[DBLP]](https://dblp.org/rec/journals/ijwmip/HeZM23)
