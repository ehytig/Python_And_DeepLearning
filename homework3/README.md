

### 快速开始

- 利用Dockerfile在Bithub上生成镜像

- 下载balloon数据集并上传到Bithub，同时要修改程序中的文件路径

  ```bash
  wget https://github.com/matterport/Mask_RCNN/releases/download/v2.1/balloon_dataset.zip
  unzip balloon_dataset.zip > /dev/null
  ```

- 运行代码

  ```
  python mask_rcnn.py
  ```

### 项目介绍

主要借鉴了Facebook团队给出的[示例代码](https://colab.research.google.com/drive/16jcaJoc6bCFAQ96jDe2HwtXj7BMD_-m5#scrollTo=9_FzH13EjseR)

代码基于[detectron2包](https://github.com/facebookresearch/detectron2)给出的框架，调用这个包完成Mask-RCNN网络的训练

config文件采用detecron2内置的COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml

Model采用本仓库中的model_final_f10217.pkl

### 训练参数设置

参数设置在detectron2中内置的COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml基础上进行修改，主要修改如下

```python
cfg.DATALOADER.NUM_WORKERS = 2 # 读取数据的进程个数
cfg.SOLVER.IMS_PER_BATCH = 2 # 一次训练所抓取的数据样本数量
cfg.SOLVER.BASE_LR = 0.00025 # 初始的学习率
cfg.SOLVER.MAX_ITER = 1000 # 最多训练次数
cfg.SOLVER.STEPS = [] # 不进行学习率改变
cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 128 #每一张照片拿去训练的anchor的数量
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1 # 类别数目，使用数据集balloon只有一个类别
```

### 文件说明

###### Dockerfile

用于在Bithub上面生成镜像，可能仅适用于Bithub上生成镜像

###### mask_rcnn.py

程序主文件

###### model_final_f10217.pkl

网络框架，使用中载入其中的网络框架而不载入训练好的参数

###### setup.ipynb

配置环境时可能用到的命令

### 

