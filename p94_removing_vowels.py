"""
Given a string s remove all the vowels it contains and return the
resulting string.

Note: In this problem y is not considered a vowel.

Ex: Given the following string s...

s = "aeiou", return ""
Ex: Given the following string s...

s = "byte", return "byt"
Ex: Given the following string s...

s = "xyz", return "xyz"
"""


def main() -> None:
    """Main function"""
    string = input('> ')
    for vowel in 'aeiou':
        string = string.replace(vowel, '')

    print(string)


if __name__ == "__main__":
    main()
