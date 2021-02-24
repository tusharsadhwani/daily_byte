"""
Given a sorted integer array nums and a target, search for the target
with in the array. If the targets exists within the array, return its
index. If it does not exist within the array, return -1.

Ex: Given the following nums and target...

nums = [-5, -3, 0, 3, 8, 12, 40], target = 8, return 4.

Ex: Given the following nums and target...

nums = [1, 2, 3, 6, 8], target = 10, return -1.
"""
from typing import Optional


def binary_search(nums: list[int], target: int) -> int:
    """Binary search, returns index of target, or -1"""
    begin = 0
    end = len(nums) - 1

    while begin <= end:
        mid = (begin + end) // 2
        value = nums[mid]

        if value == target:
            return mid

        if value < target:
            begin = mid + 1
        else:
            end = mid - 1

    return -1


def main() -> None:
    """Main function"""
    nums = [-5, -3, 0, 3, 8, 12, 40]
    target = 8
    # nums = [1, 2, 3, 6, 8]
    # target = 10

    print(binary_search(nums, target))


if __name__ == '__main__':
    main()
