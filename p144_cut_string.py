"""
Given a string s containing only lowercase characters, return a list of
integers representing the size of each substring you can create such
that each character in s only appears in one substring.

Ex: Given the following string s...

s = "abacdddecn", return [3, 6, 1]

Ex: Given the following string s...

s = "aba", return [3]
"""


def cut_string(string: str) -> list[int]:
    """Returns the lengths of the cut substrings"""
    last_indices: dict[str, int] = {}
    for index, char in enumerate(string):
        last_indices[char] = index

    index = 0
    end = len(string)

    substring_lengths: list[int] = []
    while index < end:
        char = string[index]
        last_index = last_indices[char]

        substring_length = last_index - index + 1
        substring_lengths.append(substring_length)

        index = last_index + 1

    return substring_lengths


def main() -> None:
    """Main function"""
    string = "abacdddecn"
    # string = "aba"

    print(cut_string(string))


if __name__ == '__main__':
    main()
