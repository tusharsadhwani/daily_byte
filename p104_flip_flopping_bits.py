"""
Given a positive integer N, return whether or not it has alternating bit
values.

Ex: Given the following value for N...

N = 5, return true.
5 in binary is 101 which alternates bit values between 0 and 1.

Ex: Given the following value for N...

N = 8, return false
8 in binary is 1000 which does not alternate bit values between 0 and 1.
"""
from itertools import cycle


def is_alternating(string: str) -> bool:
    """Returns if a string is composed of alternating characters"""
    if len(string) < 2:
        return True

    alternate_chars = string[:2]
    return all(char1 == char2
               for char1, char2 in zip(string, cycle(alternate_chars)))


def is_flip_flopping_bits(num: int) -> bool:
    """Return if a number has alternating bits"""
    num_binary = f'{num:b}'
    return is_alternating(num_binary)


def main() -> None:
    """Main function"""
    num = 5
    # num = 8

    print(is_flip_flopping_bits(num))


if __name__ == "__main__":
    main()
