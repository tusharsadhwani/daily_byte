"""
Given a string, return whether or not it uses capitalization correctly.
A string correctly uses capitalization if all letters are capitalized,
no letters are capitalized, or only the first letter is capitalized.

Ex: Given the following strings...

"USA", return True
"Calvin", return True
"compUter", return False
"coding", return True
"""


def check_capitalization(string: str) -> bool:
    """Checks the capitalization of the string and returns if it is valid."""
    first_char, second_char, *_ = list(string)

    if first_char.islower() and second_char.isupper():
        return False

    uppercase_string = second_char.isupper()
    for char in string[1:]:
        if uppercase_string and char.islower():
            return False
        if not uppercase_string and char.isupper():
            return False

    return True


def main():
    """Main function"""
    string = input('> ')
    result = check_capitalization(string)
    print(result)


if __name__ == "__main__":
    main()


# Alternative:

# string = input('> ')
# print(string.islower() or string.isupper() or string.istitle())
