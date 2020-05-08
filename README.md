# FastDVDnet

A state-of-the-art, simple and fast network for Deep Video Denoising which uses no motion compensation.

NEW: Paper to be presented at CVPR2020

Previous deep video denoising algorithm: [DVDnet](https://github.com/m-tassano/dvdnet)

## Overview

This source code provides a PyTorch implementation of the FastDVDnet video denoising algorithm, as in 
Tassano, Matias and Delon, Julie and Veit, Thomas. ["FastDVDnet: Towards Real-Time Video Denoising Without Explicit Motion Estimation", arXiv preprint arXiv:1907.01361 (2019).](https://arxiv.org/abs/1907.01361)

## Video Examples

You can download several denoised sequences with our algorithm and other methods [here](https://www.dropbox.com/sh/m9mpz1m1b55x420/AAAt1wes43brv37BmBxw07jna?dl=0 "FastDVDnet denoised sequences")

## Running Times

FastDVDnet is orders of magnitude faster than other state-of-the-art methods
<img src="https://github.com/m-tassano/fastdvdnet/raw/master/runtimes.png" width=350>

## User Guide

The code as is runs in Python +3.6 with the following dependencies:

### Dependencies
* [PyTorch v1.0.0](http://pytorch.org/)
* [NVIDIA DALI](https://github.com/NVIDIA/DALI)
* [scikit-image](http://scikit-image.org/)
* [numpy](https://www.numpy.org/)
* [OpenCV](https://pypi.org/project/opencv-python/)
* [tensorboardX](https://github.com/lanpa/tensorboardX/)

Note: the tested version of NVIDIA DALI is 0.10.0. To install it (supposing you have CUDA 10.0), you need to run
```
pip install --extra-index-url https://developer.download.nvidia.com/compute/redist/cuda/10.0 nvidia-dali==0.10.0 
```
## Usage

### Testing

If you want to denoise an image sequence using the pretrained model you can execute

```
test_fastdvdnet.py \
	--test_path <path_to_input_sequence> \
	--noise_sigma 30 \
	--save_path results
```

**NOTES**
* The image sequence should be stored under <path_to_input_sequence>
* The model has been trained for values of noise in [5, 55]
* run with *--no_gpu* to run on CPU instead of GPU
* run with *--save_noisy* to save noisy frames
* set *max_num_fr_per_seq* to set the max number of frames to load per sequence
* to denoise _clipped AWGN_ run with *--model_file model_clipped_noise.pth*
* run with *--help* to see details on all input parameters

### Training

If you want to train your own models you can execute

```
train_fastdvdnet.py \
	--trainset_dir <path_to_input_mp4s> \
	--valset_dir <path_to_val_sequences> \
	--log_dir logs
```

**NOTES**
* As the dataloader in based on the DALI library, the training sequences must be provided as mp4 files, all under <path_to_input_mp4s>
* The validation sequences must be stored as image sequences in individual folders under <path_to_val_sequences>
* run with *--help* to see details on all input parameters


## ABOUT

Copying and distribution of this file, with or without modification,
are permitted in any medium without royalty provided the copyright
notice and this notice are preserved. This file is offered as-is,
without any warranty.

* Author    : Matias Tassano `mtassano at gopro dot com`
* Copyright : (C) 2019 Matias Tassano
* Licence   : GPL v3+, see GPLv3.txt

The sequences are Copyright GoPro 2018
# repaired_fastdvdnet
