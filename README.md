# SOLIDER

This is the offical pytorch implementation for CVPR2023 paper "**Beyond Appearance: a Semantic Controllable Self-Supervised Learning Framework for Human-Centric Visual Tasks**".

## Results
<div align="center"><img src="assets/framework.png" width="900"></div>

## Introduction
Human-centric visual tasks have attracted increasing research attention due to their widespread applications. In this paper, we aim to learn a general human representation from massive unlabeled human images which can benefit downstream human-centric tasks to the maximum extent. We call this method SOLIDER, a Semantic cOntrollable seLf-supervIseD lEaRning framework. Unlike the existing self-supervised learning methods, prior knowledge from human images is utilized in SOLIDER to build pseudo semantic labels and import more semantic information into the learned representation. Meanwhile, we note that different downstream tasks always require different ratios of semantic information and appearance information. For example, human parsing requires more semantic information, while person re-identification needs more appearance information for identification purpose. So a single learned representation cannot fit for all requirements. To solve this problem, SOLIDER introduces a conditional network with a semantic controller. After the model is trained, users can send values to the controller to produce representations with different ratios of semantic information, which can fit different needs of downstream tasks. Finally, SOLIDER is verified on six downstream human-centric visual tasks. It outperforms state of the arts and builds new baselines for these tasks.

## Installation
This codebase has been developed with python version 3.7, PyTorch version 1.7.1, CUDA 10.1 and torchvision 0.8.2.                                           

## Datasets
Download **LUPerson** from its [offical link](https://github.com/DengpanFu/LUPerson-NL/tree/main/LUP-NL) and unzip it.                                                               

## Training
- Choice 1. To train SOLIDER from scratch, please run:
```shell
sh run_solider.sh
```

- Choice 2. Training SOLIDER from scratch may take a long time. To speed up the training, you can train a DINO model first, and then finetune it with SOLIDER, as follows:
```shell
sh run_dino.sh
sh resume_solider.sh
```

## Finetuning and Inference
There is a demo to run the trained SOLIDER model, which can be embedded into the inference or the downstream task finetuning.
```shell
python demo.py
```

## Models
| Backbone | Swin Base | Swin Small | Swin Tiny |
| ------ |:---: | :---: | :---: |
| | [Link](https://drive.google.com/file/d/1uh7tO34tMf73MJfFqyFEGx42UBktTbZU/view?usp=share_link) | [Link](https://drive.google.com/file/d/1oyEgASqDHc7YUPsQUMxuo2kBZyi2Tzfv/view?usp=share_link) | [Link](https://drive.google.com/file/d/12UyPVFmjoMVpQLHN07tNh4liHUmyDqg8/view?usp=share_link) |  

- All the models are trained on the whole LUPerson dataset.

## Updates
- The training codes of downstream tasks will be released soon.

## Knowledgement
Our implementation is mainly based on the following codebases. We gratefully thank the authors for their wonderful works.
- [damo-cv/TransReID-SSL](https://github.com/damo-cv/TransReID-SSL)
- [facebookresearch/dino](https://github.com/facebookresearch/dino).

