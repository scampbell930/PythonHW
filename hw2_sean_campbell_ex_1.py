'''
Homework 2, Exercise 1
Name: Sean Campbell
Date: 9/23/22
Description: This is a program that takes a user input integer and feeds it
into a function collatz which either returns the input // 2 or the input * 3 + 1.
It will repeat this function until the return value is equal to one.
'''


# Function that takes an integer input and returns another integer
# depending on if the number is either even or odd
def collatz(number: int) -> int:
    # Determine if input is even or odd
    even = number % 2 == 0

    # Check if even
    if even:
        # Calculate the new return value
        new_value = number // 2
        print(new_value)
        return new_value
    # If odd
    else:
        # Calculate the new return value
        new_value = 3 * number + 1
        print(new_value)
        return new_value


if __name__ == '__main__':
    # Prompt and receive user input
    print("Enter number:")
    input = int(input())

    # Call collatz function until the return value is 1
    while(input != 1):
        input = collatz(input)
