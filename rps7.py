# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 14 - Modules
# Rock Paper Scissors (Seventh Iteration)
# Time stamp: 4:57:13

import sys
import random
from enum import Enum


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
        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"You chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

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

        print(f"Game Count: {str(game_count)}")
        print(f"Player wins: {str(player_wins)}")
        print(f"Python wins: {str(python_wins)}")

        print("\nPlay again?")

        while True:
            question = input("\nY for Yes or \nQ to Quit\n")
            if question.lower() not in ["y", "q"]:
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

rock_paper_scissors = rps()

rock_paper_scissors()


if __name__ == '__main__':
    rock_paper_scissors()
