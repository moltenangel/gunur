# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 16 - Challenges
# Rock Paper Scissors (Challenges Iteration)
# Time stamp: 5:20:40

import sys
import random
from enum import Enum


def rps(name='PlayerOne'):  # PlayerOne is the default if no value is given.
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        # Rock Paper Scissors (Eighth iteration)
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1  # Constant variables use all caps
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f'\n{name}, please enter...\n1 for Rock,\n2 for Paper, or\n3 for Scissors:\n\n')
        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"{name}, you chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        # Windows Key + "." = Emoji selection window

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins!\nSorry, {name}..🥲"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count  # Work with and modify the global variable
        game_count += 1

        print(f"Game Count: {game_count}")
        print(f"{name}'s wins: {player_wins}")
        print(f"Python wins: {python_wins}")

        print(f"\nPlay again, {name}?")

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
            if __name__ == '__main__':
                sys.exit(f"Bye, {name}! 🙌")
            else:
                return

    return play_rps


if __name__ == '__main__':
    import argparse  # Command-line argument parsing library

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name",metavar="name", #  dest="firstname"
        required=False, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
