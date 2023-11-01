# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 9 - Functions
# Timestamp: 3:09:04


def hello_world():
    print("Hello World!")
    return


hello_world()


def sum(num1=0, num2=0):  # Default value = 0
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2


sum(2,3)
sum(1, 7)
sum(100, 3)
total = sum(2, 3)
total = sum("a", 3)  # returns "None"
# total = sum()  # creates error
total = sum(1)
total = sum(2, 3)
total = sum(7, 2)

print(total)


def multiple_items(*args):
    print(args)
    print(type(args))  # Returns a tuple


multiple_items("Dave", "John", "Sara")


# function names need to be all lowercase, but words can be separated by underscores
def mult_named_items(**kwargs):  # Keyword Arguments
    print(kwargs)
    print(type(kwargs))  # returns a dictionary type


mult_named_items(first = "Dave", last = "Gray")










