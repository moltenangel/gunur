# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 8 - Loops
# Timestamp: 2:46:23

import sys
import random
from enum import Enum


def lesson8():
    # While Loops
    value = 1
    while value < 10:
        print(value)
        value += 1

    value = 1
    while value <= 10:
        print(value)
        value += 1

    value = 1
    while value <= 10:
        print(value)
        if value == 5:
            break
        value += 1

#    value = 1
#    while value <= 10:
#        print(value)
#        if value == 5:
#            continue  # You don't want to continue before the increment because it will create an infinite loop
#        value += 1

    value = 1
    while value <= 10:
        value += 1
        if value == 5:
            continue  # It skips the 5th iteration
        print(value)
    else:  # The else here will run once the while expression is no longer true
        print("Value is now equal to " + str(value))

    # For loops
    names = ["Dave", "Sara", "John"]
    for x in names:
        print(x)

    for x in "Mississippi":
        print(x)

    for x in names:  # This loop stops when it gets to Sara
        if x == "Sara":
            break
        print(x)

    for x in names:  # This loop skips Sara and continues
        if x == "Sara":
            continue
        print(x)

    for x in range(4):  # returns 0 - 3
        print(x)

    for x in range(2, 4):  # returns 2 - 3 (excludes last number)
        print(x)

    for x in range(5):  # returns 0 - 5
        print(x)

    for x in range(0,100,5):  # returns 0 - 100, increment by 5 (excludes last number)
        print(x)
    else:
        print("Glad that\'s over")

    names = ["Dave", "Sara", "John"]
    actions = ["codes","eats","sleeps"]

    # Nested loop
    for name in names:  # Outside Loop
        for action in actions:  # Inside Loop
            print(name + " " + action + ".")

    lesson8b()
    return


def lesson8b():  # Modify the code from lesson 5
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

    # sys.exit("Bye! 🙌")
    return


if __name__ == '__main__':
    lesson8()
