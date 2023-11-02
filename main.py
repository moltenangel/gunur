import fib
from Lesson13 import f_strings as l13
from Lesson14 import modules as l14
import lesson15 as l15
import lesson16 as l16


def gunur_logo():
    with open('gunur-ascii.txt') as f:
        print(''.join([line for line in f]))
    f.close()


def main():
    print("Welcome to gunur.")
    loop = 1
    while loop == 1:
        print(" 0.) gunur logo")
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

if __name__ == '__main__':
    gunur_logo()