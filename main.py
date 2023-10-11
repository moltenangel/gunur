import fib
import tutorial as tut


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
        while True:
            try:  # Ensure an integer is returned
                choice = int(show_menu())
                break
            except ValueError:
                print("Invalid input. Try again...")

        if choice == 0:
            gunur_logo()
        if choice == 1:
            tut.lesson1()
        if choice == 2:
            tut.lesson2()
        if choice == 3:
            tut.lesson3()
        if choice == 4:
            tut.lesson4()
        if choice == 5:
            tut.lesson4()
        elif choice == 8:
            fib.fib()
        elif choice == 9:
            print("Exiting")
            loop = 0
        else:
            print("Invalid input. Try again...")


def show_menu():
    print("0.) gunur logo")
    print("1.) Tutorial: Lesson 1")
    print("2.) Tutorial: Lesson 2")
    print("3.) Tutorial: Lesson 3")
    print("4.) Tutorial: Lesson 4")
    print("5.) Tutorial: Lesson 5")
    print("8.) Fibonacci Sequence")
    print("9.) Exit")
    var = input("Option: ")
    return var


main()
