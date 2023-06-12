import math
import random
import time

from PyQt6.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.wins = 0
        self.ties = 0
        self.defeats = 0

        self.setWindowTitle("Rock, Paper, Scissors")

        self.result = QLabel("Press Rock, Paper, or Scissors!")
        self.stats = QLabel("See how much you can win!")

        self.buttonLayout = QHBoxLayout()

        self.rock = QPushButton("Rock")
        self.rock.pressed.connect(self.rockCall)

        self.paper = QPushButton("Paper")
        self.paper.pressed.connect(self.paperCall)

        self.scissors = QPushButton("Scissors")
        self.scissors.pressed.connect(self.scissorsCall)

        self.buttonLayout.addWidget(self.rock)
        self.buttonLayout.addWidget(self.paper)
        self.buttonLayout.addWidget(self.scissors)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.result)
        self.mainLayout.addWidget(self.stats)
        self.mainLayout.addLayout(self.buttonLayout)

        self.myWidget = QWidget()
        self.myWidget.setLayout(self.mainLayout)

        self.setCentralWidget(self.myWidget)
        self.show()

    def rockCall(self):
        self.turnHandler(input="rock")

    def paperCall(self):
        self.turnHandler(input="paper")

    def scissorsCall(self):
        self.turnHandler(input="scissors")

    def turnHandler(self, input):
        botPossible = ["rock", "paper", "scissors"]
        botInput = botPossible[math.floor(random.random() * 3)]
        if input == botInput:
            self.result.setText("It was a tie!")
            self.ties += 1
        elif input == "paper" and botInput == "rock":
            self.result.setText("You won!")
            self.wins += 1
        elif input == "rock" and botInput == "scissors":
            self.result.setText("You won!")
            self.wins += 1
        elif input == "scissors" and botInput == "paper":
            self.result.setText("You won!")
            self.wins += 1
        else:
            self.result.setText("You lost!")
            self.defeats += 1
        self.stats.setText(f"Wins: {self.wins}; Ties: {self.ties}; Defeats: {self.defeats}; Bot selection: {botInput}")


app = QApplication(sys.argv)
w = MainWindow()
app.exec()