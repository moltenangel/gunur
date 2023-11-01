# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 11 - Scope
# Timestamp: 3:41:11


# It is important not to use global variables when not needed
# It is better to use Nonlocal variables inside nested functions
game_count = 0
count = 1


# Global Scope
name = "Dave"


def another():
    color = "blue"
    global count  # Takes the value from the global variable (must be done before modifying)
    count += 1
    print(count)

    def greeting(name):  # Functions have local scope
        nonlocal color  # Uses color from the parent function
        color = "red"
        print(color)  # Has access to the Global Scope (until overwritten by local scope)
        print(name)

    greeting("Dave")


another()
