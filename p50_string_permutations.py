"""
Given a string s consisting of only letters and digits, where we are
allowed to transform any letter to uppercase or lowercase, return a list
containing all possible permutations of the string.

Ex: Given the following string...

S = "c7w2", return ["c7w2", "c7W2", "C7w2", "C7W2"]
"""
from typing import List


def string_perms(string: str) -> List[str]:
    """Recursive implementation of string permutations"""
    if len(string) == 0:
        return ['']

    perms = []
    char, rest = string[0], string[1:]

    if not char.isalpha():
        perms += [char + tail for tail in string_perms(rest)]
        return perms

    lower_perms = [char.lower() + tail for tail in string_perms(rest)]
    perms += lower_perms

    upper_perms = [char.upper() + tail for tail in string_perms(rest)]
    perms += upper_perms

    return perms


def main() -> None:
    """Main function"""
    string = input('> ')

    permutations = string_perms(string)
    print(permutations)


if __name__ == "__main__":
    main()
