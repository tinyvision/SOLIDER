<div align="center"><img src="assets/logo.png" width="900"></div>

Welcome to **SOLIDER**! SOLIDER is a Semantic Controllable Self-Supervised Learning Framework to learn general human representations from massive unlabeled human images which can benefit downstream human-centric tasks to the maximum extent. Unlike the existing self-supervised learning methods, prior knowledge from human images is utilized in SOLIDER to build pseudo semantic labels and import more semantic information into the learned representation. Meanwhile, different downstream tasks always require different ratios of semantic information and appearance information, and a single learned representation cannot fit for all requirements. To solve this problem, SOLIDER introduces a conditional network with a semantic controller, which can fit different needs of downstream tasks. For more details, please refer to our paper [Beyond Appearance: a Semantic Controllable Self-Supervised Learning Framework for Human-Centric Visual Tasks](xxx).

<div align="center"><img src="assets/framework.png" width="900"></div>

## Updates
- **[2023/03/28: Codes of 3 downstream tasks are released!] ![new](https://img.alicdn.com/imgextra/i4/O1CN01kUiDtl1HVxN6G56vN_!!6000000000764-2-tps-43-19.png)**
    * Training details of our pretrained model on 3 downstream human visual tasks, including person re-identification, person search and pedestrian detection, are released.
- **[2023/03/13: SOLIDER is accepted by CVPR2023!]**
    * The paper of SOLIDER is accepted by CVPR2023, and its offical pytorch implementation is released in this repo. 

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

## Codes on Downstream Tasks
- [Person Re-identification](https://github.com/tinyvision/SOLIDER-REID)
- [Person Search](https://github.com/tinyvision/SOLIDER-PersonSearch)
- [Pedestrian Detection](https://github.com/tinyvision/SOLIDER-PedestrianDetection)
- Human Attributes
- Human Parsing
- Pose Estimation

## Acknowledgement
Our implementation is mainly based on the following codebases. We gratefully thank the authors for their wonderful works.
- [DINO](https://github.com/facebookresearch/dino)
- [TransReID](https://github.com/damo-cv/TransReID)
- [TransReID-SSL](https://github.com/damo-cv/TransReID-SSL)
- [SeqNet](https://github.com/serend1p1ty/SeqNet)
- [Pedestron](https://github.com/hasanirtiza/Pedestron)

## Reference
If you use SOLIDER in your research, please cite our work by using the following BibTeX entry:
```
@inproceedings{chen2023beyond,
  title={Beyond Appearance: a Semantic Controllable Self-Supervised Learning Framework for Human-Centric Visual Tasks},
  author={Weihua Chen and Xianzhe Xu and Jian Jia and Hao Luo and Yaohua Wang and Fan Wang and Rong Jin and Xiuyu Sun},
  booktitle={The IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year={2023},
}
