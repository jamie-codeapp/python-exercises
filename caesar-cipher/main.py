from art import logo

alphabet = [
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
]

should_continue = True


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in start_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index + shift_amount) % len(alphabet)
            end_text += alphabet[new_index]
        else:
            end_text += letter

    print(f"Here's the {cipher_direction}d result: {end_text}")


while should_continue:
    print(logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    if (
        input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        == "no"
    ):
        should_continue = False
        print("Goodbye")
