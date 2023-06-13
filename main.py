import math
import random
import PySimpleGUI as sg

sg.theme("LightGrey2")

layout = [
    [sg.Text("Press Rock, Paper, or Scissors!", key="Main")],
    [sg.Text("See how much you can win!", key="Second")],
    [sg.Button("Rock"), sg.Button("Paper"), sg.Button("Scissors")]
]

wins = 0
ties = 0
defeats = 0

window = sg.Window("Rock, Paper, Scissors", layout)

botPossible = ["Rock", "Paper", "Scissors"]
while True:
    botChoice = botPossible[math.floor(random.random() * 3)]
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    elif event == "Rock":
        if botChoice == "Rock":
            window["Main"].update("It was a tie!")
            ties += 1
        elif botChoice == "Scissors":
            window["Main"].update("You won!")
            wins += 1
        else:
            window["Main"].update("You lost!")
            defeats += 1
        window["Second"].update(f"Wins: {wins}; Ties: {ties}; Defeats: {defeats}; Bot selection: {botChoice.lower()}")
    elif event == "Paper":
        if botChoice == "Rock":
            window["Main"].update("You won!")
            wins += 1
        elif botChoice == "Scissors":
            window["Main"].update("You lost!")
            defeats += 1
        else:
            window["Main"].update("It was a tie!")
            ties += 1
        window["Second"].update(f"Wins: {wins}; Ties: {ties}; Defeats: {defeats}; Bot selection: {botChoice.lower()}")
    elif event == "Scissors":
        if botChoice == "Rock":
            window["Main"].update("You lost!")
            defeats += 1
        elif botChoice == "Scissors":
            window["Main"].update("It was a tie!")
            ties += 1
        else:
            window["Main"].update("You won!")
            wins += 1
        window["Second"].update(f"Wins: {wins}; Ties: {ties}; Defeats: {defeats}; Bot selection: {botChoice.lower()}")

window.close()