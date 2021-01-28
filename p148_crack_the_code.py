"""
Given a string s and a string code, return whether or not s could have
been encrypted using the pattern represented in code.

Ex: Given the following s and code...

s = “the daily byte”, code = “abc”, return true

Ex: Given the following s and code...

s = “the daily byte curriculum”, code = “abcc”, return false because ‘c’
in code already maps to the word “byte”
"""


def check_valid_code(string: str, code: str) -> bool:
    """Returns if the string can be represented by the pattern in code"""
    words = string.split()

    code_mapping: dict[str, str] = {}

    for char, word in zip(code, words):
        if char in code_mapping:
            return False

        code_mapping[char] = word

    return True


def main() -> None:
    """Main function"""
    string = "the daily byte"
    code = "abc"
    # string = "the daily byte curriculum"
    # code = "abcc"

    print(check_valid_code(string, code))


if __name__ == '__main__':
    main()
