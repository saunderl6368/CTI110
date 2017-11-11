# Write a program that has the user guess a secret number
# 11/10/2017
# CTI-110 M6HW2-Random Number Guessing Game
# Laura Saunders
#
# Write a program that generates a random number from 1-100.
# Ask the user to guess the secret number.
# If the guess is too high, tell the user "Too high, try again."
# If the guess is too low, tell the user "Too low, try again."
# If the user guesses the number, congratulate the user.
# Ask the user if they want to play again.
# Have the program keep track of the number of guesses made (Extra Credit).


import random

def main():
    numberOfGuesses = 0
    userNumber = 0
    again = "y"
    
    # Program will generate a random number from 1-100.
    secretNumber = random.randint (1,100)

    while again == "y":

        while userNumber != secretNumber:
            # User guesses the secret number.
            userNumber = int( input( "Guess the secret number: "))
            # The program will keep track of the number of guesses made.
            numberOfGuesses = numberOfGuesses + 1

            # The program will tell the user if the guess is too low, too high, or correct.
            if userNumber < secretNumber:
                print("Too low, try again.")
            elif userNumber > secretNumber:
                print("Too high, try again.")
            elif userNumber == secretNumber:
                print("Congratulations! You guessed correctly! You guessed in", numberOfGuesses, "guesses.")

        # Ask the user if they want to play again.
        again = input("Play again? (y for yes): ")
        secretNumber = random.randint (1,100)
        numberOfGuesses = 0

# Call the main function.    
main()
    
