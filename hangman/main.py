import random

from hangman_art import stages, logo
from hangman_words import word_list

display = []
lives = 6
is_playing_game = True

chosen_word = random.choice(word_list)
# print(f"Pssst, the solution is {chosen_word}.")

for _ in range(len(chosen_word)):
    display += "_"

print(logo)
print(display)

while is_playing_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    else:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            is_playing_game = False
            print("You lose.")

    print(display)

    if "_" not in display:
        print("You win!")
        is_playing_game = False

    print(stages[lives])
