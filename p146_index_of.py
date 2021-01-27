"""
Given two strings s and t, return the index of the first occurrence of t
within s if it exists; otherwise, return -1.

Ex: Given the following strings s and t...

s = "abc", t = "a", return 0.
Ex: Given the following strings s and t...

s = "abc", t = "abcd", return -1.
"""


def index_of(string: str, substring: str) -> int:
    """Returns first index of substring in string. If not found, returns -1"""
    index = 0

    length = len(string)
    sublength = len(substring)

    while index + sublength <= length:
        if string[index:index+sublength] == substring:
            return index

        index += 1

    return -1


def main() -> None:
    """Main function"""
    string, substring = "abc", "a"
    # string, substring = "abc", "abcd"

    print(index_of(string, substring))

    # Builtin
    try:
        print(string.index(substring))
    except ValueError:
        print(-1)


if __name__ == '__main__':
    main()
