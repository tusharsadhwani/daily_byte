"""
Given an integer array nums, return an array where each element i
represents the product of all values in nums excluding nums[i].
Note: You may assume the product of all numbers within nums can safely
fit within an integer range.

Ex: Given the following array nums...

nums = [1, 2, 3], return [6,3,2].
6 = 3 * 2 (we exclude 1)
3 = 3 * 1 (we exclude 2)
2 = 2 * 1 (we exclude 3)
"""
from functools import reduce


def main() -> None:
    """Main function"""
    nums = [1, 2, 3]

    product = reduce(lambda x, y: x*y, nums)
    print([product // num for num in nums])


if __name__ == "__main__":
    main()
