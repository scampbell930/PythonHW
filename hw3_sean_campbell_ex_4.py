"""
Homework 3, Exercise 3
Name: Sean Campbell
Date: 10/07/2022
Description: This is a program that simulates playing a game of tic tac toe.
The game can receive user input for the location of the moves, but cannot determine
if a game has been won or not.
"""


# Function that displays an input game board, formatted, on the command line
def print_board(board: dict):
    # Display top index values
    print("%5d%4d%4d" % (0, 1, 2))

    # Loop through board to display elements
    for i in range(len(board)):
        # Check if last element in row
        if (i + 1) % 3 == 0:
            # Display element with new line
            print("| {} |".format(board[i]))
        else:
            # Check if row num need to be displayed
            if i % 3 == 0:
                # Display element
                print("{} | {} ".format(i//3, board[i]), end="")
            else:
                # Display element
                print("| {} ".format(board[i]), end="")


if __name__ == '__main__':
    # List to hold board data
    board = {0: ' ', 1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' '}

    user_one = False

    # Run the game until user quits
    while True:
        # Update user
        user_one = not user_one

        # Display game board and ask for input
        print_board(board)

        # Make sure board space is not taken
        while True:
            # Prompt user for input
            print("\nEnter Horizontal Coordinate:")
            x_coord = int(input())

            print("Enter Vertical Coordinate:")
            y_coord = int(input())

            # Test if space is empty
            if board[3 * y_coord + x_coord] != ' ':
                print("Entered space has already been used. Try again!")
            else:
                break

        # Calculate index from coordinates
        index = 3 * y_coord + x_coord

        # Store user character in board
        board[index] = 'X' if user_one else 'O'

