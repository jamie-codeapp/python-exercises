# Python Exercises

This is a list of my Python exercises.

## Band Name Generator

1. Introduction:

-   Print a welcoming message for the user.

2. User Input:

-   Prompt the user to input the name of the city they grew up in.
-   Prompt the user to input their pet's name.

3. Band Name Generation:

-   Concatenate the city name and the pet's name.
-   Print the generated band name.

4. End of Program:

-   Execution of the program ends.

## Tip Calculator

1. Introduction:

-   Print a welcoming message for the user.

2. User Input:

-   Prompt the user to input the total bill amount.
-   Prompt the user to input the desired tip percentage (10, 12, or 15).
-   Prompt the user to input the number of people to split the bill.

3. Calculate Bill Per Person:

-   Calculate the amount each person should pay, including the tip.
-   Round the result to two decimal places.
-   Format the result as a string with two decimal places.

4. Print Result:

-   Print the amount each person should pay.

5. End of Program:

-   Execution of the program ends.

## Treasure Island

Here's an outline for the provided code:

1. ASCII Art:

-   Display ASCII art representing a decorative header.

2. Introduction:

-   Print welcoming messages for the user and introduce the game.

3. User Input - First Decision:

-   Prompt the user to choose a direction (left or right) at a crossroad.

4. Conditional Branching - First Decision:

-   If the user chooses "left":
    -   Prompt the user to decide whether to wait or swim at a lake.
-   If the user chooses "right":
    -   End the game with a message.

5. Conditional Branching - Second Decision:

-   If the user chose to wait:
    -   Prompt the user to choose a door color (red, yellow, or blue).
-   If the user chose to swim:
    -   End the game with a message.

6. Conditional Branching - Third Decision:

-   Depending on the chosen door color:
    -   If the user chose:
        -   "red": End the game with a message.
        -   "yellow": End the game with a winning message.
        -   "blue": End the game with a message.
        -   Any other input: End the game with a generic failure message.

7. End of Program:

## Rock Paper Scissors

1. Importing Module:

-   Import the random module to generate random numbers.

2. ASCII Art Definitions:

-   Define ASCII art representations for rock, paper, and scissors.

3. List of Choices:

-   Create a list containing ASCII art representations for rock, paper, and scissors.

4. User Input:

-   Prompt the user to choose between rock, paper, or scissors by typing 0, 1, or 2.
-   Convert the input to an integer.

5. Input Validation:

-   Check if the user's choice is between 0 and 2 (inclusive).
-   If not, print an error message and end the game.

6. Printing Choices:

-   Print the ASCII art representation corresponding to the user's choice.

7. Computer's Choice:

-   Generate a random choice for the computer using random.randint(0, 2).
-   Print the ASCII art representation corresponding to the computer's choice.

8. Determine Winner:

-   Compare the user's choice with the computer's choice to determine the winner.
-   Print the result (win, lose, or draw) based on the game rules:
    -   Rock crushes scissors (user wins).
    -   Scissors cut paper (user wins).
    -   Paper covers rock (user wins).
    -   If both choices are the same, it's a draw.

9. End of Program:

-   Execution of the program ends.
