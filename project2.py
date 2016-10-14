#
# * Title: project2.py
# * Abstract: Using openCV and PyQT, we are making a version of rock paper scissors that uses coutours
# *				to determine what shape 2 players pick
# * Authors: Andrew Diesh, Kieran Burke, Tomas Hernandez
# * Github url: https://github.com/ttoti/CST205-Project2
# * Made using:
#http://docs.opencv.org/3.1.0/d4/d73/tutorial_py_contours_begin.html
#http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contours_more_functions/py_contours_more_functions.html
#http://docs.opencv.org/trunk/d1/dc5/tutorial_background_subtraction.html
#https://www.youtube.com/watch?v=OkHkuT59Rw0
#https://www.youtube.com/watch?v=NbXez-lixP0
# * Work file for Tomas Hernandez

#!/usr/bin/env python3
import numpy as np
import cv2
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
import sys

#Tomas and Kieran did the opencv work, we tried different approaches to see which worked best.
#this is a combination of the work 
# Andrew: worked with PyQt5. created a window with a labels, and a start and stop button. 
#Opens the camera
class CameraDetection():

	frame = None
	def mainProgram():

		cap = cv2.VideoCapture(0)
#Creates a mask made for background subtraction with a faster refresh rate
		fgbg = cv2.createBackgroundSubtractorMOG2(history = 1000)
		cv2.ocl.setUseOpenCL(False)

		firstCropXAxis = 100
		firstCropYAxis = 100
		secondCropXAxis = 700
		secondCropYAxis = 100

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
				fgmask = fgbg.apply(threshold)

				#Crops the image to find different Regions of Interest
				crop_img2 = fgmask[100:600, 100:600]
				crop_img = fgmask[100:600, 700:1200]

				firstImageArray = CameraDetection.getContours(crop_img, frame, firstCropXAxis, firstCropYAxis)
				secondImageArray = CameraDetection.getContours(crop_img2, frame, secondCropXAxis, secondCropXAxis)

				#Shows cropped image as a frame
				#cv2.imshow('crop_img', firstImageArray[0])
				#cv2.imshow('crop_img2',secondImageArray[0])
				#vis = np.concatenate((firstImageArray[2],secondImageArray[2]), axis = 0)

				cv2.imshow('frame',frame)
				print(secondImageArray[1])
				print(firstImageArray[1])
				#cv2.imshow('thresh', threshold)
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break

		# When everything done, release the capture
		cap.release()

		cv2.destroyAllWindows()

	def getFrame():
		return self.frame

	def getContours(cropped_image, frame, xAxis, yAxis):

		payload = []
		frame2, contours, hierarchy = cv2.findContours(cropped_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		max_area = 0
		cnt = 0
#once we have our contours we draw a hull around them
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
			cv2.drawContours(frame2,[cnt],0,(0,255,0), 1)#offset = (xAxis, yAxis))
			cv2.drawContours(frame2,[hull],0,(0,0,255), 1)#offset = (xAxis, yAxis))

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
			print("")

		payload.append(cropped_image)
		payload.append(len(contours))
		payload.append(frame)
		#print(payload[1])
		return payload
#Andrew did all of the QT work
class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()


    def start_clicked(self): #when user clicks the start button
        self.counter = 0
        self.progress.setValue(0)
        self.progress.reset()

        while self.counter < 100: # timer going from 0-100 for the progress barr
            print (self.counter)

            self.counter += .01
            self.progress.setValue(self.counter)
        self.label.setText("Time's up") # print message when finished. 

    def stop_clicked(self):
        self.progress.reset()
        while self.counter >= 0:
            print (self.counter)
            self.counter -= 0.01
        self.label.setText("Game over. Thank you for playing.")


    def init_ui(self):
        self.setGeometry(0,0,600,500)

        self.labelTimer = QLabel('Timer: ') # labels for our window

        self.timer = QtCore.QTimer(self)
        self.timer.start(3)


        self.labelP1Score = QLabel('Player 1 Score: ')
        self.labelP2Score = QLabel('Player 2 Score: ')


        self.label = QLabel('Press start to play, stop to quit')


        self.start = QPushButton('Start', self) #our buttons
        self.stop = QPushButton('Stop', self)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)
        self.progress.move(300, 200)
		
		# our layout. scoreLabel, buttonLabelBox, currentScoreLabel, progressBar are displayed horizontally. 
		scoreLabel = QHBoxLayout()
        buttonLabelBox = QHBoxLayout()
        currentScoreLabel = QHBoxLayout()
        progressBar = QHBoxLayout()

        scoreLabel.addWidget(self.labelP1Score)
        scoreLabel.addWidget(self.labelP2Score)
        scoreLabel.setSpacing(100)
		
		#display or progess bar or timer vertically.
        vbox = QVBoxLayout()
        vbox.addWidget(self.labelTimer)
        vbox.addWidget(self.progress)

        hbox = QHBoxLayout()
        hbox.addWidget(self.labelP1Score)
        self.score1 = QLabel('0')

        hbox.addWidget(self.labelP2Score)
        self.score2 = QLabel('0')
        hbox.addWidget(self.start)
        hbox.addWidget(self.stop)


        vbox.addLayout(hbox)
        self.setLayout(vbox)


        vbox.addWidget(self.label)
        self.setLayout(hbox)

        self.setGeometry(500, 500, 250, 250)
        self.setWindowTitle('Rock, Paper, Scissors')


        self.stop.clicked.connect(self.stop_clicked)

        self.start.clicked.connect(self.start_clicked)
        self.show()

    def trackScore(user_choice1, user_choice2): # determine who won after 3 games. 
        player1Score = 0
        player2Score = 0


        paper = "Paper"
        rock = "Rock"
        scissors = "Scissors"


        for i in range (0, 3): # best of 3 games.
            #increment score based off these

            if (user_choice1[i] == "Rock" and user_choice2[i] == "Scissors"):
                print ("Rock")
                player1Score += 1# if player1 has rock and player2 has scissors
                print (player1Score)
                print (player2Score)
            elif(user_choice1[i] == "Paper" and user_choice2[i] == "Rock"):
                print ("Paper")
                player1Score += 1 # else if player1 has paper and player2 has rock
                print (player1Score)
                print (player2Score)
            elif(user_choice1[i] == "Scissors" and user_choice2[i] == "Paper"):
                print ("Scissors")
                player1Score += 1 # else if player1 has scissors and player2 has paper
                print (player1Score)
                print (player2Score)
            elif(user_choice2[i] == "Rock" and user_choice1[i] == "Scissors"):
                print ("Rock")
                player2Score += 1 # else if player2 has rock and player1 has scissors
                print (player1Score)
                print (player2Score)
            elif(user_choice2[i] == "Paper" and user_choice1[i] == "Scissors"):
                print ("Paper")
                player2Score += 1 # else if player2 has paper and player1 has rock
                print (player1Score)
                print (player2Score)
            elif(user_choice2[i] == "Scissors" and user_choice1[i] == "Paper"):
                print ("Scissors")
                player2Score += 1 # else if player2 has scissors and player2 has paper
            # else, both player 1 and player2 used the same move
                print (player1Score)
                print (player2Score)
            else:
                print ("Player 1 and 2 used the same move")
                print (player1Score)
                print (player2Score)

        # to determine who won the game.
        if (player1Score > player2Score):
            print ("Player 1 wins!")
        elif (player1Score < player2Score):
            print ("Player 2 wins!")
        else:
            print ("It's a tie.")


print("What part of the program would you like to run?")
print("\t a. OpenCV")
print("\t b. PyQt")
inputNum = input("Enter choice: ")
if(inputNum == "a"): CameraDetection.mainProgram()
elif(inputNum == "b"):
	app = QApplication(sys.argv)
	a_window = Window()
	sys.exit(app.exec_())
else:
	print("Not a valid number. Try again")
