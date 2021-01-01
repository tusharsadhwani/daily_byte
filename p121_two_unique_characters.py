"""
Given a string s, return the length of the longest substring containing
at most two distinct characters.

Note: You may assume that s only contains lowercase alphabetical
characters.

Ex: Given the following value of s...

s = "aba", return 3.

Ex: Given the following value of s...

s = "abca", return 2.
"""


def substr_at_most_two_distinct_chars(string: str) -> str:
    """Finds the longest substring with at most two distinct characters"""
    if len(string) < 2:
        return string

    start, end = 0, 1
    longest_substring = ''

    limit = len(string)
    while end < limit:
        while True:
            substring = string[start:end+1]

            if len(set(substring)) > 2:
                start += 1
                continue

            if len(substring) > len(longest_substring):
                longest_substring = substring

            break

        end += 1

    return longest_substring


def main() -> None:
    """Main function"""
    string = "aba"
    # string = "abca"

    print(len(substr_at_most_two_distinct_chars(string)))


if __name__ == "__main__":
    main()
