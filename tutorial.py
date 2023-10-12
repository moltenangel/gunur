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
    ### Lists ###
    # The data and order of the list can be changed (mutable)

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
    users.append('Elsa')  # Adds Else to the end of the list
    print(users)  # ['Dave', 'John', 'Sara', 'Elsa']
    users += ['Jason']  # Adds Jason to the end of the list
    print(users)  # ['Dave', 'John', 'Sara', 'Elsa', 'Jason']
    # users += 'Jason'  # (incorrectly adds each letter to the list)

    # Extend adds items to the end of the list
    users.extend(['Robert', 'Jimmy'])  # Adds Robert and Jimmy to the end of the list
    print(users)  # ['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']
    # users.extend(data)  # Adds the data list to the end of the list
    # print(users)  # ['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy','Dave', 42, True]

    # Insert adds items to the start of the list
    users.insert(0,'Bob')  # Inserts Bob to the beginning of the list
    print(users)  # ['Bob', 'Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

    # Slicing (example: users[2:2])
    # users[2:2] = ['Eddie', 'Alex']  # Adds Eddie and Alex starting at the second index
    print(users)  # ['Bob', 'Dave', 'Eddie', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']
    users[1:3] = ['Robert', 'JPJ']  # Replaced the second and third indexes in the list
    print(users)  # ['Bob', 'Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

    # Removing data from a list
    users.remove('Bob')  # Remove 'Bob' from the list
    print(users)  # ['Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

    print(users.pop())  # Removes the last index of the list
    print(users)  # ['Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']

    del users[0]  # Deletes 'Robert'
    print(users)  # ['JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']

    # del data  # Completely deletes the list from memory and will throw an error if accessed
    data.clear()  # removes all entries from the list, but will not throw an error
    print(data)  # []

    # Sorting lists: (This operation is case sensitive)
    # users.sort()  # Throws an error because there is an integer in the list full of strings
    print(users)  # ['JPJ', 'Sara', 'Elsa', 'Jason', 'Robert']

    # users[1:2] = 'dave'  # Erroneously inserts 'd','a','v','e' in the second index position (Use brackets)
    users[1:2] = ['dave']  # Replaces 'Sara' with 'dave' in the second index position (lowercase)
    print(users)  # ['JPJ', 'dave', 'Elsa', 'Jason', 'Robert']
    users.sort()  # Sorts list (Capital letters come before lowercase)!!!
    print(users)  # ['Elsa', 'JPJ', 'Jason', 'Robert', 'dave']

    users.sort(key=str.lower)  # Sorts list (regardless of case)
    print(users)  # ['dave', 'Elsa', 'Jason', 'JPJ', 'Robert']

    nums = [4,42,78,1,5]
    nums.reverse()  # Reverse the order of the list items
    print(nums)  # [5, 1, 78, 42, 4]

    nums.sort(reverse=True)  # Sort the list in reverse order)
    print(nums)  # [78, 42, 5, 4, 1]

    print(sorted(nums, reverse=True))  # This returns the sorted list without modifying the original list order

    # Timeline = (2:07:18)
    # Other ways to copy a list
    numscopy = nums.copy()
    mynums = list(nums)
    mycopy = nums[:]

    print(numscopy)  # [78, 42, 5, 4, 1]
    print(mynums)  # [78, 42, 5, 4, 1]
    mycopy.sort()  # sorts list
    print(mycopy)  # [1, 4, 5, 42, 78]
    print(nums)  # [78, 42, 5, 4, 1]

    print(type(nums))  # <class 'list'>

    mylist = list([1, "Neil", True])  # create new list using constructor
    print(mylist)  # [1, 'Neil', True]

    ### Tuples ###
    # Tuples are like lists except the data will not change (immutable)

    mytuple = tuple(('Dave',42,True))  # create a tuple with a constructor
    anothertuple = (1,4,2,8)

    print(mytuple)  # ('Dave', 42, True) Has parenthesis instead of brackets
    print(type(mytuple))  # <class 'tuple'>
    print(type(anothertuple))  # <class 'tuple'>

    newlist = list(mytuple)  # create a new list out of tuple
    newlist.append('Neil')  # add a value to the list
    newtuple = tuple(newlist)  # create a new tuple from new list
    print(newtuple)  # ('Dave', 42, True, 'Neil')

    (one, two, *hey) = anothertuple
    print(one)  # 1 (unpacks the first value in anothertuple)
    print(two)  # 4 (unpacks the second value in anothertuple)
    print(hey)  # [2, 8] (unpacks the remaining values in anothertuple because of the asterisk)

    (one, *two, hey) = anothertuple
    print(one)  # 1 (unpacks the first value in anothertuple)
    print(two)  # [4, 2] (unpacks the remaining values in anothertuple MINUS the last one (hey))
    print(hey)  # 8 (unpacks the last value in anothertuple)

    print(anothertuple.count(2))  # counts how many occurances of 2 in the tuple

    return


def lesson7():  # Dictionaries & Sets
    ### Dictionaries ###
    # Used to store data values that are in key/value pairs

    band = {  # dictionaries use curly braces
        "vocals": "Plant",
        "guitar": "Page"
    }

    band2 = dict(vocals="Plant", guitar="Page")  # Using the dictionary constructor

    print(band)  # {'vocals': 'Plant', 'guitar': 'Page'}
    print(band2)  # {'vocals': 'Plant', 'guitar': 'Page'}
    print(type(band))  # <class 'dict'>
    print(len(band))  # 2 (key pairs)

    # Access items
    print(band["vocals"])  # Plant
    print(band.get("guitar"))  # Page

    # List all keys
    print(band.keys())  # dict_keys(['vocals', 'guitar'])

    # List all values
    print(band.values())  # dict_values(['Plant', 'Page'])

    # List of key/value pairs as tuples
    print(band.items())  # dict_items([('vocals', 'Plant'), ('guitar', 'Page')])

    # Verify a key exists
    print("guitar" in band)  # True
    print("triangle" in band)  # False

    # Change values
    band["vocals"] = "Coverdale"  # changed vocals to Coverdale
    band.update({"bass": "JPJ"})  # Added a new key/value pair

    print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'bass': 'JPJ'}

    # Removing items
    print(band.pop("bass"))  # returns JPJ (removes last key/value pair)
    print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}

    band["drums"] = "Bonham"  # Add key/value pair
    print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Bonham'}

    # removes last key/value pair added to the dictionary
    print(band.popitem())  # returns tuple ('drums', 'Bonham')

    # Delete and clear items
    band["drums"] = "Bonham"  # Add key/value pair
    del band["drums"]  # removes tuple ('drums', 'Bonham')
    print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}

    band2.clear()  # clears all key/value pairs in dictionary
    print(band2)  # {}

    del band2  # completely deletes dictionary

    # Copy dictionaries
    # How not to copy dictionaries
    band2 = band  # creates reference (which means they share memory. Modifying one modifies both.)
    print("Bad copy!")
    print(band2)  # {'vocals': 'Coverdale', 'guitar': 'Page'}
    print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}

    band2["drums"] = "Dave"  # Adds key/value pair to both
    print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'}

    # How to copy dictionaries
    band2 = band.copy()  # The proper way to make a dictionary copy
    band2["drums"] = "Dave"  # Adds key/value pair to both
    print("Good copy!")
    print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'}
    print(band2)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'}

    # Or use the dictionary constructor function
    band3 = dict(band)  # Create copy using dict constructor function
    print("Good copy!")
    print(band3)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'}

    # Nested dictionaries
    # This means a key/value pair in a dictionary can be another dictionary

    member1 = {
        "name": "Plant",
        "instrument": "vocals"
    }
    member2 = {
        "name": "Page",
        "instrument": "guitar"
    }
    band = {
        "member1": member1,  # member1 dictionary as value
        "member2": member2  # member2 dictionary as value
    }
    print(band)  # {'member1': {'name': 'Plant', 'instrument': 'vocals'}, 'member2': {'name': 'Page', 'instrument': 'guitar'}}
    print(band["member1"]["name"])  # Plant (member1 is the first level deep. name is the second level deep.)

    ### Sets ###

    nums = { 1, 2, 3, 4 }  # create set

    nums = set(( 1, 2, 3, 4 ))  # create set using set constructor function

    nums2 = set ((1,2,3,4))  # create set using set constructor function

    print(nums)  # {1, 2, 3, 4}
    print(nums2)  # {1, 2, 3, 4}
    print(type(nums))  # <class 'set'>
    print(len(nums))  # 4

    # No duplicates allowed
    nums = { 1, 2, 2, 3}  # Tried to create set with a duplicate
    print(nums)  # {1, 2, 3}

    # True is a dupe of 1 and False is a Dupe of zero
    nums = {1, True, 2, False, 3, 4, 0 }
    print(nums)  # {False, 1, 2, 3, 4} (notice it is sorted)

    # Check if a value is in a set
    print(2 in nums)  # True

    # but you cannot refer to an element in the set with an index position or a key
    # Time stamp 2:40:54

    # Add a new element to a set
    nums.add(8)
    print(nums)  # {False, 1, 2, 3, 4, 8}

    # Add elements from one set to another
    morenums = {5, 6, 7}
    nums.update(morenums)  # Adding elements from morenums to nums
    print(nums)  # {False, 1, 2, 3, 4, 5, 6, 7, 8}

    # You can use update with lists, tuples, and dictionaries, too.
    # 2:42:54
    return


def lesson8():  # Loops

    return


def lesson():  #

    return


if __name__ == '__main__':
    # print('This script is not meant to be ran by itself. Please run main.py.')
    lesson7()
