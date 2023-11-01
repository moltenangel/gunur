# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 10 - Recursion
# Timestamp: 3:23:48
# Recursion is when a function calls itself


def add_one(num):

    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)


mynewtotal = add_one(0)
print(mynewtotal)


def example():
    value = True  # Could also be 'y'

    # while value == True:
    while value:  # Means the same as 'while value == True' (or 'while value exists')
        print(value)
        value = False  # Could also be value = 0

    value = "y"
    count = 0
    while value:  # Means the same as 'while value == True' (or 'while value exists')
        count += 1
        print(count)
        if (count == 5):
            break
        else:
            value = 0
            continue  # The while loop will be evaluated again
    return


example()
