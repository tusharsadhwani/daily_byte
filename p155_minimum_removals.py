"""
Given a string s, remove the minimum number of parentheses to make s
valid. Return all possible results.

Ex: Given the following string s...

s = "(()()()", return ["()()()","(())()","(()())"].

Ex: Given the following string s...

s = "()()()", return ["()()()"].
"""
from collections import deque
from typing import Deque


def valid_parens(parens: str) -> bool:
    """Returns if given parens are valid or not"""
    count = 0

    for char in parens:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        else:
            raise ValueError('input has non-parens')

        if count < 0:
            return False

    return count == 0


def remove_invalids(string: str) -> list[str]:
    """Removes minimum number of parens to make them valid"""
    visited: set[str] = set()

    queue: Deque[str] = deque()
    queue.append(string)
    visited.add(string)

    output: list[str] = []
    min_length_reached = False
    while queue:
        parens = queue.popleft()

        if valid_parens(parens):
            output.append(parens)
            min_length_reached = True

        if min_length_reached:
            # prevents smaller solutions being found
            continue

        for index, char in enumerate(parens):
            if char not in '()':
                raise ValueError('input has non-parens')

            candidate = parens[:index] + parens[index+1:]
            if candidate not in visited:
                queue.append(candidate)
                visited.add(candidate)

    return output if output else ['']


def main() -> None:
    """Main function"""
    string = "(()()()"
    # string = "()()()"

    print(remove_invalids(string))


if __name__ == '__main__':
    main()
