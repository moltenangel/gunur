# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/

import math


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

    return


def lesson5():  #

    return


def lesson():  #

    return


if __name__ == '__main__':
    # print('This script is not meant to be ran by itself. Please run main.py.')
    lesson4()
