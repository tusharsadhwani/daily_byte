"""
Given two strings s and t, return the minimum number of operations
needed to convert s into t where a single operation consists of
inserting a character, deleting a character, or replacing a character.

Ex: Given the following strings s and t...

s = "cat", t = "bat", return 1.

Ex: Given the following strings s and t...

s = "beach", t = "batch", return 2.
Delete the 'e' in "beach" and add a 't' to the resulting "bach".
"""


def levenshtein_distance(string1: str, string2: str) -> int:
    """Recursively calculates levenshtein distance of two strings"""
    # NOTE: can be made much faster,
    # refer https://www.python-course.eu/levenshtein_distance.php
    if string1 == "":
        return len(string2)
    if string2 == "":
        return len(string1)
    if string1[-1] == string2[-1]:
        cost = 0
    else:
        cost = 1

    res = min([levenshtein_distance(string1[:-1], string2) + 1,
               levenshtein_distance(string1, string2[:-1]) + 1,
               levenshtein_distance(string1[:-1], string2[:-1]) + cost])

    return res


def main() -> None:
    """Main function"""
    string1, string2 = "cat", "bat"
    # string1, string2 = "beach", "batch"

    print(levenshtein_distance(string1, string2))


if __name__ == "__main__":
    main()
