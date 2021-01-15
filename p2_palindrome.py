"""Code that prints if a string is a palindrome or not"""


def iterate(text: str, forward_index: int, reverse_index: int) -> tuple[int, int]:
    """Finds the indices of the next set of alphabets in the string"""
    while not text[forward_index].isalpha():
        forward_index += 1
    while not text[reverse_index].isalpha():
        reverse_index -= 1

    return forward_index, reverse_index


def main() -> None:
    """Main function"""
    text = input('Enter a palindrome: ').lower()
    is_palindrome = True
    front, back = 0, len(text) - 1
    while front < back:
        front, back = iterate(text, front, back)
        if text[front] != text[back]:
            is_palindrome = False
            break
        front += 1
        back -= 1
    print(is_palindrome)


if __name__ == "__main__":
    main()

# Alternative:

# import re
# text = re.sub(r'[^A-Za-z]', '', input('Enter a palindrome: ')).lower()
# print(text == text[::-1])
