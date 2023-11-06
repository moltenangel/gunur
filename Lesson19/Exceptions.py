# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 19 - Exceptions & Errors
# Time stamp: 6:15:44
# Python Built-In Exceptions: https://www.w3schools.com/python/python_ref_exceptions.asp

x = 2

try:
    print(x / 0)
except NameError:
    print('NameError means something is probably undefined')
except ZeroDivisionError:
    print('Please do not divide by zero.')
# 6:21:14