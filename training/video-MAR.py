def MAR_video(file):
    smile_no = 0

    shape_predictor= "shape_predictor_68_face_landmarks.dat" 
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(shape_predictor)


    (mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]

    print("[INFO] starting video...")
    vs = cv2.VideoCapture(file)

    while(vs.isOpened()):
        ret, frame = vs.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)
        smile_no = smile_no + 1
        frame1 = frame.copy()
              
        for rect in rects:   
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)
            mouth= shape[mStart:mEnd]
            mar= smile(mouth)
            mouthHull = cv2.convexHull(mouth)
            cv2.drawContours(frame, [mouthHull], -1, (0, 255, 0), 1)
            
            if (mar < .25 or mar > .38):
                cv2.putText(frame,"Smile Detected",(10, 60), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 3, cv2.LINE_AA)       
                cv2.putText(frame,"Captured",(10, 120), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)
                img_name = "images/video_mar/mar_video_test_{}.png".format(smile_no)
                cv2.imwrite(img_name,frame1)
                  
            cv2.putText(frame, "MAR: {}".format(mar), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            
        cv2.imshow("Video Testing", frame)
        

        key2 = cv2.waitKey(1) & 0xFF
        if key2 == ord('q'):
            break


    cv2.destroyAllWindows()

    print("[INFO] video ended..")
    

videofile = 'dataset/videos/Make People Smile Project.mp4'
MAR_video(videofile)
