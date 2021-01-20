"""
Given a string s, return the length of the longest substring that
contains only unique characters.

Ex: Given the following string s...

s = "ababbc", return 2.

Ex: Given the following string s...

s = "abcdssa", return 5.
"""


def has_duplicates(string: str) -> bool:
    """Returns if a string has duplicate characters"""
    chars = set[str]()
    for char in string:
        if char in chars:
            return True

        chars.add(char)

    return False


def longest_substring_no_repetitions(string: str) -> str:
    """Return longest substring with no repeated characters"""
    start, end = 0, 0
    longest_substring = ''

    limit = len(string)
    while end < limit:
        while True:
            substring = string[start:end+1]

            if has_duplicates(substring):
                start += 1
                continue

            if len(substring) > len(longest_substring):
                longest_substring = substring

            break

        end += 1

    return longest_substring


def main() -> None:
    """Main function"""
    string = "ababbc"
    # string = "abcdssa"

    print(longest_substring_no_repetitions(string))


if __name__ == "__main__":
    main()
