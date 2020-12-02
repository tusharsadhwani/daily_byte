"""
Given a character array, compress it in place and return the new length
of the array.

Note: You should only compress the array if its compressed form will be
at least as short as the length of its original form.

Ex: Given the following character array chars…

chars = ['a', 'a', 'a', 'a', 'a', 'a'], return 2.
chars should be compressed to look like the following:
chars = ['a', '6']

Ex: Given the following character array chars…

chars = ['a', 'a', 'b', 'b', 'c', 'c'], return 6.
chars should be compressed to look like the following:
chars = ['a', '2', 'b', '2', 'c', '2']

Ex: Given the following character array chars…

chars = ['a', 'b', 'c'], return 3.
In this case we chose not to compress chars.
"""


from typing import List, Optional


def compress_chars(chars: List[str]) -> List[str]:
    """Returns compressed form of the chars"""
    compressed: List[str] = []

    char = chars[0]
    count = 1
    for next_char in chars[1:]:
        if char == next_char:
            count += 1
            continue

        if count == 1:
            compressed.append(char)
            char = next_char
            continue

        compressed.append(char)
        compressed.append(f'{count}')
        count = 1

        char = next_char

    if count == 1:
        compressed.append(char)
    else:
        compressed.append(char)
        compressed.append(f'{count}')

    return compressed


def main() -> None:
    """Main function"""

    chars = ['a', 'a', 'a', 'a', 'a', 'a']
    # chars = ['a', 'a', 'b', 'b', 'c', 'c']
    # chars = ['a', 'b', 'c']

    compressed = compress_chars(chars)
    print(len(compressed))


if __name__ == "__main__":
    main()
