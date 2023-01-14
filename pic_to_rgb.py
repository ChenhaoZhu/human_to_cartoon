import cv2
from PIL import Image
import matplotlib.pyplot as plt
import os
import numpy as np



# 批量转灰度图并保存
# crack文件夹下批量处理将灰度图转成RGB并保存

def convert2gray(filename):  # 定义灰度图转RGB图的函数
    img = cv2.imread(file_path + '/' + filename, 1)  # 1是以BGR图方式去读
    RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imwrite(out_path + filename, RGB_img)  # 保存在新文件夹下，且图名中加RGB


file_path = "D:\parcharm_project\Cycle_horse\datasets\horse2zebra\\train\B"  # 输入文件夹

out_path = "D:\parcharm_project\Cycle_horse\datasets\horse2zebra\\train\B/"  # 设置为新目录为输出文件夹

pic = os.listdir(file_path)

for ele in pic:
    convert2gray(ele)