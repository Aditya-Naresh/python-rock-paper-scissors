import math
import random


def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    index = math.floor(random.randint(0, 2))
    return choices[index]


def play_round(computer_choice, player_choice):
    if (player_choice == "Rock" and computer_choice == "Paper") or \
            (player_choice == "Paper" and computer_choice == "Scissors") or \
            (player_choice == "Scissors" and computer_choice == "Rock"):
        result = "You Lose! " + computer_choice + " beats " + player_choice
        print(result)
    elif (player_choice == "Paper" and computer_choice == "Rock") or \
            (player_choice == "Scissors" and computer_choice == "Paper") or \
            (player_choice == "Rock" and computer_choice == "Scissors"):
        result = "You Win! " + player_choice + " beats " + computer_choice
        print(result)
    else:
        result = "It's a tie"
        print(result)


computer_choice = get_computer_choice()
play_round(computer_choice, "Rock")