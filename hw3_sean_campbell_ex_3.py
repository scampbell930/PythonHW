"""
Homework 3, Exercise 3
Name: Sean Campbell
Date: 10/07/2022
Description: This program simulates a stores inventory. It stores the inventory
in a dictionary with the name and quantity being the key-value pair. The user can add or
remove items from the inventory, and they can be printed neatly with the printInventory
function
"""


# Function that takes an input inventory and displays it in a nicely formatted table
def printInventory(inventory: dict):
    # Display table header
    print("%-18s%-15s" % ("Item", "Number of item"))

    # Display inventory elements and totals
    for item in inventory:
        print("%-18s%-15d" % (item, inventory[item]))


# Function that adds a given input string to the inventory, if already in inventory then increment total
def addItem(inventory: dict, item: str):
    # Check if item is already in inventory
    if item in inventory:
        # Increment total
        inventory[item] += 1
    else:
        # Add item to inventory
        inventory[item] = 1


# Function that removes an item from inventory, or decrements total items. If item total is alreay
# 0, an error message will display
def deleteItem(inventory: dict, item: str):
    # Check if item is in inventory
    if (item not in inventory) or (inventory[item] == 0):
        print("{} cannot be deleted any further.".format(item))
    else:
        # Decrement total
        inventory[item] -= 1


if __name__ == '__main__':
    # Store inventory in dict
    inventory = {'Hand sanitizer': 10,
                 'Soap': 6,
                 'Kleenex': 22,
                 'Lotion': 16,
                 'Razors': 12}

    # Step 2
    printInventory(inventory)

    # Step 3
    addItem(inventory, 'Advil')
    addItem(inventory, 'Lotion')
    print()
    printInventory(inventory)

    # Step 4
    deleteItem(inventory, 'Soap')
    deleteItem(inventory, 'Advil')
    print()
    printInventory(inventory)
    deleteItem(inventory, 'Advil')
