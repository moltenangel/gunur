# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 13 - f-Strings
# Time stamp: 4:38:02

import sys
import random
from enum import Enum


def lesson13():
    person = "Dave"
    coins = 3

    # Print method used in previous lessons
    print("\n" + person + " has " + str(coins) + " coins left.")

    # Other print methods that can be used (using %s for string)
    message = "\n%s has %s coins left." % (person, coins)
    print(message)

    # Format print method
    message = "\n{} has {} coins left.".format(person, coins)
    print(message)

    # Format print method using index values
    message = "\n{1} has {0} coins left.".format(coins, person)
    print(message)

    # Format print method using names
    message = "\n{person} has {coins} coins left.".format(coins=coins, person=person)
    print(message)

    player = { 'person': "Dave", 'coins': 3 }

    # Format print method using dictionary
    message = "\n{person} has {coins} coins left.".format(**player)
    print(message)

    #######################
    # f-strings! This is the way.

    # f-string print method
    message = f"\n{person} has {coins} coins left."
    print(message)

    # Use an equation inside {} instead of variable
    message = f"\n{person} has {2 * 5} coins left."
    print(message)

    # Use methods inside {} instead of variable
    message = f"\n{person.lower()} has {2 * 5} coins left."
    print(message)

    # Use dictionary[index] values inside {} instead of variable
    message = f"\n{player['person']} has {2 * 5} coins left."
    print(message)

    #######################
    # You can pass formatting options.
    # All formatting starts with a :

    num = 10
    print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")  # .2 indicates 2 decimals and the f indicates fixed

    for num in range(1,11):
        print(f"2.25 times {num} is {2.25 * num:.2f}")  # .2 indicates 2 decimals and the f indicates fixed

    for num in range(1,11):
        print(f"{num} divided by 4.52 is {num / 4.52:.2%}")  # .2 indicates 2 decimals and the % indicates percentage

    #######################
    # w3 Schools Python String format() method
    # https://w3schools.com/python/ref_string_format.asp

    # Time stamp: 4:37:38

    play = rps()
    play()
    return


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


if __name__ == '__main__':
    lesson13()
