'''
Homework 2, Exercise 3
Name: Sean Campbell
Date: 9/23/22
Description: This is a program that manipulates a list of string elements
and then concatenates them together in a sentence format.
'''


# Function takes list of elements and concatenates them
# together
def strList(items: list) -> str:
    result = ""

    # Loop through all elements in list
    for i in range(len(items)):
        # Check is element is not last in list and concatenate
        if i != len(items) - 1:
            result += items[i] + ", "
        # Concatenate last element
        else:
            result += "and " + items[i]

    return result


if __name__ == '__main__':
    # Step 1
    items = ['Wallet', 'Phone', 'Keys']
    print(items)

    # Step 2
    items.sort()
    print(items)

    # Step 3
    print(items[0])

    # Step 4
    print(items[1:])

    # Step 5
    print(items[-1])

    # Step 6
    print(items.index('Keys'))

    # Step 7
    items.append('Tablet')
    print(items)

    # Step 8
    items.insert(1, 'Mask')
    print(items)

    # Step 9
    items.remove('Phone')
    print(items)

    # Step 10
    items = items[::-1]
    print(items)

    # Step 11
    print(strList(items))
