# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 5 - User Input
# Timestamp: 1:23:25

import sys
import random
from enum import Enum


def lesson5():
    # Rock Paper Scissors
    print("")
    playerchoice = input('Enter...\n1 for Rock,\n2 for Paper, or\n3 for Scissors:\n\n')
    player = int(playerchoice)
    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")  # Don't forget to import sys

    computerchoice = random.choice("123")
    computer = int(computerchoice)
    print("")  # Display numeric values
    print("You chose " + playerchoice + ".")
    print("Python chose " + computerchoice + ".")
    print("")

    class RPS(Enum):
        ROCK = 1  # Constant variables use all caps
        PAPER = 2
        SCISSORS = 3

    print("")  # Display Enum values
    print("You chose " + str(RPS(player)) + ".")
    print("Python chose " + str(RPS(computer)) + ".")
    print("")

    print("")  # Remove the classname from the output
    print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
    print("")

    print("")  # Convert to Title case for aesthetics
    print("You chose " + str(RPS(player)).replace('RPS.', '').title() + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '').title() + ".")
    print("")

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

    # Introduction to Enums
    # import command:
    # from enum import Enum
    # Included class RPS at beginning of code

    print(RPS(2))  # RPS.PAPER
    print(RPS.ROCK)  # RPS.ROCK
    print(RPS['ROCK'])  # RPS.ROCK
    print(RPS.ROCK.value)  # 1
    print(str(RPS.ROCK))  # RPS.ROCK
    print(str(RPS.ROCK).replace('RPS.', ''))  # ROCK
    print(str(RPS.ROCK).replace('RPS.', '').title())  # Rock
    return


if __name__ == '__main__':
    lesson5()
