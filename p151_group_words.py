"""
Given a list of strings, return a list of strings containing all
anagrams grouped together.

Ex: Given the following list of strings strs...

strs = ["car", "arc", "bee", "eeb", "tea"], return
[
  ["car","arc"],
  ["tea"],
  ["bee","eeb"]
]
"""
from itertools import groupby
from collections import Counter


def group_anagrams(strings: list[str]) -> list[list[str]]:
    """Groups anagrams together"""
    return [list(group) for _, group in groupby(strings, key=Counter)]


def main() -> None:
    """Main function"""
    strings = ["car", "arc", "bee", "eeb", "tea"]

    print(group_anagrams(strings))


if __name__ == '__main__':
    main()
