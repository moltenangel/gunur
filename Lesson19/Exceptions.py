# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 19 - Exceptions & Errors
# Time stamp: 6:15:44
# Python Built-In Exceptions: https://www.w3schools.com/python/python_ref_exceptions.asp

class JustNotCoolError(Exception):
    pass


x = 2

try:
    raise JustNotCoolError("This just isn't cool, man.")
    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print('NameError means something is probably undefined')
except ZeroDivisionError:
    print('Please do not divide by zero.')
except Exception as error:
    print(error)
else:
    print('No errors!')
finally:
    print("I'm going to print with or without an error.")
