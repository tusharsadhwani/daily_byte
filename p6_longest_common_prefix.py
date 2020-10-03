"""Program that prints the longest common prefix from a list of words"""
from typing import List


def find_common_prefix_length(words: List[str]) -> int:
    """Returns the length of longest common prefix from the list of words"""
    smallest_word_length = min(len(word) for word in words)

    for index in range(smallest_word_length):
        ith_character = words[0][index]
        if not all(word[index] == ith_character for word in words):
            break
    else:
        # Whole length of the smallest word matched with every other word
        return smallest_word_length

    # The point at which the for loop broke is the length of the common prefix
    return index


def longest_common_prefix(words: List[str]) -> str:
    """Returns the common prefix in the list of words"""
    first_word = words[0]
    prefix_length = find_common_prefix_length(words)
    return first_word[:prefix_length]


def main() -> None:
    """Main function"""
    print(longest_common_prefix(["colorado", "color", "cold"]))
    print(longest_common_prefix(["a", "b", "c"]))
    print(longest_common_prefix(["spot", "spotty", "spotted"]))


if __name__ == "__main__":
    main()
