#
# * Title: project2.py
# * Abstract: Using openCV and PyQT, we are making a version of rock paper scissors that uses coutours
# *				to determine what shape 2 players pick
# * Authors: Andrew Diesh, Kieran Burke, Tomas Hernandez
# * Github url: https://github.com/ttoti/CST205-Project2

#!/usr/bin/env python3
import numpy as np
import cv2

#Defines camera to use
cap = cv2.VideoCapture(0)
#Creates BackgroundSubtractor
fgbg = cv2.createBackgroundSubtractorMOG2(history = 2500)
#Workaround for OpenCV error
cv2.ocl.setUseOpenCL(False)

def mainProgram():
	while(True):
		# Capture frame-by-frame
		ret, frame = cap.read()
		if frame is not None:
		# Operations to add effects for BackgroundSubtractor
			cv2.rectangle(frame,(400,400),(100,100),(0,255,0),0)
			cv2.rectangle(frame,(1100,400),(800,100),(0,255,0),0)

			##Crop image to get contours of each
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			blur = cv2.GaussianBlur(gray,(15,15),0)
			ret, threshold = cv2.threshold(blur,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
			fgmask = fgbg.apply(threshold)
			#threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

			#Apply mask
			#fgmask = fgbg.apply(threshold)
			crop_img2 = fgmask[100:400, 100:400]
			crop_img = fgmask[100:400, 800:1100]
			#Find contours then draws
			#frame2, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
			#cv2.drawContours(threshold, contours, -1, (255,255,255), 3)

			# Display the resulting frame
			#cv2.imshow('Foreground',threshold)

			#getContours(crop_img)
			#getContours(crop_img2)
			cv2.imshow('frame', getContours(crop_img))
			#cv2.imshow('frame2', getContours(crop_img2))
			cv2.imshow('main', frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()

def getContours(cropped_image):
	#This function currently doesn't work properly
	frame2, contours, hierarchy = cv2.findContours(cropped_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	max_area =0
	ci = 1
	if(len(contours) >= 0):
		#hull(redline)
		for i in range(len(contours)):
			cnt = contours[i]
			area = cv2.contourArea(cnt)
			if(area > max_area):
				max_area = area
				ci=i

	cnt = contours[ci]
	hull =cv2.convexHull(cnt)
	frame2 =np.zeros(cropped_image.shape,np.uint8)
	cv2.drawContours(cropped_image,[cnt],0,(0,255,0),1)
	cv2.drawContours(cropped_image,[hull],0,(0,0,255),1)

	hull=cv2.convexHull(cnt,returnPoints = False)
	defects = cv2.convexityDefects(cnt,hull)

	i = 0
	for i in range(defects.shape[0]):
		s,e,f,d = defects[i,0]
		start = tuple(cnt[s][0])
		end = tuple(cnt[e][0])
		far = tuple(cnt[f][0])
		cv2.line(cropped_image,start,end,[0,255,0],0)
		cv2.circle(cropped_image,far,5,[0,0,255],0)
		print(i)
	return cropped_image

mainProgram()
