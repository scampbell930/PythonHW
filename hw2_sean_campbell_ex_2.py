
def collatz(number: int) -> int:
    even = number % 2 == 0

    if even:
        new_value = number // 2
        print(new_value)
        return new_value
    else:
        new_value = 3 * number + 1
        print(new_value)
        return new_value


if __name__ == '__main__':

    while True:
        try:
            print("Enter number:")
            input = int(input())
            break
        except ValueError:
            print("Input must be an integer")

    while(input != 1):
        input = collatz(input)
