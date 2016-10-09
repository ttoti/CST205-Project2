#
# * Title: project2.py
# * Abstract:
# * Authors: Andrew Diesh, Kieran Burke, Tomas Hernandez
# * Github url: https://github.com/ttoti/CST205-Project2

#!/usr/bin/env python3
import numpy as np
import cv2

#Defines camera to use
cap = cv2.VideoCapture(0)
#Creates BackgroundSubtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

#Workaround for OpenCV error
cv2.ocl.setUseOpenCL(False)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	if frame is not None:
	# Operations to add effects for detection
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#	fist = fist_cascade.detectMultiScale(gray, 1.2, 5)
		#if fist:
		#	for(x,y,w,h) in fist:
		#		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,170,0),2)
		blur = cv2.GaussianBlur(gray,(15,15),0)
		threshold = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
		fgmask = fgbg.apply(threshold)
		frame2, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		cv2.drawContours(threshold, contours, -1, (255,255,255), 3)
		# Display the resulting frame
		cv2.imshow('Foreground',fgmask)
		#cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
