"""
Given an integer N, where N represents the number of pairs of
parentheses (i.e. "(" and ")") you are given, return a list containing
all possible well-formed parentheses you can create.

Ex: Given the following value of N...

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
        n_open: int,
        n_close: int,
        perms: List[str],
        seq: str = '') -> List[str]:
    """Recursive function to find all possible bracket pairs"""
    if n_open == 0 and n_close == 0:
        perms.append(seq)

    if n_open > 0:
        build_bracket_sequence(n_open - 1, n_close, perms, seq + '(')
    if n_close > n_open:
        build_bracket_sequence(n_open, n_close - 1, perms, seq + ')')

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
