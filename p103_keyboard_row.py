"""
Given a list of words, return all the words that require only a single
row of a keyboard to type.

Note: You may assume that all words only contain lowercase alphabetical
characters.

Ex: Given the following list of words...

words = ["two", "dad", "cat"], return ["two", "dad"].

Ex: Given the following list of words...

words = ["ufo", "xzy", "byte"], return [].
"""
from typing import List


def get_row(char: str) -> int:
    """Get the keyboard row index of a character"""
    rows = [
        'qwertyuiop',
        'asdfghjkl',
        'zxcvbnm',
    ]
    for index, row in enumerate(rows):
        if char in row:
            return index

    return -1


def equal_elements(array: List[int]) -> bool:
    """If all elements in an array are equal"""
    first = array[0]
    return array.count(first) == len(array)


def is_single_row(word: str) -> bool:
    """If all characters in a word are from the same keyboard row"""
    rows = [get_row(char) for char in word]
    return equal_elements(rows)


def main() -> None:
    """Main function"""
    words = ["two", "dad", "cat"]
    # words = ["ufo", "xzy", "byte"]

    print(list(filter(is_single_row, words)))


if __name__ == "__main__":
    main()
