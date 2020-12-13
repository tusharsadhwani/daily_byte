"""
Given two strings representing sentences, return the words that are not
common to both strings (i.e. the words that only appear in one of the
sentences). You may assume that each sentence is a sequence of words
(without punctuation) correctly separated using space characters.

Ex: given the following strings...

sentence1 = "the quick",
sentence2 = "brown fox",
return ["the", "quick", "brown", "fox"]

sentence1 = "the tortoise beat the haire",
sentence2 = "the tortoise lost to the haire",
return ["beat", "to", "lost"]

sentence1 = "copper coffee pot",
sentence2 = "hot coffee pot",
return ["copper", "hot"]
"""
from typing import List


def find_uncommon_words(sentence1: str, sentence2: str) -> List[str]:
    """Hello"""
    words1 = sentence1.split()
    words = set(words1)
    words.update()

    removed_words = set()

    for word in sentence2.split():
        if word in words:
            words.remove(word)
            removed_words.add(word)
        elif word not in removed_words:
            words.add(word)

    return list(words)


def main() -> None:
    """Main function"""
    sentence1 = input('> ')
    sentence2 = input('> ')

    uncommon_words = find_uncommon_words(sentence1, sentence2)
    print(uncommon_words)


if __name__ == "__main__":
    main()
