#!/usr/local/bin/python3
#export PYTHONPATH=/usr/local/lib/python3.5/site-packages

import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget)
import time
class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()


    # write

    def timer(int): # 3 second countdown
        counter = 3;
        for i in range(0, 3):
            counter -= i
            print (counter)
            return
    print("Time's up")



    def init_ui(self):
        self.labelTitle = QLabel("Rock Paper Scissors Game: ")

        #self.labelTitle.move(0, 100)

        #self.label.move(0, 0)
        self.labelTimer = QLabel('Timer: ')

        self.labelP1Score = QLabel('Player 1 Score: ')
        self.labelP2Score = QLabel('Player 2 Score: ')
        #self.lableReset = QLabel('Reset game')
        self.label = QLabel('Choose a button, then click select ')
        # buttons
        self.start = QRadioButton('Start')
        self.stop = QRadioButton('Stop')
        #self.reset = QRadioButton('Reset')
        self.button = QPushButton('Select')


        layout = QVBoxLayout()
        layout.addWidget(self.labelTitle)
        layout.addWidget(self.labelTimer)
        layout.addWidget(self.labelP1Score)
        layout.addWidget(self.labelP2Score)
        layout.addWidget(self.start)
        layout.addWidget(self.stop)
        #layout.addWidget(self.reset)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setWindowTitle('Rock, Paper, Scissors')

        self.button.clicked.connect(lambda: self.btn_clk(self.start.isChecked(), self.label))
        #self.button.clicked.connect(self.reset_clck(self.reset.isChecked(), self.labelReset)
        self.show()

    def btn_clk(self, chk, label):
        if chk:
            label.setText('Get ready to play')
        else:
            label.setText('Game over.')

app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
