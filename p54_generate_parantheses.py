"""
Given an integer N, where N represents the number of pairs of
parentheses (i.e. "(" and ")") you are given, return a list containing
all possible well-formed parentheses you can create.

Ex: Given the following value of N…

N = 3,
return [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]
"""
from typing import List


def build_bracket_sequence(
        count: int,
        close: int,
        perms: List[str],
        seq: str = '') -> List[str]:
    """Recursive function to find all possible bracket pairs"""
    if count == 0 and close == 0:
        perms.append(seq)

    if count > 0:
        build_bracket_sequence(count - 1, close, perms, seq + '(')
    if close > count:
        build_bracket_sequence(count, close - 1, perms, seq + ')')

    return perms


def get_bracket_perms(count: int) -> List[str]:
    """Returns permutations of all valid bracket pairs"""
    perms: List[str] = []
    return build_bracket_sequence(count, count, perms)


def main() -> None:
    """Main function"""
    count = int(input('Enter N: '))
    print(get_bracket_perms(count))


if __name__ == "__main__":
    main()
