"""
Homework 1
Name: Sean Campbell
Date: 9/2/22
Description of you program: This is a small security program that asks a series of
questions to the user and will only display the secret information if all the answers are
correct. This program uses many python practices to achieve this goal.
"""
import random

if __name__ == '__main__':
    # Initialize variables for answers
    secret_int = 3
    secret_float = 6.126
    middle_name = "DavidDavidDavidDavid"

    # Loop until all answers are correct
    not_correct = True
    while not_correct:

        # Initialize user input booleans
        user_int_correct = False
        user_float_correct = False
        user_name_correct = False

        # Loop through the three security questions
        for i in range(3):
            if i == 0:
                # Gather user input
                print("What is the secret integer?")
                user_int = int(input())

                # Calculate new value
                user_int = user_int % 6

                if user_int == secret_int:
                    user_int_correct = True
                else:
                    break

            elif i == 1:
                # Gather user input
                print("What is the secret float?")
                user_float = float(input())
                user_float = 3.125 - user_float

                # Check if final float value is within acceptable range
                if (user_float > secret_float - 0.1) and (user_float < secret_float + 0.1):
                    user_float_correct = True
                else:
                    break

            else:
                # Gather user input
                print("What is the secret string?")
                user_name = input()

                # Check if string is empty
                if not len(user_name):
                    # Receive more secret input
                    user_name = input()

                    # Calculate final string
                    user_name = user_name * 4

                    # Check if new string is correct
                    if user_name == middle_name:
                        user_name_correct = True
                    else:
                        break

        # Generate random number from 0 to 2
        lucky_num = random.randint(0, 3)

        # Check if lucky number is going to skip this iteration
        if not lucky_num:
            continue

        # Check if all answers are correct
        elif user_name_correct and user_float_correct and user_int_correct:
            # Print secret information and exit loop
            secret = 97236923503740721340
            print("Welcome! The secret information is: " + str(secret))
            not_correct = False
