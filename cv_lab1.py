# -*- coding: utf-8 -*-
"""CV_Lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lG-ghdxnCWciVuoGgQjKYZwhkVdIxKQY
"""

from google.colab import drive
drive.mount('/content/gdrive')

"""2"""

import numpy as np
import cv2 

def go_fast(my_img):
    my_img.max()
    max = my_img.max()
    my_img.min()
    min = my_img.min()
    for i in range(my_img.shape[0]):
        for j in range(my_img.shape[1]):
            my_img[i, j] = (my_img[i, j]-min)/(max-min)*255
    return my_img

img = cv2.imread("Paris.jpeg", cv2.IMREAD_GRAYSCALE)
res1 = go_fast(img)

cv2_imshow(res1)
cv2.waitKey(0)

"""3"""

import numpy as np
import cv2
from numba import njit 
from google.colab.patches import cv2_imshow

@njit
def go_fast(my_img):
    my_img.max()
    max = my_img.max()
    my_img.min()
    min = my_img.min()
    for i in range(my_img.shape[0]):
        for j in range(my_img.shape[1]):
            my_img[i, j] = (my_img[i, j]-min)/(max-min)*255
    return my_img

img = cv2.imread("Paris.jpeg", cv2.IMREAD_GRAYSCALE)
res = go_fast(img)

cv2_imshow(res)
cv2.waitKey(0)