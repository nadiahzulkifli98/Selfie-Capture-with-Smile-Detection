#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 23:27:31 2020

@author: nadiahzulkifli
@author: sabrinasyazwani
@author: puteriaisyah
"""

import time
import cv2
from scipy.spatial import distance as dist
from imutils import face_utils
import dlib

def haar_app(name):

    faceCascade = cv2.CascadeClassifier('classifierhaarcascade_frontalface_default.xml')
    smileCascade = cv2.CascadeClassifier('classifier/haarcascade_smile.xml')
     
    #print("[INFO] starting video stream thread...")
    cap = cv2.VideoCapture(0)
    
    counter = 0
    selfie_no = 0
    
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,      
            minSize=(30, 30)
        )
    
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
            roi_gray = gray[y:y+h, x:x+w]
                    
            smile = smileCascade.detectMultiScale(
                roi_gray,
                scaleFactor= 1.5,
                minNeighbors=15,
                minSize=(25, 25),
                )
            
            for i in smile:
                if len(smile)>1.97:
                    cv2.putText(img,"Smile Detected",(x-30,y-30),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),3,cv2.LINE_AA)
                    counter = counter + 1
                    
                    if counter > 20:
                        cv2.putText(img,"3",(10,90),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
                    
                    if counter > 40:
                        cv2.putText(img,"2",(30,90),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
                        
                    if counter > 60:
                        cv2.putText(img,"1",(50,90),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
                        
                    if counter > 80 :
                        ret, img1 = cap.read()   
                        cv2.putText(img,"Captured",(10, 120), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)
                    
                    if counter == 90 :
                        selfie_no = selfie_no+1
                        img_name = "images/haar_smart_selfie_{}.png".format(selfie_no)
                        time.sleep(2)
                        cv2.imwrite(img_name,img1)
                        counter = 0
                        
                else:
                    counter = 0
                    
                   
        cv2.imshow('Live Capture', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27: # press 'ESC' to quit
            break
    
    cap.release()
    cv2.destroyAllWindows()
    #print("[INFO] video stream ended..")
        
def mar_app(name):

    def smile(mouth):
        A = dist.euclidean(mouth[3], mouth[9])
        B = dist.euclidean(mouth[2], mouth[10])
        C = dist.euclidean(mouth[4], mouth[8])
        avg = (A+B+C)/3
        D = dist.euclidean(mouth[0], mouth[6])
        mar=avg/D
        return mar
    
    
    counter = 0
    selfie_no = 0
    
    shape_predictor= "classifier/shape_predictor_68_face_landmarks.dat" 
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(shape_predictor)
    
    
    (mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]
    vs = cv2.VideoCapture(0)
    
    while True:
        ret, frame = vs.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)
        for rect in rects:
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)
            mouth= shape[mStart:mEnd]
            mar= smile(mouth)
            mouthHull = cv2.convexHull(mouth)
            cv2.drawContours(frame, [mouthHull], -1, (0, 255, 0), 1)
           
    
            if mar <= .25 or mar > .38 :
                cv2.putText(frame,"Smile Detected",(10, 60), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 3, cv2.LINE_AA) 
                counter = counter + 1
                
                if counter > 20 :
                    cv2.putText(frame,"3",(10, 90), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 3, cv2.LINE_AA)
                    
                if counter > 40 :
                    cv2.putText(frame,"2",(30, 90), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 3, cv2.LINE_AA)
                    
                if counter > 60 :
                    cv2.putText(frame,"1",(50, 90), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 3, cv2.LINE_AA)
                
                if counter > 80 :
                    ret,frame1 = vs.read()     
                    cv2.putText(frame,"Captured",(10, 120), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 3, cv2.LINE_AA)
                    
                if counter == 90 :
                    selfie_no = selfie_no+1
                    img_name = "images/mar_smart_selfie_{}.png".format(selfie_no)
                    time.sleep(2)
                    cv2.imwrite(img_name,frame1)
                    counter = 0
                    
            else :
                counter = 0
    
            cv2.putText(frame, "MAR: {}".format(mar), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
        
        cv2.imshow('Live Capture', frame)
        
        k = cv2.waitKey(30) & 0xff
        if k == 27: # press 'ESC' to quit
            break
    
    vs.release()
    cv2.destroyAllWindows()
