# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 14 - Modules
# Time stamp: 4:42:15

import math  # print(math.pi)
from math import pi  # print(pi)
import random as rdm
import kansas
from rps7 import rock_paper_scissors

def lesson14():
    print(math.pi)
    print(pi)
    rdm.choice("123")

    # for item in dir(rdm):  # List all the methods and variables of the random module
    #     print(item)

# 4:48:22
    print(kansas.capital)
    kansas.randomfunfact()
    print(__name__)
    print(kansas.__name__)

    rock_paper_scissors()
    return


if __name__ == '__main__':
    lesson14()
