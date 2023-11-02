# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 8 - Loops
# Rock Paper Scissors (Second Iteration)
# Timestamp: 2:46:23

import sys
import random
from enum import Enum


# Rock Paper Scissors (Second Iteration)
class RPS(Enum):
    ROCK = 1  # Constant variables use all caps
    PAPER = 2
    SCISSORS = 3


playagain = True

while playagain == True:
    playerchoice = input('\nEnter...\n1 for Rock,\n2 for Paper, or\n3 for Scissors:\n\n')
    player = int(playerchoice)
    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")  # Don't forget to import sys

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

    question = input("\nPlay again?\nY for Yes or \nQ to Quit \n\n")
    print(question)
    if question.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        playagain = False  # break would also work here

sys.exit("Bye! 🙌")