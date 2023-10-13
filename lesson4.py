# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 4 - Data Types

import math


def lesson4():
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
    print(multiline.replace("good", "ok"))  # Replace any instance of "good" with "ok"
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
    comp_value = 5 + 3j
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

    # Casting a string into a number
    zipcode = "29651"
    zip_value = int(zipcode)
    print(type(zip_value))

    # Error if you attempt to cast the incorrect data
    # zip_value = int("New York")  # Invalid literal error
    return


if __name__ == '__main__':
    lesson4()
