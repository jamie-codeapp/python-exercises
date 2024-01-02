import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
symbols = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def conver_to_int(input):
    try:
        return int(input)
    except ValueError:
        pass


print("Welcome to the PyPassword Generator!")

letters_input = input("How many letters would you like in your password?\n")
symbols_input = input("How many symbols would you like?\n")
numbers_input = input("How many symbols would you like?\n")

letters_as_int = conver_to_int(letters_input)
symbols_as_int = conver_to_int(symbols_input)
numbers_as_int = conver_to_int(numbers_input)

password_list = []

if letters_as_int != None and symbols_as_int != None and numbers_as_int != None:
    for _ in range(letters_as_int):
        password_list.append(random.choice(letters))
    for _ in range(symbols_as_int):
        password_list.append(random.choice(symbols))
    for _ in range(numbers_as_int):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)
    password = "".join(password_list)
    print(f"Your password is: {password}")
else:
    print("You typed an invalid value.")
