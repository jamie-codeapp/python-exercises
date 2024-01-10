from art import logo
import os

bidders = {}
bidding_in_progress = True


def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def add_new_bidder(bid_list):
    try:
        name = input("What is your name?: ").lower()
        bid_amount = input("What's your bid?: $")
        bid_amount = float(bid_amount)
        bid_list[name] = bid_amount
    except ValueError:
        print("You should enter a bid amount.")


def find_winner(bid_list):
    winner = ""
    highest_bid = 0

    for name, bid_amount in bid_list.items():
        if bid_amount > highest_bid:
            winner = name.title()
            highest_bid = bid_amount

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


print(logo)
print("Welcome to the secret auction program.")

while bidding_in_progress:
    add_new_bidder(bidders)

    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n"
    ).lower()

    clear()

    if should_continue == "no":
        bidding_in_progress = False
        find_winner(bidders)
