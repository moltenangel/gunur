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
        print(" 0.) gunur logo")
        print(" 1.) Tutorial: Lesson 1")
        print(" 2.) Tutorial: Lesson 2")
        print(" 3.) Tutorial: Lesson 3")
        print(" 4.) Tutorial: Lesson 4")
        print(" 5.) Tutorial: Lesson 5")
        print(" 6.) Tutorial: Lesson 6")
        print(" 7.) Tutorial: Lesson 7")
        print(" 8.) Tutorial: Lesson 8")
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
            tut.lesson1()
        if choice == 2:
            tut.lesson2()
        if choice == 3:
            tut.lesson3()
        if choice == 4:
            tut.lesson4()
        if choice == 5:
            tut.lesson5()
        if choice == 6:
            tut.lesson6()
        if choice == 7:
            tut.lesson7()
        if choice == 8:
            tut.lesson8()
        elif choice == 98:
            fib.fib()
        elif choice == 99:
            print("Exiting")
            loop = 0
        else:
            print("Invalid input. Try again...")


main()
