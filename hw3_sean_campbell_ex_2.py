"""
Homework 3, Exercise 2
Name: Sean Campbell
Date: 10/07/2022
Description: FILL THIS IN
"""
import pprint

if __name__ == '__main__':
    # Prompt user for spam message input
    print("What is the spam message?")
    spam = input()

    # Dictionary to store characters and totals
    totals = {}

    # Loop through string and count characters
    for char in spam:
        if char in totals:
            totals[char] += 1
        else:
            totals[char] = 1

    # Display final totals
    pprint.pprint(totals)
