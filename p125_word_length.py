"""
Given a string, s, return the length of the last word.

Note: You may not use any sort of split() method.

Ex: Given the following string...

s = "The Daily Byte", return 4 (because "Byte" is four characters long).
"""
import re
from string import whitespace as WHITESPACE


def main() -> None:
    """Main function"""
    string = "The Daily Byte"

    for index, char in enumerate(reversed(string)):
        if char in WHITESPACE:
            print(index)
            break
    else:
        print(len(string))

    # Alternative
    print(len(string) - re.search(r'\b\w+$', string).start())  # type: ignore


if __name__ == "__main__":
    main()
