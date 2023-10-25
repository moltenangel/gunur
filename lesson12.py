# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 12 - Closures
# Timestamp: 4:00:30
# Closures is a function having access to the scope of its parent function after the parent function has returned
# The closure is created when the parent function returns.

import sys
import random
from enum import Enum


def lesson12():
    def parent_function(person, coins):
        # coins = 3

        def play_game():
            nonlocal coins  # References coins from the parent function
            coins -= 1  # reduce coins by one

            if coins > 1:
                print("\n" + person + " has " + str(coins) + " coins left.")
            elif coins == 1:
                print("\n" + person + " has " + str(coins) + " coin left.")
            else:
                print("\n" + person + " is out of coins.")

        return play_game

    tommy = parent_function("Tommy", 3)
    jenny = parent_function("Jenny", 5)

    tommy()
    tommy()

    jenny()

    tommy()

    play = rps()

    play()


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        # Rock Paper Scissors (Fifth iteration)

        nonlocal player_wins
        nonlocal python_wins

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
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉 You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🎉 You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎉 You win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return "🐍 Python wins!"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count  # Work with and modify the global variable
        game_count += 1

        print("Game Count: " + str(game_count))
        print("Player wins: " + str(player_wins))
        print("Python wins: " + str(python_wins))

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

    return play_rps


if __name__ == '__main__':
    lesson12()
