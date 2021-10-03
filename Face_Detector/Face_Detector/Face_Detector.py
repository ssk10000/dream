import cv2
from random import randrange

#load pre trained data from open cv
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# choose an image
img = cv2.imread('RD3.jpg')
#img = cv2.imread('ii.jpg')
# Must convert to gray scale
#webcam = cv2.VideoCapture(0)
while True:
	#succesful_frame_read, frame = webcam.read()
	greyscaled_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)
	for(x,y,w,h) in face_coordinates:
		cv2.rectangle(img,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),2)
	cv2.imshow('Face Detector',img)
	key = cv2.waitKey(1)

	if key == 81 or key == 113:
		break

print(cv2.__version__)

