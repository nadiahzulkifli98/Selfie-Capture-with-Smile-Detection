#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 05:03:07 2020

@author: nadiahzulkifli
"""

#test image HAAR

import cv2
import numpy as np 
import os
import glob

eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')

pos_dir = 'dataset/positives/'
neg_dir = 'dataset/negatives/'


def HAAR_image(img, file):
    
    print("[INFO] Image " + file + "..")
            
    scale_percent = 200 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
                
    #smile  = smileCascade.detectMultiScale(
    #        img,
    #        scaleFactor= 1.5,
    #        minNeighbors=15,
    #        minSize=(25, 25),
    #        )
    
    smile  = smileCascade.detectMultiScale(img, scaleFactor = 1.8, minNeighbors = 20)
                
    for (sx, sy, sw, sh) in smile:
        cv2.rectangle(img, (sx, sy), ((sx + sw), (sy + sh)), (0, 255,0), 5)
        print("smile")
        file_split = file.split('/')
        print(file_split)
        file_split1 = file_split[2].split('.')
        #filename = 'images/haar-static/' + file_split1[0] + '.png'
        filename = 'images/haar-static-neg/' + file_split1[0] + '.png'
        cv2.imwrite(filename, resized_img)
        print("saved")

                
                
#to call files
#data_path = os.path.join(pos_dir, '*g') 
data_path = os.path.join(neg_dir, '*g') 

files = glob.glob(data_path)
data = [] 
for f1 in files: 
    image = cv2.imread(f1) 
    data.append(image)
    HAAR_image(image, f1)
    #print("test")


#cv2.destroyAllWindows()
print("[INFO] End of images...")