"""
Given a string representing your stones and another string representing
a list of jewels, return the number of stones that you have that are
also jewels.

Ex: Given the following jewels and stones...

jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0
"""


def count_matching_characters(jewels: str, stones: str) -> int:
    """Counts the number of characters common between two strings"""
    # Assuming from the examples in the problem, all jewels are unique
    jewel_set = set(jewels)
    common_count = 0
    for stone in stones:
        if stone in jewel_set:
            common_count += 1
    return common_count


def main():
    """Main function"""
    jewels = input("Enter jewels: ")
    stones = input("Enter stones: ")

    common_count = count_matching_characters(jewels, stones)
    print(common_count)


if __name__ == "__main__":
    main()
