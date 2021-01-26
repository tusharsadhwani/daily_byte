"""
Given two strings s and t, return the index of the first occurrence of t
within s if it exists; otherwise, return -1.

Ex: Given the following strings s and t...

s = "abc", t = "a", return 0.
Ex: Given the following strings s and t...

s = "abc", t = "abcd", return -1.
"""


def main() -> None:
    """Main function"""
    string, substring = "abc", "a"
    # string, substring = "abc", "abcd"

    try:
        print(string.index(substring))
    except ValueError:
        print(-1)


if __name__ == '__main__':
    main()
