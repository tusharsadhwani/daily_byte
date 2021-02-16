"""
Given an array digits that represents a non-negative integer, add one to
the number and return the result as an array.

Ex: Given the following digits...

digits = [1, 2], return [1, 3].

Ex: Given the following digits...

digits = [9, 9], return [1, 0, 0].
"""


def add_one(digits: list[int]) -> list[int]:
    """Adds one"""
    carry = True
    new_digits = []
    for digit in reversed(digits):
        if carry:
            digit += 1
            if digit == 10:
                digit = 0
            else:
                carry = False

        new_digits.append(digit)

    if carry:
        new_digits.append(1)

    new_digits.reverse()
    return new_digits


def main() -> None:
    """Main function"""
    digits = [1, 2]
    # digits = [9, 9]

    print(add_one(digits))


if __name__ == '__main__':
    main()
