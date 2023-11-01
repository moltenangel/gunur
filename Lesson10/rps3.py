# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 10 - Recursion
# Timestamp: 3:23:48
# Recursion is when a function calls itself

import sys
import random
from enum import Enum


def play_rps():
    # Rock Paper Scissors (Third iteration)
    class RPS(Enum):
        ROCK = 1  # Constant variables use all caps
        PAPER = 2
        SCISSORS = 3

    playerchoice = input('\nEnter...\n1 for Rock,\n2 for Paper, or\n3 for Scissors:\n\n')
    if playerchoice not in ["1","2","3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("You chose " + str(RPS(player)).replace('RPS.', '').title() + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '').title() + ".\n")

    # Windows Key + "." = Emoji selection window

    if player == 1 and computer == 3:
        print("🎉 You win!")
    elif player == 2 and computer == 1:
        print("🎉 You win!")
    elif player == 3 and computer == 2:
        print("🎉 You win!")
    elif player == computer:
        print("😲 Tie game!")
    else:
        print("🐍 Python wins!")

    print("\nPlay again?")

    while True:
        question = input("\nY for Yes or \nQ to Quit\n")
        if question.lower()    not in ["y","q"]:
            continue  # Starts the loop again asking for "y" or "n"
        else:
            break  # the loop stops
    if question.lower() == "y":
        play_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 🙌")


if __name__ == '__main__':
    play_rps()
