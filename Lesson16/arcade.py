# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 16 - Challenges
# Arcade (menu which launches choice of game)
# Time stamp: 5:20:40

from guess_number import guess_number
from rps import rps
import sys


def play_game(name='PlayerOne'):  # PlayerOne is the default if no value is given.
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"{name}, welcome back to the Arcade! 🤖")

        playerchoice = input(
            '\nPlease choose a game:\n'
            '1 = Rock Paper Scissors\n'
            '2 = Guess My Number\n\n'
            'Or press "x" to exit the Arcade.\n')
        if playerchoice.lower() not in ["1", "2", "x"]:
            print(f"{name}, please enter 1, 2, or x.")
            return play_game(name)

        welcome_back = True

        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        if playerchoice == "2":
            guess_my_number = guess_number(name)
            guess_my_number()
        if playerchoice.lower() == "x":
            print("\nSee you next time!\n")
            sys.exit(f"Bye, {name}! 🙌")


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

    play_game(args.name)