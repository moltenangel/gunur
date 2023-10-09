# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('World')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def main():
    print("Welcome to gunur.")
    loop = 1
    choice = 0
    while loop == 1:
        while True:
            try:  # Ensure an integer is returned
                choice = int(show_menu())
                break
            except ValueError:
                print("Invalid input. Try again...")

        if choice == 1:
            print(choice)
        elif choice == 2:
            print(choice)
        elif choice == 9:
            print("Exiting")
            loop = 0
        else:
            print("Invalid input. Try again...")


def show_menu():
    print("1.) Item 1")
    print("2.) Item 2")
    print("9.) Exit")
    var = input("Option: ")
    return var


main()
