from math import log10, sqrt 
import cv2 
import numpy as np 
  
def PSNR(original, compressed): 
    mse = np.mean((original - compressed) ** 2) 
    if(mse == 0):  # MSE is zero means no noise is present in the signal . 
                  # Therefore PSNR have no importance. 
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse)) 
    return psnr 
  


def print_psnr(data_class,noisy):

    original = []
    compressed = []
    print(data_class,noisy)
    for i in range(25):
        original.append( cv2.imread(f"images/{data_class}/frame{i}.jpg") )
        compressed.append(cv2.imread(f"results/n{noisy}_FastDVDnet_{i}.png", 1)) 
    # print(original)
    value = 0
    for i in range(25):
        value += PSNR(original[i], compressed[i]) 
    value = value/25
    print(f"PSNR  value is {value} dB") 

    original = []
    compressed = []
    for i in range(25):
        original.append( cv2.imread(f"images/{data_class}/frame{i}.jpg") )
        compressed.append(cv2.imread(f"results/n{noisy}_{i}.png", 1)) 
    # print(original)
    nosiy_value = 0
    for i in range(25):
        nosiy_value += PSNR(original[i], compressed[i]) 
    nosiy_value = nosiy_value/25

    print(f"PSNR noisy value is {nosiy_value} dB") 