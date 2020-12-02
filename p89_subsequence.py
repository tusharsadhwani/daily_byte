"""
Given two strings s and t return whether or not s is a subsequence of t.

Note: You may assume both s and t only consist of lowercase characters
and both have a length of at least one.

Ex: Given the following strings s and t...

s = "abc", t = "aabbcc", return true.

Ex: Given the following strings s and t...

s = "cpu", t = "computer", return true.

Ex: Given the following strings s and t...

s = "xyz", t = "axbyc", return false.
"""


from typing import Counter


def is_subsequence(sequence: str, subsequence: str) -> bool:
    """Returns if given subsequence is a valid subsequence or not"""
    seq_counter = Counter(sequence)
    subseq_counter = Counter(subsequence)

    for item, count in subseq_counter.items():
        if seq_counter[item] < count:
            return False

    return True


def main() -> None:
    """Main function"""
    subsequence, sequence = "abc", "aabbcc"
    # subsequence, sequence = "cpu", "computer"
    # subsequence, sequence = "xyz", "axbyc"

    print(is_subsequence(sequence, subsequence))


if __name__ == "__main__":
    main()
