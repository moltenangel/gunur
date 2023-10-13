# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 8 - Loops


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
    for name in names:
        for action in actions:
            print(name + " " + action + ".")
    return


if __name__ == '__main__':
    lesson8()
