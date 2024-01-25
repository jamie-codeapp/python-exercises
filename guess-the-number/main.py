from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def conver_to_int(input):
    try:
        return int(input)
    except ValueError:
        pass


def check_answer(guess, answer):
    global in_the_game, turns

    if turns > 1:
        if guess > answer:
            turns -= 1
            return "Too high."
        elif answer > guess:
            turns -= 1
            return "Too low."
        else:
            in_the_game = False
            return f"You got it! The answer was {answer}."
    else:
        in_the_game = False
        return "You've run out of guesses, you lose."


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

answer = random.randint(1, 100)
# print(f"Pssst, the correct answer is {answer}.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
turns = HARD_LEVEL_TURNS if level == "hard" else EASY_LEVEL_TURNS
in_the_game = True

while in_the_game:
    print(f"You have {turns} attempts to remaining to guess the number.")

    guess = conver_to_int(input("Make a guess: "))

    if guess != None:
        result = check_answer(guess, answer)
        print(result)
    else:
        turns -= 1
        print("You should enter a number.")
