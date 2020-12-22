"""
Given an integer N, return the total number self divisible numbers that
are strictly less than N (starting from one).
Note: A self divisible number if a number that is divisible by all of
its digits.

Ex: Given the following value of N…

N = 17, return 12 because 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15 are all
self divisible numbers.
"""
from typing import Generator


def self_divisible_numbers(limit: int) -> Generator[int, None, None]:
    """Returns self divisible number upto limit"""
    for num in range(1, limit):
        digits = (int(digit) for digit in str(num))
        if all(digit != 0 and num % digit == 0 for digit in digits):
            yield num


def main() -> None:
    """Main function"""
    print(len(list(self_divisible_numbers(17))))


if __name__ == "__main__":
    main()
