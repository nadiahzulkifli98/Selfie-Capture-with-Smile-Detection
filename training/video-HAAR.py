def HAAR_video(file):
    frame_no = 0
    eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')
 
    print("[INFO] starting video stream thread...")
    cap = cv2.VideoCapture(file)

    
    while(cap.isOpened()):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        eyes = eyeCascade.detectMultiScale(gray)

        frame_no = frame_no + 1
        
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(gray,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
            smile = smileCascade.detectMultiScale(
                gray,
                scaleFactor= 1.5,
                minNeighbors=15,
                minSize=(25, 25),
                )

            for i in smile:
                if len(smile)>1.97:
                    cv2.putText(img,"Smile Detected",(10,90),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),3,cv2.LINE_AA)
                    ret, img1 = cap.read()
                    frame_no = frame_no + 1
                    cv2.putText(img,"Captured",(10, 120), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)
                    img_name = "images/video_haar/haar_video_test_{}.png".format(frame_no)
                    cv2.imwrite(img_name,img1)
                    

        cv2.imshow('Video Test', img)
        
        key2 = cv2.waitKey(1) & 0xFF
        if key2 == ord('q'):
            break

    cv2.destroyAllWindows()
    print("[INFO] video stream ended..")
    
video = 'dataset/videos/Make People Smile Project.mp4'
HAAR_video(video)
