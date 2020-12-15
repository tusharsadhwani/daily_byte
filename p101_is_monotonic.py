"""
Given an array nums, return whether or not its values are monotonically
increasing or monotonically decreasing.

Note: An array is monotonically increasing if for all values i <= j,
nums[i] <= nums[j]. Similarly an array is monotonically decreasing if
for all values i <= j, nums[i] >= nums[j].

Ex: Given the following array nums...

nums = [1, 2, 3, 4, 4, 5], return true.

Ex: Given the following array nums...

nums = [7, 6, 3], return true.

Ex: Given the following array nums...

nums = [8, 4, 6], return false.
"""
from typing import List


def is_monotonic(nums: List[int]) -> bool:
    """Returns if an array is monotonically increasing or decreasing"""
    if all(nums[n-1] >= nums[n] for n in range(1, len(nums))):
        return True

    if all(nums[n-1] <= nums[n] for n in range(1, len(nums))):
        return True

    return False


def main() -> None:
    """Main function"""
    nums = [1, 2, 3, 4, 4, 5]
    # nums = [7, 6, 3]
    # nums = [8, 4, 6]

    print(is_monotonic(nums))


if __name__ == "__main__":
    main()
