"""
Given a string, reverse the vowels of it.
Note: In this problem y is not considered a vowel.

Ex: Given the following strings s...

s = "computer", return "cemputor"

Ex: Given the following strings s...

s = "The Daily Byte", return "The Dialy Byte"
"""

from typing import List


def reverse_vowels(string: str) -> str:
    """Reverse the vowels in the string"""
    vowels: List[int] = []
    for idx, char in enumerate(string):
        if char.lower() in 'aeiou':
            vowels.append(idx)

    chars = list(string)

    half_length = len(vowels) // 2
    for i in range(half_length):
        idx = vowels[i]
        reverse_idx = vowels[-1-i]
        chars[idx], chars[reverse_idx] = chars[reverse_idx], chars[idx]

    return ''.join(chars)


def main() -> None:
    """Main function"""
    string = "computer"
    # string = "The Daily Byte"

    print(reverse_vowels(string))


if __name__ == "__main__":
    main()
