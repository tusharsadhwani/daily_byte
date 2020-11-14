"""
Given a string of digits, return all possible text messages those digits
could send. Note: The mapping of digits to letters is as follows...

0 -> null
1 -> null
2 -> "abc"
3 -> "def"
4 -> "ghi"
5 -> "jkl"
6 -> "mno"
7 -> "pqrs"
8 -> "tuv"
9 -> "wxyz"

Ex: digits = "23",
return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""
from typing import Dict, List


def generate_t9_messages(digits: str) -> List[str]:
    """Generate all possible strings from given T9 input"""
    char_map: Dict[int, str] = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    }

    perms: List[str] = []
    for digit_char in digits:
        digit = int(digit_char)

        chars = char_map.get(digit)
        if chars is None:
            continue

        if len(perms) == 0:
            perms = list(chars)
        else:
            perms = [head + char for head in perms for char in chars]

    return perms


def main() -> None:
    """Main function"""
    digits = input('> ')

    messages = generate_t9_messages(digits)
    print(messages)


if __name__ == "__main__":
    main()
