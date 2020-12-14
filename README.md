# Selfie Capture with Smile Detection GUI-APP

PROJECT TITLE: Selfie Capture with Smile Detection

PURPOSE OF PROJECT: TDS 3651 - Visual Information Processing Project

VERSION or DATE: October 2020

# A very Simple Gui app for Selfie Capture with Smile Detection 

  - Detect smile using Haar Feature Selection
  - Detect smile using Mouth Aspect Ratio (MAR) 
  - Capture image and save to file.
  
# Installation

1 : Install the requirements.

```sh
$ pip install -r  requirements.txt
```

2 : Run The App 

```sh
$ python selfie-capture-smile-detection.py
```

# APP GUI

- Home Page <br>
- Camera <br>
- Haar Feature Selection<br>
- Mouth Aspect Ratio (MAR)<br><br>

This is a project for TDS 3651 - Visual Information Processing under Multimedia University courses.<br><br>

AUTHORS:

Nur Sabrina Syazwani binti Mazlan
Nurul Nadiah binti Zulkifli
Puteri Aisyah binti Megat Muzafar
INSTITUTION: Multimedia University

1. ABSTRACT
A smile represents satisfaction and happiness. Many applications are created using smile detection technology, for example product rating, patient monitoring, image capturing, video conferencing and interactive systems. In this project, we focused on how to apply smile detection for image capturing specifically for selfie capture and to compare which methods perform better at smile detection by measuring the accuracy, precision, recall, and F1-score. Methods used for this project are Haar Feature Selection and Mouth Aspect Ratio (MAR). Both methods were tested by using datasets of images, videos and real-time webcam. The comparison for both methods was evaluated based on the evaluation metrics. The results showed that MAR is generally better at detecting a smile on non-static images compared to Haar. However, both methods did not perform well at detecting smiles for static images. Nonetheless, they showed good results on capturing selfies using the real-time webcam. Some improvements could be made to improve the performance for both methods, such as the features used and haarcascades values for Haar, as well as the threshold values set for MAR.

2. INTRODUCTION
In this modern day and age, smartphones play a crucial role in taking pictures. Less and less people have a tendency to bring around their cameras as smartphones are generally a “one size fits all” in terms of having a lot of similar uses to those of a camera. For example, pictures taken from a smartphone could sometimes beat those of a professional camera, plus they are much cheaper too than some. In addition, smartphones are much more used due to the presence of a front and back camera that enables users to take pictures from both angles. The front camera in a smartphone is especially used for “selfies” or also known as self-portraits. It could also capture a photo full of people for a family photo, friendship photo and others. Selfies are taken while one extends their arm at a certain position to get the best view of one-self. Then, it is continued by clicking the button on the phone to take the picture. Therefore, this sometimes limits the outcome of the picture. It is very difficult for people to hold the phone while simultaneously taking the picture. The image may get blurry due to the movement of the hand during the clicking of the button. Furthermore, sometimes the images taken do not capture the people at their best. One may be smiling while another does not. Henceforth, the computer vision that will be investigated is smile detection. With smile detection, the camera will only capture the image once everyone detected inside the image is smiling. Consequently, the perfect photo with no blurry areas and with every person smiling will be taken.

3. APPROACH
OpenCV is an open source computer vision library for commercial and research use. It is one of the most widely used libraries in image processing. The OpenCV was chosen for its extensive library, simple usage and extensive user network. Our study is to compare two existing algorithms which Haar Feature Selection [4] and Mouth Aspect Ratio [5].

3.1. Mouth Aspect Ratio (MAR) Technique
3.1.1. Library Required
numpy: Used for fast matrix calculations and manipulations.
dlib: Library containing the facial landmarks.
cv2: The OpenCV library used for image manipulation and saving.
scipy.spatial: Used to calculate the Euclidean distance between facial points.
imutils: Library to access video streams.
3.1.2. Facial Landmark Detector in dlib
This study will be using the facial landmarks detector from dlib to get the mouth coordinates. The facial landmark detector is an API implemented inside dlib. It produces 68 x- y-coordinates that map to specific facials including eyes, jaws, nose and mouth structures. We will focus on the mouth which can be accessed through point range [49,…, 68]. There are twenty coordinates for mouth structure.

3.1.3. MAR Computation
This technique proposes to compute the distance between point 49 and point 55 as D, and calculate the average of the distances between:

point 51 and point 59
point 52 and point 58
point 53 and point 57 Let’s call it L, using the same naming structure: Hence, MAR = L/D The ratio for the smile detector will be influenced by how an individual will be smiling. Smiling with the mouth closed will increase the distance between point 49 and point 55 and decrease the distance between the top and bottom points. So, L will decrease. Smiling with mouth open will lead to D decreasing and L increasing.
3.2. Haar Feature Selection Technique
3.2.1. Library Required
numpy: Used for fast matrix calculations and manipulations.
cv2: The OpenCV library used for image manipulation and saving.
3.2.2. Face Detection using Haar Feature Selection
The dataset of images will be including haar cascade files in the python file. The video that will be captured from the real-time camera is nothing but a series of images. Therefore, they will run as an infinite while-loop of images. The algorithm will read faces using an already included haarcascade file and detectMultiscale() function where the gray image, ScaleFactor, and minNeighbors will be passed.

ScaleFactor: Parameter specifying zoom image
minNeighbors: Parameter specifying how many neighbors each rectangle should have to retain it. Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images. Here, it will work with face detection. Initially, the algorithm needs a lot of positive images (images of faces) and negative images (images without faces) to train the classifier. Then, we need to extract features from it. If it detects a face, an outer boundary of the face will be drawn using rectangle() method of cv2. The method contains 5 arguments:
image: Image on which rectangle is to be drawn.
start_point: Starting coordinates of rectangle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
end_point: Ending coordinates of rectangle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
color: Color of border line of rectangle to be drawn.
thickness: Thickness of the rectangle border line in px. After the face is detected, the structure for the mouth hence a smile will be detected by using the smile haar cascade file that can be imported easily in the algorithm to detect smile in the dataset.
3.3. Auto Capture Image during Video Live Stream
The study will be using the VideoCapture() from OpenCV according to MAR values that will be set up and passed values to parameters of Haar detection function. Once the values meet the range of MAR and Haar detection function, the image will be auto captured and saved to the directory. Finally, the windows of the video streaming will be destroyed.

4. EXPERIMENT
For this project, we are comparing two existing algorithms which are by using Haar Feature Selection and Mouth Aspect Ratio (MAR) to determine which method will be implemented in the auto capture image during video live stream. We conducted a test for both approaches to analyse which methods perform better at smile detection by measuring the accuracy, precision, recall, and F1-score. The performance evaluation using confusion matrix is made in terms of achieving the best trade-off between correct detection and false detection during the testing of the dataset. After the testing is complete, live detection of smiles during a selfie will be implemented using a webcam in real-time. This is to test whether the algorithm works for both static and non-static images.

4.1. Dataset
To test the smile detector, the dataset that will be used is an existing dataset that consists of both smiling and not smiling images and video from all sets of gender including male and female. The purpose of collecting from different genders is to test the smile detector with contrasting types of smiles. Some smiles could be restrained but still considered as a smile according to the angle of the mouth, show of dental or the extent of their smiles. One of the datasets would be “SMILES” by Daniel Hromada in Github [6] that contains smiling and non-smiling grayscale images, focused on the crop of the face. The second dataset would be from the YouTube video, “Make People Smile Project," [7] that also contains people with smiling and non-smiling faces.

4.2. Haar Feature Selection
Haar Feature Selection is the first technique we used to test the images, video and live capture. For images, we used a smile haarcascade to only detect smiles as the images are zoomed into the face. For video, eye and smile haar cascade were used to detect a smile because it had better detection than a combination of face and smile haarcascade. Lastly, for the live capture, we used a face and smile haar cascade to detect a smile before the capture. The values for the haarcascades are as below:

Smile Haarcascade: scaleFactor = 1.5, minNeighbors = 15 minSize = (25, 25)

Face Haarcascade: scaleFactor = 1.3, minNeighbors = 5 minSize = (30, 30)

5. CONCLUSION
As a conclusion, this project was to capture a selfie with smile detection. Two methods were used which are Haar Feature Selection and Mouth Aspect Ratio (MAR). With good feature selections and threshold values for Haar and MAR respectively, both methods showed good results on capturing selfie using the real-time webcam. Meanwhile, these two methods were also compared to identify which method is more superior. From the tests conducted, MAR is generally better at detecting a smile. This is because it focuses on detecting the mouth figure on a person’s face, while Haar focuses on finding features using the right haarcascade values. However, Haar also proved to be a good method to detect smiles depending on the features selected, and MAR could be worse if the threshold value is not set accurately. Furthermore, from the tests conducted, Haar and MAR works better for non-static images when detecting a smile. In future works, Haar and MAR could be combined to get a higher performance in smile detection.

6. REFERENCES
[1] J. Whitehill, G. Littlewort, I. Fasel, M. Bartlett and J. Movellan, "Toward Practical Smile Detection," IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 31, no. 11, p. 2106, November 2009.

[2] C.-S. F. Yu-Hao Huang, "FACE DETECTION AND SMILE DETECTION," 2020.

[3] Winal Zikril Zulkifli, Syamimi Shamsuddin, Fairul Azni Jafar, Rabiah Ahmad, Azizah Abdul Manaf, Alaa Abdulsalam Alarood, Lim Thiam Hwee, "Smile Detection Tool using OpenCV-Python to Measure Response in Human-Robot Interaction with Animal Robot PARO," (IJACSA) International Journal of Advanced Computer Science and Applications, vol. 9, no. 11, 2018.

[4] DataFlair Team, "Python Project – Auto-capture Selfie by Detecting Smile," 18 August 2020. [Online]. Available: https://data-flair.training/blogs/python-project-capture-selfie-by-detecting-smile/.

[5] R. Agarwal, "Smilefie: how you can auto-capture selfies by detecting a smile," 7 August 2018. [Online]. Available: https://www.freecodecamp.org/news/smilfie-auto-capture-selfies-by-detecting-a-smile-using-opencv-and-python-8c5cfb6ec197/.

[6] Hromada, D, "SMILEsmileD," GitHub, 28 October 2010. [Online]. Available: https://github.com/hromi/SMILEsmileD.

[7] Huzeyfe Kurt, "Make People Smile Project," 15 May 2016. [Online]. Available: https://www.youtube.com/watch?v=8YuBxP4CKZc.

Note: "shape_predictor_68_face_landmarks.dat" is not included.
