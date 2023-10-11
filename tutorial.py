# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/

import math
import sys
import random
from enum import Enum


def lesson1():  # Getting Started
    greeting = 'Hello World!'
    print(greeting)
    return


def lesson2():  # The Basics
    line01 = "********************"  # header/footer
    line02 = "*                  *"  # re-use
    line03 = "*     WELCOME!     *"

    # starts with a blank line
    print('')
    print(line01)
    print(line02)
    print(line03)
    print(line02)
    print(line01)
    return


def lesson3():  # Operators
    # Symbols used to perform operations on values and the variables that hold those values.
    # = assignment
    # + add
    # - subtract
    # * multiply
    # / divide
    # // divide (round down)
    # round(expression) (round up)
    # ** to the power of (exponent)
    # % Modulus (remainder)
    # += add
    # -= subtract
    # /= (converts to float)
    # Comparison statements:
    # + concatenate "string " + "string" = "string string"
    # Is this equal (boolean) 42 == 41 = False
    # Is not equal (boolean) 42 != 42 = False
    # 10 > 5 = True
    # x = True
    # y = False
    # Conditional Statements:
    # not x = False
    # and x and y = False because one of them is False
    # or x or y = True  because one of them is True

    meaning = 42
    print('')
    # if meaning > 10:
    #     print('Right on!')
    # else:
    #     print('Not today')
    # return

    # Ternary Operator:
    print('Right on!') if meaning > 10 else print('Not today')
    return


def lesson4():  # Data Types
    # String data type

    # Literal assignment
    first = "Matthew"
    last = "Greene"
    print(type(first))
    print(type(first) == str)  # True
    print(isinstance(first, str))  # True

    # Constructor function:
    pizza = str("Pepperoni")
    print(type(pizza))
    print(type(pizza) == str)  # True
    print(isinstance(pizza, str))  # True

    # Concatenation:
    fullname = first + " " + last
    print(fullname)
    fullname += "!"
    print(fullname)

    # Casting a number to a string
    decade = str(1980)
    print(type(decade))

    statement = "I like rock music from the " + decade + "s."
    print(statement)

    # Multiple lines
    multiline = '''
    Hey, how are you?                          
    
    I was just checking in.    
                        All good? 
    
    '''
    print(multiline)

    # Escaping special characters
    sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
    print(sentence)

    # String Methods:

    print(first)
    print(first.lower())  # convert output to lowercase
    print(first.upper())  # convert output to uppercase
    print(first)

    print(multiline.title())  # Convert output to "proper case"
    print(multiline.replace("good","ok"))  # Replace any instance of "good" with "ok"
    print(multiline)

    print(len(multiline))
    multiline += "                                           "
    multiline = "                              " + multiline
    print(len(multiline))

    print(multiline.strip())
    print(len(multiline.strip()))
    print(len(multiline.lstrip()))
    print(len(multiline.rstrip()))

    print("")

    # Build a menu
    title = "menu".upper()
    print(title.center(20, "="))
    print("Coffee".ljust(16, ".") + "$1".rjust(4))
    print("Muffin".ljust(16, ".") + "$2".rjust(4))
    print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

    print("")

    # String Index Values
    print(first[1])  # a
    print(first[-1])  # w  (last letter)
    print(first[1:-1])  # atthe  (last letter **is not** included in the range)
    print(first[1:])  # atthew  (range from the nth to the last)

    # Some mthods return boolean data
    print(first.startswith("M"))  # True
    print(first.endswith("e"))  # False

    # Boolean data type
    myvalue = False  # (True or False must be written in Proper Case)
    x = bool(False)
    print(type(x))
    print(isinstance(myvalue, bool))  # True

    # Numeric data types

    # Integer type
    price = 100
    best_price = int(100)
    print(type(price))
    print(isinstance(best_price, int))  # True

    # Float type
    gpa = 3.28
    y = float(1.14)
    print(type(gpa))

    # Complex type
    comp_value = 5+3j
    print(type(comp_value))  # complex
    print(comp_value.real)  # 5.0
    print(comp_value.imag)  # 3.0

    # Built-in functions for numbers
    print(abs(gpa))  # Absolute Value = 3.8
    print(abs(gpa * -1))  # Absolute Value = 3.8
    print(round(gpa))  # Round to the nearest integer = 3
    print(round(gpa, 1))  # Round to the nearest n decimal = 3.3

    print(math.pi)
    print(math.sqrt(64))  # 8
    print(math.ceil(gpa))  # round up to the nearest integer
    print(math.floor(gpa))  # round down to the nearest integer

    # CAsting a string into a number
    zipcode = "29651"
    zip_value = int(zipcode)
    print(type(zip_value))

    # Error if you attempt to cast the incorrect data
    # zip_value = int("New York")  # Invalid literal error
    return


def lesson5():  # User Input
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


def lesson6():  # Lists & Tuples
    users = ['Dave', 'John', 'Sara']
    data = ['Dave', 42, True]
    emptylist = []
    print("Dave" in users)  # True
    print("Dave" in emptylist)  # False
    print(users[0])  # Dave
    print(users[-1])  # Sara
    print(users[-2])  # John

    print(users.index('Sara'))  # 2

    print(users[0:2])  # ['Dave', 'John']
    print(users[1:])  # ['John', 'Sara']
    print(users[-3:-1])  # ['Dave', 'John'] (same as [0:2]

    print(len(data))  # 3

    # Adding data to a list
    # users.append('Elsa')  # Adds Else to the end of the list
    print(users)  # ['Dave', 'John', 'Sara', 'Elsa']
    users += ['Jason']  # Adds Jason to the end of the list
    print(users)  # ['Dave', 'John', 'Sara', 'Elsa', 'Jason']
    # users += 'Jason'  # (incorrectly adds each letter to the list)
    # Extend adds items to the end of the list
    users.extend(['Robert', 'Jimmy'])  # Adds Robert and Jimmy to the end of the list
    print(users)  # ['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']
    users.extend(data)  # Adds the data list to the end of the list
    print(users)  # ['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy','Dave', 42, True]
    # Insert adds items to the start of the list
    users.insert(0,'Bob')  # Inserts Bob to the beginning of the list
    print(users)  # ['Bob', 'Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

    # Slicing (example: users[2:2])
    # users[2:2] = ['Eddie', 'Alex']  # Adds Eddie and Alex starting at the second index
    print(users)  # ['Bob', 'Dave', 'Eddie', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']
    users[1:3] = ['Robert', 'JPJ']  # Replaced the second and third indexes in the list
    print(users)  # ['Bob', 'Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

    # Removing data from a list
    users.remove('Bob')  # Remove Bob from the list
    print(users)  # ['Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

    print(users.pop())  # Removes the last index of the list
    print(users)  # ['Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']

    return


def lesson7():  # Dictionaries & Sets

    return


def lesson8():  # Loops

    return


def lesson():  #

    return


if __name__ == '__main__':
    # print('This script is not meant to be ran by itself. Please run main.py.')
    lesson6()
