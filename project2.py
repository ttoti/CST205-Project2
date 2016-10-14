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

class CameraDetection():

	frame = None
	def mainProgram():

		cap = cv2.VideoCapture(0)

		fgbg = cv2.createBackgroundSubtractorMOG2(history =5000)
		cv2.ocl.setUseOpenCL(False)

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

				#Crops the image
				crop_img2 = fgmask[100:600, 100:600]
				crop_img = fgmask[100:600, 700:1200]

				firstImageArray = CameraDetection.getContours(crop_img, frame)
				secondImageArray = CameraDetection.getContours(crop_img2, frame)

				#Shows cropped image as a frame
				#cv2.imshow('crop_img', firstImageArray[0])
				#cv2.imshow('crop_img2',secondImageArray[0])

				cv2.imshow('frame',frame)
				#cv2.imshow('thresh', threshold)
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break

		# When everything done, release the capture
		cap.release()

		cv2.destroyAllWindows()

	def getFrame():
		return self.frame

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
		payload.append(len(contours))
		payload.append(frame)
		#print(payload[1])
		return payload

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    # write

    def start_clicked(self): # 3 second countdown

        #self.label.setText("Get ready to play")

        #self.timer = QTimer()


        self.counter = 0
        self.progress.setValue(0)
        #self.timer.start(3)
        self.progress.reset()

        while self.counter < 100:
            print (self.counter)

            self.counter += .01
            self.progress.setValue(self.counter)
            #if (self.counter == )
        self.label.setText("Time's up")
        #trackScore()

    #print("Time's up")
    """
    def start_clock(self):
        self.counter = 3
        #self.timer.start(3)
        while self.counter > 0:
            if self.counter > 0:
                time.sleep(1)
                print (self.counter)
                self.counter -= 1
            if self.counter == 0:
                print("Time's up")
        #trackScore()
    """
    #print("Time's up")
    def stop_clicked(self):
        self.progress.reset()
        #self.counter = 100
        while self.counter >= 0:
            print (self.counter)
            self.counter -= 0.01
        self.label.setText("Game over. Thank you for playing.")


    def init_ui(self):
        #self.labelTitle = QLabel("Rock Paper Scissors Game: ")
        self.setGeometry(0,0,600,500)
        #self.labelTitle.move(0, 100)

        #self.label.move(0, 0)
        self.labelTimer = QLabel('Timer: ')

        self.timer = QtCore.QTimer(self)
        #self.timer.timeout.connect(self.start_clicked)
        self.timer.start(3)
        #self.lcd = QtGui.QLCDNumber(self)


        self.labelP1Score = QLabel('Player 1 Score: ')
        self.labelP2Score = QLabel('Player 2 Score: ')


        self.label = QLabel('Press start to play, stop to quit')
        # buttons


        self.start = QPushButton('Start', self)
        self.stop = QPushButton('Stop', self)
        #self.reset = QRadioButton('Reset')
        #self.button = QPushButton('Select')
        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)
        self.progress.move(300, 200)

        scoreLabel = QHBoxLayout()
        buttonLabelBox = QHBoxLayout()
        currentScoreLabel = QHBoxLayout()
        progressBar = QHBoxLayout()

        scoreLabel.addWidget(self.labelP1Score)
        scoreLabel.addWidget(self.labelP2Score)
        scoreLabel.setSpacing(100)

        vbox = QVBoxLayout()
        #vbox.addWidget(self.labelTitle)
        vbox.addWidget(self.labelTimer)
        #vbox.
        vbox.addWidget(self.progress)
        #vbox.addLayout(vbox)
        #.addLayout(hbox)
        #vbox.addWidget(self.labelP1Score)
        #vbox.addWidget(self.labelP2Score)
        #vbox.addWidget(self.start)
        #vbox.addWidget(self.stop)
        #layout.addWidget(self.reset)
        #layout.addWidget(self.button)

        hbox = QHBoxLayout()
        hbox.addWidget(self.labelP1Score)
        self.score1 = QLabel('0')

        hbox.addWidget(self.labelP2Score)
        self.score2 = QLabel('0')
        hbox.addWidget(self.start)
        #hbox.addStretch(1)
        hbox.addWidget(self.stop)


        vbox.addLayout(hbox)
        self.setLayout(vbox)


        vbox.addWidget(self.label)
        #self.setLayout(vbox)
        self.setLayout(hbox)

        self.setGeometry(500, 500, 250, 250)
        self.setWindowTitle('Rock, Paper, Scissors')


        self.stop.clicked.connect(self.stop_clicked)
        #self.button.clicked.connect(lambda: self.btn_clk(self.start.isChecked(), self.label))
        #self.button.clicked.connect(self.reset_clck(self.reset.isChecked(), self.labelReset)
        #self.button.clicked.connect(self.timer)


        #self.progress.move(200, 400)
        self.start.clicked.connect(self.start_clicked)
        self.show()

    def trackScore(user_choice1, user_choice2):
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

CameraDetection.mainProgram()
#app = QApplication(sys.argv)
#a_window = Window()
#sys.exit(app.exec_())
