"""
Given two strings, passage and text return whether or not the characters
in text can be used to form the given passage.

Note: Each character in text may only be used once and passage and text
will only contain lowercase alphabetical characters.

Ex: Given the following passage and text...

passage = "bat", text = "cat", return false.

Ex: Given the following passage and text...

passage = "dog" text = "didnotgo", return true.
"""


from collections import Counter


def character_scramble(passage: str, text: str) -> bool:
    """Returns if given passage can be formed using given text"""
    passage_counter = Counter(passage)
    text_counter = Counter(text)

    for char, count in passage_counter.items():
        if text_counter[char] < count:
            return False

    return True


def main() -> None:
    """Main function"""
    passage, text = "bat", "cat"
    # passage, text = "dog", "didnotgo"

    print(character_scramble(passage, text))


if __name__ == "__main__":
    main()
