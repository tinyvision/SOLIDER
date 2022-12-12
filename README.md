# SOLIDER

This is the offical pytorch implementation for paper "**Beyond Visual Appearance: a Semantic Controllable Self-Supervised Learning Framework for Human-Centric Visual Tasks**".

## Results
<div align="center"><img src="assets/framework.png" width="900"></div>

## Introduction
Human-centric visual tasks have attracted increasing research attention due to their widespread applications. SOLIDER is a framework used to learn a general human representation from massive unlabeled human images which can benefit downstream human-centric tasks to the maximum extent. The full name of SOLIDER is a **s**emantic c**o**ntrollable se**l**f-superv**i**se**d** l**e**a**r**ning framework. Unlike the existing self-supervised learning methods, prior knowledge from human images is utilized in SOLIDER to build pseudo semantic labels and import more semantic information into the learned representation. Meanwhile, SOLIDER introduces a conditional network with a semantic controller. After the model is trained, users can send values to the controller to produce representations with different ratios of semantic information, which can fit different needs of downstream tasks.

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
| | [Link](https://idstcv.oss-cn-zhangjiakou.aliyuncs.com/SOLIDER/swin_base.pth) | [Link](https://idstcv.oss-cn-zhangjiakou.aliyuncs.com/SOLIDER/swin_small.pth) | [Link](https://idstcv.oss-cn-zhangjiakou.aliyuncs.com/SOLIDER/swin_tiny.pth) |  

- All the models are trained on the whole LUPerson dataset.

## Updates
- The training codes of downstream tasks will be released soon.

## Knowledgement
Our implementation is mainly based on the following codebases. We gratefully thank the authors for their wonderful works.
- [damo-cv/TransReID-SSL](https://github.com/damo-cv/TransReID-SSL)
- [facebookresearch/dino](https://github.com/facebookresearch/dino).

