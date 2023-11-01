import fib
from Lesson1 import hello as l1
from Lesson2 import welcome as l2
from Lesson3 import meaning as l3
from Lesson4 import data_types as l4
from Lesson5 import rps as l5
from Lesson6 import lists as l6
from Lesson7 import dictionaries as l7
from Lesson8 import loops as l8
from Lesson9 import functions as l9
from Lesson10 import recursion as l10
from Lesson11 import scope as l11
import lesson12 as l12
import lesson13 as l13
import lesson14 as l14
import lesson15 as l15
import lesson16 as l16


def gunur_logo():
    with open('gunur-ascii.txt') as f:
        print(''.join([line for line in f]))
    f.close()


if __name__ == '__main__':
    gunur_logo()


def main():
    print("Welcome to gunur.")
    loop = 1
    while loop == 1:
        print(" 0.) gunur logo")
        print(" 1.) Tutorial: Lesson 1")
        print(" 2.) Tutorial: Lesson 2")
        print(" 3.) Tutorial: Lesson 3")
        print(" 4.) Tutorial: Lesson 4")
        print(" 5.) Tutorial: Lesson 5")
        print(" 6.) Tutorial: Lesson 6")
        print(" 7.) Tutorial: Lesson 7")
        print(" 8.) Tutorial: Lesson 8")
        print(" 9.) Tutorial: Lesson 9")
        print(" 10.) Tutorial: Lesson 10")
        print(" 11.) Tutorial: Lesson 11")
        print(" 12.) Tutorial: Lesson 12")
        print(" 13.) Tutorial: Lesson 13")
        print(" 14.) Tutorial: Lesson 14")
        print(" 15.) Tutorial: Lesson 15")
        print(" 16.) Tutorial: Lesson 16")
        print("98.) Fibonacci Sequence")
        print("99.) Exit")

        while True:
            try:  # Ensure an integer is returned
                choice = int(input("Option: "))
                break
            except ValueError:
                print("Invalid input. Try again...")

        if choice == 0:
            gunur_logo()
        if choice == 1:
            l1.lesson1()
        if choice == 2:
            l2.lesson2()
        if choice == 3:
            l3.lesson3()
        if choice == 4:
            l4.lesson4()
        if choice == 5:
            l5.lesson5()
        if choice == 6:
            l6.lesson6()
        if choice == 7:
            l7.lesson7()
        if choice == 8:
            l8.lesson8()
        if choice == 9:
            l9.lesson9()
        if choice == 10:
            l10.lesson10()
        if choice == 11:
            l11.lesson11()
        if choice == 12:
            l12.lesson12()
        if choice == 13:
            l13.lesson13()
        if choice == 14:
            l14.lesson14()
        if choice == 15:
            l15.lesson15()
        if choice == 16:
            l16.lesson16()
        elif choice == 98:
            fib.fib()
        elif choice == 99:
            print("Exiting")
            loop = 0
        else:
            print("Invalid input. Try again...")


main()
