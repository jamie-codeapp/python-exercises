import os, random
from art import logo, vs
from game_data import data


def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def pick_a_random_account(account_data):
    return random.choice(account_data)

def show_account_info(account):
    return f"{account["name"]}, a {account["description"]}, from {account["country"]}."

def check_answer(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == "a"
    elif followers_b > followers_a:
        return guess == "b"

def game():
    score = 0
    account_a = pick_a_random_account(data)
    account_b = pick_a_random_account(data)
    should_continue = True

    print(logo)

    while should_continue:
        account_a = account_b
        account_b = pick_a_random_account(data)

        while account_a == account_b:
            account_b = pick_a_random_account(data)

        
        print(f"Compare A: {show_account_info(account_a)}")
        print(vs)
        print(f"Against B: {show_account_info(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        clear()
        print(logo)

        if check_answer(guess, account_a["follower_count"], account_b["follower_count"]):
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
    
game()
