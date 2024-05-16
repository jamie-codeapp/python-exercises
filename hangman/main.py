import random
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6

word = random.choice(word_list)
print(f"Psst, the solution is {word}")

display = []
for _ in range(len(word)):
    display += "_"


end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for index, letter in enumerate(word):
        if guess == letter:
            display[index] = letter

    if "_" not in display:
        end_of_game = True
        print("You win.")

    if guess not in word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    if lives == 0:
        end_of_game = True
        print("You lose.")

    print(" ".join(display))
    print(stages[lives])
