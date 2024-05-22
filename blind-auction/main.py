import os
from art import logo

bids = {}
is_bidding = True


def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def add_bid(bid_records):
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bid_records[name] = price


def find_highest_bid(bid_records):
    winner = ""
    bid = 0
    for bidder in bid_records:
        if bid_records[bidder] > bid:
            winner = bidder
            bid = bid_records[bidder]
    print(f"The winner is {winner} with a bid of ${bid}")


print(logo)

while is_bidding:
    add_bid(bids)

    has_other_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n"
    ).lower()

    if has_other_bidders == "no":
        find_highest_bid(bids)
        is_bidding = False
    else:
        clear()
