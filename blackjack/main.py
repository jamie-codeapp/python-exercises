import random
import os
from art import logo


def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    return random.choice(cards)


def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return -1
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if computer_score == -1:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == -1:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif user_score == computer_score:
        return "Draw 🙃"
    elif computer_score > 21:
        return "Opponent went over. You win 😬"
    elif user_score > computer_score:
        return "You win 🙂"
    else:
        return "You lose 😤"


def play_game():
    user_in_the_game = True
    user_cards = []
    computer_cards = []

    print(logo)

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while user_in_the_game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        if user_score == -1 or computer_score == -1 or user_score > 21:
            user_in_the_game = False
        else:
            print(f"   Your cards: {user_cards}, current score: {user_score if user_score != -1 else "Blackjack"}")
            print(f"   Computer's first card: {computer_cards[0]}")

            if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                user_cards.append(deal_card())
            else:
                user_in_the_game = False

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"   Your final hand: {user_cards}, final score: {user_score if user_score != -1 else "Blackjack"}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score if computer_score != -1 else "Blackjack"}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
