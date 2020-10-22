#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 02:56:00 2020

@author: nadiahzulkifli
"""

#test image MAR

from scipy.spatial import distance as dist
from imutils import face_utils
import imutils
import numpy as np
import time
import dlib
import cv2
import os
from os import listdir
import glob

def smile(mouth):
    A = dist.euclidean(mouth[3], mouth[9])
    B = dist.euclidean(mouth[2], mouth[10])
    C = dist.euclidean(mouth[4], mouth[8])
    avg = (A+B+C)/3
    D = dist.euclidean(mouth[0], mouth[6])
    mar=avg/D
    return mar

pos_dir = 'dataset/positives/'
neg_dir = 'dataset/negatives/'

def MAR_image(img, file):
    
    print("[INFO] Image " + file + "..")
            
    scale_percent = 200 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    shape_predictor= "shape_predictor_68_face_landmarks.dat" 
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(shape_predictor)

    (mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]


    #for i in range(len(path)):
        #gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    rects = detector(resized_img, 0)

    for rect in rects:
        print("mouth")
        shape = predictor(resized_img, rect)
        shape = face_utils.shape_to_np(shape)
        mouth= shape[mStart:mEnd]
        mar= smile(mouth)
        mouthHull = cv2.convexHull(mouth)
        #cv2.drawContours(resized_img, [mouthHull], -1, (0, 255, 0), 1)

        if mar <= .25 or mar > .38 :  
            print("smile")
            #cv2.putText(resized_img,"SMILE",(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            #save each images
            file_split = file.split('/')
            file_split1 = file_split[2].split('.')
            #filename1 = filter_img_dir + file_split1[0] + '.png'
            #filename = 'images/mar-static/' + file_split1[0] + '.png'
            filename = 'images/mar-static-neg/' + file_split1[0] + '.png'
            cv2.imwrite(filename, resized_img)
            print("Saved")

            #return resized_img


        #cv2.imshow("Image Smile", resized_img)
        #key2 = cv2.waitKey(1) & 0xFF
        #if key2 == ord('q'):
            #break


#to call all image files from positive dataset 
#data_path = os.path.join(pos_dir, '*g') 
data_path = os.path.join(neg_dir, '*g') 

files = glob.glob(data_path)
data = [] 
for f1 in files: 
    image = cv2.imread(f1) 
    data.append(image)
    MAR_image(image, f1)
    #print("test")


#cv2.destroyAllWindows()
print("[INFO] End of images...")