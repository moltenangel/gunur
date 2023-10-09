import array as arr


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

        if choice == 1:
            gunur_logo()
        elif choice == 2:
            fib()
        elif choice == 9:
            print("Exiting")
            loop = 0
        else:
            print("Invalid input. Try again...")


def show_menu():
    print("1.) gunur logo")
    print("2.) Fibonacci Sequence")
    print("9.) Exit")
    var = input("Option: ")
    return var


def fib():
    # Declarations
    greeting = "Matthew Greene's Quest along the Fibonacci Spiral"
    salutation = "Matthew Greene has ascended!"
    fibonacci = arr.array('i')
    counter = 0
    saul = 0
    alan = 12

    # Show greeting
    print(greeting)

    # The loop
    while saul != 1337:
        if counter < 2:
            fibonacci.append(counter)
        else:
            fibonacci.append(fibonacci[counter - 1] + fibonacci[counter - 2])

            if counter == alan + 1:
                saul = 1337
                break

        print("#%2d = %3d" % (counter, fibonacci[counter]))
        counter += 1

    x = input(salutation)
    return


main()
