"""
Homework 3, Exercise 1
Name: Sean Campbell
Date: 10/07/2022
Description: This program takes a grid created with a 2-dimensional list
and prints is after being rotated clock-wise by 90 degrees.
"""


if __name__ == '__main__':
    # Initialize grid to rotated heart shape
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    # Loop through whole grid, column wise
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            # Display element of grid
            if j != len(grid) - 1:
                print(grid[j][i], end="")
            else:
                print(grid[j][i])
