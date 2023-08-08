# CellFluorescenceEnhancement-CycleGAN-pytorch
Description: A clean and readable Pytorch implementation of CycleGAN (https://arxiv.org/abs/1703.10593) for Cell Fluorescence Enhancement.



## **Before using this Repository**

learning something about CycleGAN 

You can get it by:  https://www.jianshu.com/p/5bf937a0d993   or other article is comfortable to you.



## Training

### 1. Setup the dataset
Baidu driver link：https://pan.baidu.com/s/1e9Qc6iUMxC2wCezNHLN6Kw      code：rznb 

Alternatively you can build your own dataset by setting up the following directory structure:

    .
    ├── datasets                   
    |   ├── <dataset_name>         # i.e. cell
    |   |   ├── train              # Training
    |   |   |   ├── A              # Contains domain A images (i.e. The darker cells)
    |   |   |   └── B              # Contains domain B images (i.e. The brighter cells)
    |   |   └── test               # Testing
    |   |   |   ├── A              # Contains domain A images (i.e. The darker cells)
    |   |   |   └── B              # Contains domain B images (i.e. The brighter cells)

The order of A and B is not that important.

### 2. Train!

run  tain.py to start training the model

The process of the training can be showed in tensorboard:

```
tensorboard --logdir=logs
```



### 3.test

run test.py     



The original image:

![cell](.\img_bin\cell.png)





The ideal image

![cell_GT](.\img_bin\cell_GT.png)



The output of the model:



![0001](.\img_bin\0001.png)

## Acknowledgments
Code is basically a cleaner and less obscured implementation of [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix). 
