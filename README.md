# CellFluorescenceEnhancement-CycleGAN-pytorch
Description: A clean and readable Pytorch implementation of CycleGAN (https://arxiv.org/abs/1703.10593) for Cell Fluorescence Enhancement.



## **Before using this Repository**

learning something about CycleGAN 

You can get it at:  https://www.jianshu.com/p/5bf937a0d993   or another article that suits you.



## Training

### 1. Setup the dataset
Baidu driver link：https://pan.baidu.com/s/1TjbajGIbNp0Zxf1bXLE98g       code：rznb 



Alternatively, you can build your own dataset by setting up the following directory structure:

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

The process of the training can be shown in tensorboard:

```
tensorboard --logdir=logs
```



### 3.test

run test.py     



The original image:


<div align=center>
<img src="https://github.com/shahelaojieraozhi/CellFluorescenceEnhancement_by_CycleGAN/blob/master/img_bin/cell.png">
</div>



The ideal image

<div align=center>
<img src="https://github.com/shahelaojieraozhi/CellFluorescenceEnhancement_by_CycleGAN/blob/master/img_bin/cell_GT.png">
</div>


The output of the model:

<div align=center>
<img src="https://github.com/shahelaojieraozhi/CellFluorescenceEnhancement_by_CycleGAN/blob/master/img_bin/0001.png">
</div>


Contrast of flattening

<div align=center>
<img src="https://github.com/shahelaojieraozhi/CellFluorescenceEnhancement_by_CycleGAN/blob/master/img_bin/cell.png"><img src="https://github.com/shahelaojieraozhi/CellFluorescenceEnhancement_by_CycleGAN/blob/master/img_bin/cell_GT.png"><img src="https://github.com/shahelaojieraozhi/CellFluorescenceEnhancement_by_CycleGAN/blob/master/img_bin/0001.png">
</div>





## Acknowledgments
Code is basically a cleaner and less obscured implementation of [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix). 
