# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 11 - Scope
# Timestamp: 3:41:11

import sys
import random
from enum import Enum

# It is important not to use global variables when not needed
game_count = 0
count = 1


def lesson11():
    # Global Scope
    name = "Dave"


    def another():
        color = "blue"
        global count  # Takes the value from the global variable (must be done before modifying)
        count += 1
        print(count)

        def greeting(name):  # Functions have local scope
            nonlocal color  # Uses color from the parent function
            color = "red"
            print(color)  # Has access to the Global Scope (until overwritten by local scope)
            print(name)

        greeting("Dave")

    another()
    play_rps()
    return


def play_rps():
    # Rock Paper Scissors (Forth iteration)
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

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "🎉 You win!"
        elif player == 2 and computer == 1:
            return "🎉 You win!"
        elif player == 3 and computer == 2:
            return "🎉 You win!"
        elif player == computer:
            return "😲 Tie game!"
        else:
            return "🐍 Python wins!"

    game_result = decide_winner(player, computer)

    print(game_result)

    global game_count  # Work with and modify the global variable
    game_count += 1

    print("\nGame Count: " + str(game_count))

    print("\nPlay again?")

    while True:
        question = input("\nY for Yes or \nQ to Quit\n")
        if question.lower() not in ["y","q"]:
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
    lesson11()
