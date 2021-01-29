"""
Given two strings, s and t, return the length of their longest
subsequence.

Ex: Given the following strings s and t...

s = "xyz", t = "xyz". return 3.

Ex: Given the following strings s and t...

s = "abca", t = "acea", return 3.

Ex: Given the following strings s and t...

s = "abc", t = "def", return 0.
"""
from collections import Counter


def longest_common_subsequence(string1: str, string2: str) -> int:
    """Returns length of longest common subsequence"""
    counter = Counter(string1)

    common_count = 0
    for char in string2:
        if counter.get(char, 0) > 0:
            counter[char] -= 1
            common_count += 1

    return common_count


def main() -> None:
    """Main function"""
    string1, string2 = "xyz", "xyz"
    # string1, string2 = "abca", "acea"
    # string1, string2 = "abc", "def"

    print(longest_common_subsequence(string1, string2))


if __name__ == '__main__':
    main()
