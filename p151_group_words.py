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
from collections import Counter
from itertools import groupby


def group_anagrams(strings: list[str]) -> list[list[str]]:
    """Groups anagrams together"""
    anagrams: dict[frozenset[tuple[str, int]], list[str]] = {}

    for string in strings:
        counter = frozenset(Counter(string).items())
        if counter in anagrams:
            anagrams[counter].append(string)
        else:
            anagrams[counter] = [string]

    return list(anagrams.values())


def main() -> None:
    """Main function"""
    strings = ["car", "arc", "bee", "eeb", "tea"]

    print(group_anagrams(strings))


if __name__ == '__main__':
    main()
