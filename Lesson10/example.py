# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 10 - Recursion
# Timestamp: 3:23:48
# Recursion is when a function calls itself

value = "y"
count = 0

while value:
    count += 1
    print(count)
    if (count == 5):
        break
    else:
        value = 0
        continue