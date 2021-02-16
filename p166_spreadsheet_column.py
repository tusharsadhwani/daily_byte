"""
Given a positive integer n, return its corresponding column title in an
excel spreadsheet.

Ex: Given the following values for n...

n = 1, return “A”.
n = 2, return “B”.
n = 3, return “C”.
n = 26, return “Z”.
n = 27, return “AA”.
n = 28, return “AB”.
"""
import string


def spreadsheet_column(num: int) -> str:
    """Returns nth spreadsheet column"""
    chars = []
    while num > 0:
        num -= 1
        chars.append(string.ascii_uppercase[num % 26])
        num //= 26

    return "".join(reversed(chars))


def main() -> None:
    """Main function"""
    num = 28

    print(spreadsheet_column(num))


if __name__ == '__main__':
    main()
