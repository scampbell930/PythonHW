'''
Homework 2, Exercise 4.1
Name: Sean Campbell
Date: 9/23/22
Description: This program is a number guessing program where the user
tries to guess the number and the program will tell the user if they are
correct, too high, or too low.
'''
import random

if __name__ == '__main__':
    # Calculate number to guess and set guesses
    value = random.randint(1, 21)
    num_tries = 10

    print("I am thinking of a number between 1 and 20. You have 10 tries.")

    # Loop until tries are out or user is correct
    while num_tries >= 0:
        # Check if any tries are left
        if num_tries == 0:
            print("Sorry, the number I was thinking of was " + str(value))
            break

        # Prompt user
        print("Take a guess.")
        user_input = int(input())

        # Decrease tries
        num_tries -= 1

        # Check if user is correct, too high, or too low
        if user_input == value:
            print("Good job! You guessed my number in " + str(10 - num_tries) + " guesses!")
            break
        elif user_input < value:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
