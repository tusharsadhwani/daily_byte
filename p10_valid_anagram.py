"""Take two inputs and verify both are anagrams of each other"""

from collections import Counter, defaultdict
from typing import Dict


def check_anagram_alternative(word1: str, word2: str) -> bool:
    """Checks if two words are anagrams using builtin Counter"""
    word1_counter = Counter(word1)
    word2_counter = Counter(word2)
    return word1_counter == word2_counter


def check_anagram(word1: str, word2: str) -> bool:
    """Checks if two words are anagrams"""
    chars: Dict[str, int] = defaultdict(int)
    for char in word1:
        chars[char] += 1
    for char in word2:
        chars[char] -= 1

    return all(count == 0 for count in chars.values())


def main():
    """Main function"""
    word1 = input("Enter word1: ")
    word2 = input("Enter word2: ")

    is_anagram = check_anagram(word1, word2)
    print(is_anagram)


if __name__ == "__main__":
    main()
