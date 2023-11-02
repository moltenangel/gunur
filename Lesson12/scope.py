# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 12 - Closures
# Timestamp: 4:00:30
# Closures is a function having access to the scope of its parent function after the parent function has returned
# The closure is created when the parent function returns.


def parent_function(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins  # References coins from the parent function
        coins -= 1  # reduce coins by one

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game

tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 5)

tommy()
tommy()

jenny()

tommy()
