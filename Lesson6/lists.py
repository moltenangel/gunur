# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 6 - Lists & Tuples
# Timestamp: 1:45:31

# Lists #
# The data and order of the list can be changed (mutable)

users = ['Dave', 'John', 'Sara']
data = ['Dave', 42, True]
emptylist = []
print("Dave" in users)  # True
print("Dave" in emptylist)  # False
print(users[0])  # Dave
print(users[-1])  # Sara
print(users[-2])  # John

print(users.index('Sara'))  # 2

print(users[0:2])  # ['Dave', 'John']
print(users[1:])  # ['John', 'Sara']
print(users[-3:-1])  # ['Dave', 'John'] (same as [0:2]

print(len(data))  # 3

# Adding data to a list
users.append('Elsa')  # Adds Else to the end of the list
print(users)  # ['Dave', 'John', 'Sara', 'Elsa']
users += ['Jason']  # Adds Jason to the end of the list
print(users)  # ['Dave', 'John', 'Sara', 'Elsa', 'Jason']
# users += 'Jason'  # (incorrectly adds each letter to the list)

# Extend adds items to the end of the list
users.extend(['Robert', 'Jimmy'])  # Adds Robert and Jimmy to the end of the list
print(users)  # ['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']
# users.extend(data)  # Adds the data list to the end of the list
# print(users)  # ['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy','Dave', 42, True]

# Insert adds items to the start of the list
users.insert(0,'Bob')  # Inserts Bob to the beginning of the list
print(users)  # ['Bob', 'Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

# Slicing (example: users[2:2])
# users[2:2] = ['Eddie', 'Alex']  # Adds Eddie and Alex starting at the second index
print(users)  # ['Bob', 'Dave', 'Eddie', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']
users[1:3] = ['Robert', 'JPJ']  # Replaced the second and third indexes in the list
print(users)  # ['Bob', 'Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

# Removing data from a list
users.remove('Bob')  # Remove 'Bob' from the list
print(users)  # ['Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

print(users.pop())  # Removes the last index of the list
print(users)  # ['Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']

del users[0]  # Deletes 'Robert'
print(users)  # ['JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']

# del data  # Completely deletes the list from memory and will throw an error if accessed
data.clear()  # removes all entries from the list, but will not throw an error
print(data)  # []

# Sorting lists: (This operation is case sensitive)
# users.sort()  # Throws an error because there is an integer in the list full of strings
print(users)  # ['JPJ', 'Sara', 'Elsa', 'Jason', 'Robert']

# users[1:2] = 'dave'  # Erroneously inserts 'd','a','v','e' in the second index position (Use brackets)
users[1:2] = ['dave']  # Replaces 'Sara' with 'dave' in the second index position (lowercase)
print(users)  # ['JPJ', 'dave', 'Elsa', 'Jason', 'Robert']
users.sort()  # Sorts list (Capital letters come before lowercase)!!!
print(users)  # ['Elsa', 'JPJ', 'Jason', 'Robert', 'dave']

users.sort(key=str.lower)  # Sorts list (regardless of case)
print(users)  # ['dave', 'Elsa', 'Jason', 'JPJ', 'Robert']

nums = [4,42,78,1,5]
nums.reverse()  # Reverse the order of the list items
print(nums)  # [5, 1, 78, 42, 4]

nums.sort(reverse=True)  # Sort the list in reverse order)
print(nums)  # [78, 42, 5, 4, 1]

print(sorted(nums, reverse=True))  # This returns the sorted list without modifying the original list order

# Timeline = (2:07:18)
# Other ways to copy a list
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)  # [78, 42, 5, 4, 1]
print(mynums)  # [78, 42, 5, 4, 1]
mycopy.sort()  # sorts list
print(mycopy)  # [1, 4, 5, 42, 78]
print(nums)  # [78, 42, 5, 4, 1]

print(type(nums))  # <class 'list'>

mylist = list([1, "Neil", True])  # create new list using constructor
print(mylist)  # [1, 'Neil', True]

# Tuples
# Tuples are like lists except the data will not change (immutable)

mytuple = tuple(('Dave',42,True))  # create a tuple with a constructor
anothertuple = (1,4,2,8)

print(mytuple)  # ('Dave', 42, True) Has parenthesis instead of brackets
print(type(mytuple))  # <class 'tuple'>
print(type(anothertuple))  # <class 'tuple'>

newlist = list(mytuple)  # create a new list out of tuple
newlist.append('Neil')  # add a value to the list
newtuple = tuple(newlist)  # create a new tuple from new list
print(newtuple)  # ('Dave', 42, True, 'Neil')

(one, two, *hey) = anothertuple
print(one)  # 1 (unpacks the first value in anothertuple)
print(two)  # 4 (unpacks the second value in anothertuple)
print(hey)  # [2, 8] (unpacks the remaining values in anothertuple because of the asterisk)

(one, *two, hey) = anothertuple
print(one)  # 1 (unpacks the first value in anothertuple)
print(two)  # [4, 2] (unpacks the remaining values in anothertuple MINUS the last one (hey))
print(hey)  # 8 (unpacks the last value in anothertuple)

print(anothertuple.count(2))  # counts how many occurances of 2 in the tuple
