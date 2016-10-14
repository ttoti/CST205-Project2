#
# * Title: project2.py
# * Abstract: Using openCV and PyQT, we are making a version of rock paper scissors that uses coutours
# *				to determine what shape 2 players pick
# * Authors: Andrew Diesh, Kieran Burke, Tomas Hernandez
# * Github url: https://github.com/ttoti/CST205-Project2
# * Work file for Tomas Hernandez

#!/usr/bin/env python3
import numpy as np
import cv2

#Defines camera to use
cap = cv2.VideoCapture(0)

#Creates BackgroundSubtractor #Uncomment for to apply mask
#fgbg = cv2.createBackgroundSubtractorMOG2(history =5000)

#Workaround for OpenCV error #Uncomment for to apply mask
#cv2.ocl.setUseOpenCL(False)

def mainProgram():
	while(True):
		# Capture frame-by-frame
		ret, frame = cap.read()
		if frame is not None:

			#Renders rectangles to show where to place hands
			cv2.rectangle(frame,(600,600),(100,100),(0,255,0),0)
			cv2.rectangle(frame,(1200,600),(700,100),(0,255,0),0)

			#Applys filters to getContours
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			blur = cv2.GaussianBlur(gray,(11,11),0)
			ret, threshold = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

			#Apply mask #Uncomment for to apply mask
			#fgmask = fgbg.apply(threshold)

			#Crops the image
			crop_img2 = threshold[100:600, 100:600]
			crop_img = threshold[100:600, 700:1200]

			firstImageArray = getContours(crop_img, frame)
			secondImageArray = getContours(crop_img2, frame)

			#Shows cropped image as a frame
			cv2.imshow('crop_img', firstImageArray[0])
			cv2.imshow('crop_img2',secondImageArray[0])

			cv2.imshow('frame',frame)
			#cv2.imshow('thresh', threshold)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

	# When everything done, release the capture
	cap.release()

	cv2.destroyAllWindows()

#Runs in main program, returns an array in order of cropped_image,count of contours, and frame
def getContours(cropped_image, frame):

	payload = []
	frame2, contours, hierarchy = cv2.findContours(cropped_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	max_area = 0
	cnt = 0

	try:
		#hull(redline)
		for i in range(len(contours)):
			cnt = contours[i]
			area = cv2.contourArea(cnt)
			if(area > max_area):
				max_area = area
				ci=i

		cnt = contours[ci]
		hull =cv2.convexHull(cnt)
		frame2 =np.zeros(frame.shape,np.uint8)
		cv2.drawContours(frame2,[cnt],0,(0,255,0),1)
		cv2.drawContours(frame2,[hull],0,(0,0,255),1)

		hull=cv2.convexHull(cnt,returnPoints = False)
		defects = cv2.convexityDefects(cnt,hull)

		min = 0
		max = 0
		i = 0
		for i in range(defects.shape[0]):
			s,e,f,d = defects[i,0]
			start = tuple(cnt[s][0])
			end = tuple(cnt[e][0])
			far = tuple(cnt[f][0])
			cv2.line(frame,start,end,[0,255,0],2)
			cv2.circle(frame,far,5,[0,0,255],-1)
			#print(i)

	except:
		print("oops")

	payload.append(cropped_image)
	payload.append(cnt)
	payload.append(frame)

	return payload
mainProgram()
