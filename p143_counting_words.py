"""
Given a list of words, return the top k frequently occurring words.

Note: If two words occur with the same frequency, then the
alphabetically smaller word should come first.

Ex: Given the following words and value k…

words = ["the", "daily", "byte", "byte"], k = 1, return ["byte"].

Ex: Given the following words and value k…

words = ["coding", "is", "fun", "code", "coding", "fun"], k = 2,
return ["coding", "fun"].
"""

import collections
from typing import Counter


def main() -> None:
    """Main function"""
    words = ["the", "daily", "byte", "byte"]
    count = 1
    # words = ["coding", "is", "fun", "code", "coding", "fun"]
    # count = 2

    counter: Counter[str] = collections.Counter(words)
    words = sorted(set(words), key=lambda word: (-counter[word], word))

    print(words[:count])


if __name__ == '__main__':
    main()
