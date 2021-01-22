"""
Given a string and a character, return an array of integers where each
index is the shortest distance from the character.

Ex: Given the following string s and character c...

s = "dailybyte", c = 'y', return [4, 3, 2, 1, 0, 1, 0, 1, 2]
"""
from collections import deque
from typing import Deque


def shortest_distance(string: str, value: str) -> list[int]:
    """Return shortest distance of every index from nearest char value"""
    indices: Deque[int] = deque()
    for index, char in enumerate(string):
        if char == value:
            indices.append(index)

    distances = list[int]()
    current_index = indices.popleft()
    is_empty = len(indices) == 0

    for index, char in enumerate(string):
        if not is_empty and index > current_index:
            current_index = indices.popleft()
            is_empty = len(indices) == 0

        distances.append(abs(index - current_index))

    return distances


def main() -> None:
    """Main function"""
    string = "dailybyte"
    value = "y"

    print(shortest_distance(string, value))


if __name__ == '__main__':
    main()
