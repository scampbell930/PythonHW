
def strList(items: list) -> str:
    result = ""

    for i in range(len(items)):
        if i != len(items) - 1:
            result += items[i] + ", "
        else:
            result += "and " + items[i]

    return result


if __name__ == '__main__':
    items = ['Wallet', 'Phone', 'Keys']
    print(items)

    items.sort()
    print(items)

    print(items[0])

    print(items[1:])

    print(items[-1])

    print(items.index('Keys'))

    items.append('Tablet')

    items.insert(1, 'Mask')
    print(items)

    items.remove('Phone')
    print(items)

    items = items[::-1]
    print(items)

    print(strList(items))
