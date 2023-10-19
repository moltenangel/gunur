# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 13 - f-Strings
# Time stamp: 4:19:33

def lesson13():
    person = "Dave"
    coins = 3

    # Print method used in previous lessons
    print("\n" + person + " has " + str(coins) + " coins left.")

    # Other print methods that can be used (using %s for string)
    message = "\n%s has %s coins left." % (person, coins)
    print(message)

    # Format print method
    message = "\n{} has {} coins left.".format(person, coins)
    print(message)

    # Format print method using index values
    message = "\n{1} has {0} coins left.".format(coins, person)
    print(message)

    # Format print method using names
    message = "\n{person} has {coins} coins left.".format(coins=coins, person=person)
    print(message)

    player = { 'person': "Dave", 'coins': 3 }

    # Format print method using dictionary
    message = "\n{person} has {coins} coins left.".format(**player)
    print(message)

    #######################
    # f-strings! This is the way.

    # f-string print method
    message = f"\n{person} has {coins} coins left."
    print(message)

    # Use an equation inside {} instead of variable
    message = f"\n{person} has {2 * 5} coins left."
    print(message)

    # Use methods inside {} instead of variable
    message = f"\n{person.lower()} has {2 * 5} coins left."
    print(message)

    # Use dictionary[index] values inside {} instead of variable
    message = f"\n{player['person']} has {2 * 5} coins left."
    print(message)

    #######################
    # You can pass formatting options.
    # All formatting starts with a :

    num = 10
    print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")  # .2 indicates 2 decimals and the f indicates fixed

    for num in range(1,11):
        print(f"2.25 times {num} is {2.25 * num:.2f}")  # .2 indicates 2 decimals and the f indicates fixed

    for num in range(1,11):
        print(f"{num} divided by 4.52 is {num / 4.52:.2%}")  # .2 indicates 2 decimals and the % indicates percentage

    #######################
    # w3 Schools Python String format() method
    # https://w3schools.com/python/ref_string_format.asp

    # Time stamp: 4:37:38
    return


if __name__ == '__main__':
    lesson13()
