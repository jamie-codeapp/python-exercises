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
symbols = ["!", "#", "$", "%", "&", "*", "(", ")", "-", "+"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

print("Welcome to the PyPassword Generator!")

number_letters = int(input("How many letters would you like in your password?\n"))
number_symbols = int(input("How many symbols would you like?\n"))
number_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for _ in range(number_letters):
    letter = letters[random.randint(0, len(letters) - 1)]
    password_list.append(letter)

for _ in range(number_symbols):
    symbol = symbols[random.randint(0, len(symbols) - 1)]
    password_list.append(symbol)

for _ in range(number_numbers):
    number = numbers[random.randint(0, len(numbers) - 1)]
    password_list.append(number)

random.shuffle(password_list)
password = "".join(password_list)
print(f"Your password is: {password}")
