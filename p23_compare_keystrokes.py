"""
Given two strings s and t, which represents a sequence of keystrokes,
where # denotes a backspace, return whether or not the sequences produce
the same result.

Ex: Given the following strings...

s = "ABC#", t = "CD##AB", return true
s = "como#pur#ter", t = "computer", return true
s = "cof#dim#ng", t = "code", return false
"""
from typing import List


def apply_backspaces(string: str) -> str:
    """Process the string with backspace characters into its result"""
    new_string_chars: List[str] = []
    for char in string:
        if char == '#':
            try:
                new_string_chars.pop()
            except IndexError:
                raise ValueError('Too many backspaces')
        else:
            new_string_chars.append(char)

    new_string = ''.join(new_string_chars)
    return new_string


def main() -> None:
    """Main function"""
    string1 = apply_backspaces(input('> '))
    string2 = apply_backspaces(input('> '))

    print(string1 == string2)


if __name__ == "__main__":
    main()
