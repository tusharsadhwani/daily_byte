"""
Given an array of integers, nums, each element in the array either
appears once or twice. Return a list containing all the numbers that
appear twice.
Note: Each element in nums is between one and nums.length (inclusive).

Ex: Given the following array nums...

nums = [2, 3, 1, 5, 5], return [5].

Ex: Given the following array nums...

nums = [1, 2, 3], return [].

Ex: Given the following array nums...

nums = [7, 2, 2, 3, 3, 4, 4], return [2, 3, 4].
"""
from typing import List


def find_duplicates(nums: List[int]) -> List[int]:
    """Returns duplicates in nums"""
    duplicates = []

    for num in nums:
        num = abs(num)
        index = num - 1
        if nums[index] < 0:
            duplicates.append(num)

        nums[index] = -nums[index]

    return duplicates


def main() -> None:
    """Main function"""
    nums = [2, 3, 1, 5, 5]
    # nums = [1, 2, 3]
    # nums = [7, 2, 2, 3, 3, 4, 4]

    print(find_duplicates(nums))


if __name__ == "__main__":
    main()
