# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 16 - Challenges
# Guess Number Game
# Time stamp: 5:20:40

import sys
import random


def guess_number(name='PlayerOne'):  # PlayerOne is the default if no value is given.
    game_count = 0
    player_wins = 0

    def play_guess_number():
        # Guess Number Game
        nonlocal name
        nonlocal player_wins

        playerchoice = input(
            f"\n{name}, guess which number I'm thinking of...\n1, 2, or 3.\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_guess_number()

        computerchoice = random.choice("123")
        computerchoice = random.

        print(f"{name}, you chose {playerchoice}.")
        print(f"I was thinking about the number {computerchoice}.\n")

        player = int(playerchoice)

        computer = int(computerchoice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            if player == computer:
                player_wins += 1
                return f"🎉 {name}, you win!"
            else:
                return f"Sorry, {name}. Better luck next time. 🥲"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count  # Work with and modify the "global"/nonlocal variable
        game_count += 1

        print(f"Game Count: {game_count}")
        print(f"{name}'s wins: {player_wins}")
        print(f"Your winning percentage: {player_wins / game_count:.2%}")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue  # Starts the loop again asking for "y" or "n"
            else:
                break  # the loop stops
        if playagain.lower() == "y":
            return play_guess_number()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            if __name__ == '__main__':
                sys.exit(f"Bye, {name}! 🙌")
            else:
                return

    return play_guess_number


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

    guess_number_game = guess_number(args.name)
    guess_number_game()
