import array as arr


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