"""
Given a positive integer N, return the number of prime numbers less than
N.

Ex: Given the following N…

N = 3, return 1.
2 is the only prime number less than 3.

Ex: Given the following N…

N = 7, return 3.
2, 3, and 5 are the only prime numbers less than 7.
"""
from math import ceil, sqrt
from typing import Generator


def generate_primes() -> Generator[int, None, None]:
    """Generates primes"""
    counter = 2
    while True:
        is_prime = True

        upper_limit = sqrt(counter)
        if upper_limit % 1 == 0:
            upper_limit += 1
        upper_limit = ceil(upper_limit)

        for i in range(2, upper_limit):
            if counter % i == 0:
                is_prime = False

        if is_prime:
            yield counter
        counter += 1


def count_primes_upto(num: int) -> int:
    """Counts number of primes less than num"""
    count = 0
    for prime in generate_primes():
        if prime >= num:
            break

        count += 1

    return count


def main() -> None:
    """Main function"""
    num = 3
    # num = 7

    print(count_primes_upto(num))


if __name__ == "__main__":
    main()
