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
fgbg = cv2.createBackgroundSubtractorMOG2(history =2500)

#Workaround for OpenCV error
cv2.ocl.setUseOpenCL(False)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	if frame is not None:
	# Operations to add effects for detection
		
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		blur = cv2.GaussianBlur(gray,(11,11),0)
		ret, threshold = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
		
		fgmask = fgbg.apply(threshold)
		frame2, contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		max_area =0
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
		frame2 =np.zeros(frame.shape,np.uint8)
		cv2.drawContours(frame2,[cnt],0,(0,255,0),1)
		cv2.drawContours(frame2,[hull],0,(0,0,255),1)	
		
		hull=cv2.convexHull(cnt,returnPoints = False)
		defects = cv2.convexityDefects(cnt,hull)
		
		min =0
		max =0
		i =0
		for i in range(defects.shape[0]):
			s,e,f,d = defects[i,0]
			start = tuple(cnt[s][0])
			end = tuple(cnt[e][0])
			far = tuple(cnt[f][0])
			cv2.line(frame,start,end,[0,255,0],0)                
			cv2.circle(frame,far,5,[0,0,255],0)
			print(i)
		
		
			# Display the resulting frame
		
	cv2.imshow('mask',fgmask)
	cv2.imshow('frame',frame)
	cv2.imshow('thresh', threshold)
	if cv2.waitKey(1) & 0xFF == ord('q'):
			break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()