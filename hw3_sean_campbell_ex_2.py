"""
Homework 3, Exercise 2
Name: Sean Campbell
Date: 10/07/2022
Description: This program counts the number of individual characters in a spam message.
It will store the characters and their totals in a dictionary as a key-value pair, and will
be printed neatly after the totals are calculated
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
