"""
Code that prints if a string is a valid palindrome after removing at most one
charcater from the string.
"""
from typing import Tuple


def iterate(
        text: str,
        forward_index: int,
        reverse_index: int,
        can_skip: bool) -> Tuple[int, int, bool]:
    """Finds the indices of the next set of valid alphabets in the string."""
    if text[forward_index] == text[reverse_index]:
        return forward_index, reverse_index, True

    # The immediate next characters don't match.
    # So we have to check if we can skip a character and make the palindrome work.
    if not can_skip:
        return forward_index, reverse_index, False

    # Check the next immediate indices for equality
    if text[forward_index + 1] == text[reverse_index]:
        return forward_index + 1, reverse_index, False

    if text[forward_index] == text[reverse_index - 1]:
        return forward_index, reverse_index - 1, False

    # Not a palindrome, return unequal indices
    return forward_index, reverse_index, False


def main() -> None:
    """Main function"""
    text = input('Enter a palindrome: ').lower()
    front, back = 0, len(text) - 1
    is_palindrome = True
    can_skip = True
    while front < back:
        front, back, can_skip = iterate(text, front, back, can_skip)
        if text[front] != text[back]:
            is_palindrome = False
            break
        front += 1
        back -= 1
    print(is_palindrome)


if __name__ == "__main__":
    main()
