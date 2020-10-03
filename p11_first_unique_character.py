"""
Given a string, return the index of its first unique character. If a
unique character does not exist, return -1.

Ex: Given the following strings...

"abcabd", return 2
"thedailybyte", return 1
"developer", return 0
"abcabc", return -1
"""

from typing import Dict


def main() -> None:
    """Main Function"""
    string = input('> ')
    unique_characters: Dict[str, int] = dict()
    for index, char in enumerate(string):
        if char in unique_characters:
            unique_characters.pop(char)
        else:
            unique_characters[char] = index

    first_unique_index = -1
    for index in unique_characters.values():
        if first_unique_index == -1 or index < first_unique_index:
            first_unique_index = index

    print(first_unique_index)


if __name__ == "__main__":
    main()
