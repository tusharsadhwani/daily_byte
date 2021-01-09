"""
Given an array of words, return the length of the longest phrase,
containing only unique characters, that you can form by combining the
given words together.

Ex: Given the following words...

words = ["the","dog","ran"], return 9 because you can combine all the
words, i.e. "the dog ran" since all the characters in the phrase are
unique.

Ex: Given the following words...

words = ["the","eagle","flew"], return 4 because "flew" is the longest
phrase you can create without using duplicate characters.
"""
from itertools import chain, combinations
from typing import List, Set


def contain_duplicates(*strings: str) -> bool:
    """Returns if given strings contain repeated chatacters"""
    chars: Set[str] = set()

    for string in strings:
        for char in string:
            if char in chars:
                return True

            chars.add(char)

    return False


def longest_phrase(words: List[str]) -> int:
    """Returns length of longest phrase without repeated chatacters"""
    sizes = range(len(words) + 1)
    word_combos = chain.from_iterable(combinations(words, r=n) for n in sizes)

    max_phrase_length = 0
    for word_combo in word_combos:
        if not contain_duplicates(*word_combo):
            phrase_length = sum(len(word) for word in word_combo)
            if phrase_length > max_phrase_length:
                max_phrase_length = phrase_length

    return max_phrase_length


def main() -> None:
    """Main function"""
    words = ["the", "dog", "ran"]
    # words = ["the", "eagle", "flew"]

    print(longest_phrase(words))


if __name__ == "__main__":
    main()
