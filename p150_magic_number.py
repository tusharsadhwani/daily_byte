"""
Given an integer n, return whether or not it is a “magical” number. A
magical number is an integer such that when you repeatedly replace the
number with the sum of the squares of its digits its eventually becomes
one.

Ex: Given the following integer n...

n = 19, return true.
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1.

Ex: Given the following integer n...

n = 22, return false
"""


def is_magical(num: int) -> bool:
    """Returns if a number is magical or not"""
    previous_numbers = set[int]()

    while num != 1:
        previous_numbers.add(num)

        total = 0
        while num > 0:
            digit = num % 10
            total += digit ** 2
            num //= 10

        num = total
        print(num)

        if num in previous_numbers:
            return False

    return True


def main() -> None:
    """Main function"""
    num = 19
    # num = 22

    print(is_magical(num))


if __name__ == '__main__':
    main()
