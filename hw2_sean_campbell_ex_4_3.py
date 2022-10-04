'''
Homework 2, Exercise 4.2
Name: Sean Campbell
Date: 9/23/22
Description: This program is a number guessing program where the user
tries to guess the number and the program will tell the user if they are
correct, too high, or too low. Unlike ex 4.2 this exercise generates random endpoints
and has the program automatically guess the next number and keep track of previous guesses
'''
import random

if __name__ == '__main__':
    guesses = []

    # Calculate endpoints
    while True:
        lower = random.randint(1, 1000)
        upper = random.randint(1, 1000)

        # Make sure lower is less than upper
        if lower < upper:
            break

    # Calculate number to guess and set guesses
    value = random.randint(lower, upper)
    num_tries = 10

    print("I am thinking of a number between " + str(lower) + " and " + str(upper) + ". You have 10 tries.")

    # Loop until tries are out or user is correct
    while num_tries >= 0:
        # Check if any tries are left
        if num_tries == 0:
            print("Sorry, the number I was thinking of was " + str(value))
            break

        # Calculate guess
        print("Take a guess.")
        while True:
            guess = random.randint(lower, upper)

            if guess not in guesses:
                print(guess)
                break

        # Decrease tries
        num_tries -= 1

        # Check if user is correct, too high, or too low
        if guess == value:
            print("Good job! You guessed my number in " + str(10 - num_tries) + " guesses!")
            break
        elif guess < value:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
