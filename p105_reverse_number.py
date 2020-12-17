"""
Given a 32 bit signed integer, reverse it and return the result.
Note: You may assume that the reversed integer will always fit within
the bounds of the integer data type.

Ex: Given the following integer num...

num = 550, return 55

Ex: Given the following integer num...

num = -37, return -73
"""


def reverse(num: int) -> int:
    """Returns the reverse of a number"""
    negative = num < 0

    num = abs(num)
    reversed_num = 0
    while num:
        reversed_num *= 10
        reversed_num += num % 10
        num //= 10

    return -reversed_num if negative else reversed_num


def main() -> None:
    """Main function"""
    num = 550
    # num = -37

    print(reverse(num))


if __name__ == "__main__":
    main()
