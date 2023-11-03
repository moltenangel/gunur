# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 17 - Lambda & Higher Order Functions
# Time stamp: 5:35:59
# Lambda Function - Single expression that returns a value
# Lambda functions are sometimes referred to as anonymous functions


squared = lambda num : num * num  # (This is the way he wrote it. VSCode converted it to the way it is written below)
# def squared(num): return num * num


print(squared(2))

addTwo = lambda num : num + 2

print(addTwo(12))

sum = lambda a, b : a + b

print(sum(10,8))

########################
# When would I use a lamba?
# Lambdas are usually used inside another function


def funcBuilder(x):
    return lambda num : num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

########################
# What is a higher order function?
# A function that takes one or more functions as arguments or a function that returns a function as its result


numbers = [3,7,12,18,20,21]

# This function will return the squared value of each item in the list (all in one line of code)
squared_nums = map(lambda num : num * num, numbers)
# map() is a built-in function that receives a function as the first argument

print(list(squared_nums))

########################
# Filters filter results
# This function will filter the results of list... (all in one line of code)
odd_nums = filter(lambda num : num % 2 != 0, numbers)
# filter() is a built-in function
# != is a comparison which will return True or False

print(list(odd_nums))

# 5:49:46
