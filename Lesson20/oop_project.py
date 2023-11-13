# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 20 - OOP Project
# Time stamp: 6:27:30


from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(10000, Sara)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Dave)

