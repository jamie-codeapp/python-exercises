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
    "q",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    try:
        shift_amount = int(shift_amount)

        for letter in start_text:
            if letter in alphabet:
                new_index = (
                    alphabet.index(letter) + shift_amount
                    if cipher_direction == "encode"
                    else alphabet.index(letter) - shift_amount
                )
                new_index %= len(alphabet)
                end_text += alphabet[new_index]
            else:
                end_text += letter

        print(f"Here's the {cipher_direction}d result: {end_text}")

    except ValueError:
        print("You should enter a shift number.")


continue_cipher = True

while continue_cipher:
    print(logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = input("Type the shift number:\n")

    caesar(text, shift, direction)

    if input("Type 'yes' if you want to go again. Otherwise type 'no'.\n") == "no":
        continue_cipher = False
        print("Goodbye")
