# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 15 - Command Line Arguments
# Timestamp: 4:59:47

def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)


if __name__ == '__main__':
    # Reference: https://docs.python.org/py-modindex.html
    import argparse  # Command-line argument parsing library

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument(
        "-n", "--name",metavar="name", #  dest="firstname"
        required=True, help="The name of the person to greet."
    )

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English","Spanish","German"],
        help="The language of the greeting."
    )

    args = parser.parse_args()

    hello(args.name, args.lang)
