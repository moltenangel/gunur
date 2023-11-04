# gunur - Discovering Purpose
# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/

import fib


def gunur_logo():
    with open('gunur-ascii.txt') as f:
        print(''.join([line for line in f]))
    f.close()


def main():
    print("Welcome to gunur.")
    loop = 1
    while loop == 1:
        print(" 1.) gunur logo")
        print("2.) Fibonacci Sequence")
        print("3.) Exit")

        while True:
            try:  # Ensure an integer is returned
                choice = int(input("Option: "))
                break
            except ValueError:
                print("Invalid input. Try again...")

        if choice == 1:
            gunur_logo()
        elif choice == 2:
            fib.fib()
        elif choice == 3:
            print("Exiting")
            loop = 0
        else:
            print("Invalid input. Try again...")


main()

if __name__ == '__main__':
    gunur_logo()