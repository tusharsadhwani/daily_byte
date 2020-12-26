"""
Given a string s, reverse the words.
Note: You may assume that there are no leading or trailing whitespaces
and each word within s is only separated by a single whitespace.

Ex: Given the following string s...

s = "The Daily Byte", return "Byte Daily The".
"""


def main() -> None:
    """Main function"""
    string = "The Daily Byte"
    print(' '.join(reversed(string.split())))


if __name__ == "__main__":
    main()
