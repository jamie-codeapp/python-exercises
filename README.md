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

## Password Generator

1. Importing Module:

-   Import the random module to generate random elements.

2. Data Preparation:

-   Define lists containing letters, symbols, and numbers.

3. Introduction:

-   Print a welcoming message for the user.

4. User Input:

-   Prompt the user to input the desired number of letters, symbols, and numbers for the password.

5. Password Generation:

-   Create an empty list to store the characters of the password.

6. For Loop - Letters:

-   Use a for loop to iterate over the desired number of letters.
-   Randomly select a letter from the letters list and append it to the password list.

7. For Loop - Symbols:

-   Use a for loop to iterate over the desired number of symbols.
-   Randomly select a symbol from the symbols list and append it to the password list.

8. For Loop - Numbers:

-   Use a for loop to iterate over the desired number of numbers.
-   Randomly select a number from the numbers list and append it to the password list.

9. Shuffling the Password List:

-   Shuffle the elements of the password list to randomize the order of characters.

10. Password Construction:

-   Join the elements of the password list into a single string to form the password.

11. Print Result:

-   Print the generated password to the user.

12. End of Program:

-   Execution of the program ends.

## Hangman

1. Importing Modules and Resources

-   To import necessary functions and variables from other modules.

2. Initialization

-   To set initial game variables.

3. Game Loop

-   To repeatedly prompt the user for guesses and update the game state accordingly.

    1. Check for Repeated Guesses

    -   To inform the user if they have already guessed a letter.

    2. Update Display

    -   To reveal correctly guessed letters in the display list.

    3. Check for Win Condition

    -   To determine if the user has guessed the entire word.

    4. Handle Incorrect Guesses

    -   To decrement lives and notify the user if the guess is incorrect.

    5. Check for Lose Condition

    -   To determine if the user has run out of lives.

4. Display Current State

-   To print the current state of the display list and remaining lives (using the stages art).

5.  End of Program

-   The program completes its execution when the game ends (either win or lose).

## Caesar Cipher

1. Importing Module and Constants

-   To import necessary functions and variables.

2. Global Variable

-   To control the loop for repeated user interaction.

3. Define the Caesar Cipher Function

-   To perform the Caesar cipher encoding or decoding.

4. User Interaction Loop

-   To repeatedly interact with the user for encoding/decoding messages until they choose to exit.

5. End of Program

-   The program completes its execution when the user chooses not to continue.

## Blind Auction

1. Importing Modules and Constants

-   To import necessary functions and variables.

2. Initialization

-   To set initial game variables.

3. Define the Clear Function

-   To clear the console for better user experience.

4. Define the Add Bid Function

-   To collect a new bid from the user and add it to the `bids` dictionary.

5. Define the Find Highest Bid Function

-   To find and announce the highest bid from the `bids` dictionary.

6. Main Program Loop

-   To repeatedly prompt for bids until there are no more bidders.

7. End of Program

-   The program completes its execution when the bidding process ends.

## Calculator

1. Importing Module

-   To import necessary functions and variables.

2. Define Basic Arithmetic Functions

-   To perform basic arithmetic operations.

3. Define Operations Dictionary

-   To map operation symbols to their corresponding functions.

4. Define Calculate Function

-   To handle user interaction and perform calculations.

5. Start the Calculator

-   To begin the calculator program by calling the `calculate` function.

6. End of Program

-   The program completes its execution when the user decides to stop calculating.
