"""
Given an integer array, nums, return the total number of “partners” in
the array.

Note: Two numbers in our array are partners if they reside at different
indices and both contain the same value.

Ex: Given the following array nums...

nums = [5, 5, 3, 1, 1, 3, 3], return 5.
5 (index 0) and 5 (index 1) are partners.
1 (index 3) and 1 (index 4) are partners.
3 (index 2) and 3 (index 5) are partners.
3 (index 2) and 3 (index 6) are partners.
3 (index 5) and 3 (index 6) are partners.
"""
from collections import Counter


def count_partners(nums: list[int]) -> int:
    """Returns the count of all possible partners"""
    counter = Counter(nums)

    partner_count = 0
    for count in counter.values():
        partner_count += count * (count-1) // 2

    return partner_count


def main() -> None:
    """Main function"""
    nums = [5, 5, 3, 1, 1, 3, 3]

    print(count_partners(nums))


if __name__ == "__main__":
    main()
