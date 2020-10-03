"""
Given a string s containing only lowercase letters, continuously remove
adjacent characters that are the same and return the result.

Ex: Given the following strings...

s = "abccba", return ""
s = "foobar", return "fbar"
s = "abccbefggfe", return "a"
"""
from typing import List


def remove_adjacent_duplicates(string: str) -> str:
    """Removes adjacent duplicate characters from string"""
    stack: List[str] = []
    for char in string:
        if len(stack) > 0 and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    new_string = ''.join(stack)
    return new_string


def main() -> None:
    """Main function"""
    string = input('> ')
    print(remove_adjacent_duplicates(string))


if __name__ == "__main__":
    main()
