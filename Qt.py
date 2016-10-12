#!/usr/local/bin/python3
#export PYTHONPATH=/usr/local/lib/python3.5/site-packages

import sys
<<<<<<< HEAD
from PyQt5.QtWidgets import * #(QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QWidget)
#from PyQt5.QtCore import * #(QTimer, QTime)
from PyQt5 import QtCore
from time import strftime
from PyQt5 import QtGui


#from PyQt5 import QtCore
=======
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QHBoxLayout,QVBoxLayout, QApplication, QWidget)
>>>>>>> b1435a69a8d7fa2170c96f0c17e125fbc0529cc6
import time
class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()


    # write

<<<<<<< HEAD
    def start_clicked(self): # 3 second countdown
=======
    def timer(int): # 3 second countdown
        counter = 3
        for i in range(0, 3):
            counter -= i
            print (counter)
            return
    print("Time's up")
>>>>>>> b1435a69a8d7fa2170c96f0c17e125fbc0529cc6

        #self.label.setText("Get ready to play")

        #self.timer = QTimer()

<<<<<<< HEAD

        self.counter = 0
        self.progress.setValue(self.counter)
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
=======
    def init_ui(self):
        self.labelTitle = QLabel("Rock Paper Scissors Game: ")
>>>>>>> b1435a69a8d7fa2170c96f0c17e125fbc0529cc6
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
<<<<<<< HEAD


        self.label = QLabel('Press start to play, stop to quit')
        # buttons
=======
        #self.labelP2Score.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        #self.lableReset = QLabel('Reset game')
        self.label = QLabel('Choose a button, then click select ')
        # buttons
        self.score1 = QLabel('0')
        self.score2 = QLabel('0')
        self.start = QRadioButton('Start')
        self.stop = QRadioButton('Stop')
        #self.reset = QRadioButton('Reset')
        self.button = QPushButton('Select')
>>>>>>> b1435a69a8d7fa2170c96f0c17e125fbc0529cc6

        scoreLabel = QHBoxLayout()
        buttonLabelBox = QHBoxLayout()
        currentScoreLabel = QHBoxLayout()
        #scoreLabel.addStretch()
        scoreLabel.addWidget(self.labelP1Score)
        scoreLabel.addWidget(self.labelP2Score)
        scoreLabel.setSpacing(100)

        currentScoreLabel.addWidget(self.score1)
        currentScoreLabel.addWidget(self.score2)
        #currentScoreLabel.setSpacing(1)

        buttonLabelBox.addWidget(self.start)
        buttonLabelBox.addWidget(self.stop)
        #buttonLabelBox.setSpacing(1)

<<<<<<< HEAD
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
=======
        layout = QVBoxLayout()
        #layout.setSpacing(1)
        layout.addWidget(self.labelTitle)
        layout.addWidget(self.labelTimer)
        layout.addLayout(scoreLabel)
        layout.addLayout(currentScoreLabel)
        layout.addLayout(buttonLabelBox)
    #    layout.addWidget(self.start)
    #    layout.addWidget(self.stop)
>>>>>>> b1435a69a8d7fa2170c96f0c17e125fbc0529cc6
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

app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
