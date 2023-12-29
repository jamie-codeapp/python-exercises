import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rock_paper_scissors = [rock, paper, scissors]


def convert_to_int(input):
    try:
        return int(input)
    except ValueError:
        pass


user_input = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
)

user_choice = convert_to_int(user_input)

if user_choice != None:
    if user_choice < 0 or user_choice > 2:
        print("You typed an invalid number, you lose!")
    else:
        print(rock_paper_scissors[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(rock_paper_scissors[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("You win!")
        elif computer_choice == 0 and user_choice == 2:
            print("You lose.")
        elif user_choice > computer_choice:
            print("You win!")
        elif computer_choice > user_choice:
            print("You lose.")
        elif user_choice == computer_choice:
            print("It's a draw.")
else:
    print("You should enter 0, 1 or 2.")
