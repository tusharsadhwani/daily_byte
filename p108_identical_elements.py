"""
Given an array, nums, and an integer k, return whether or not two unique
indices exist such that nums[i] = nums[j] and the two indices i and j
are at most k elements apart.

Ex: Given the following array nums and value k...

nums = [1, 2, 1], k = 1, return false.

Ex: Given the following array nums and value k...

nums = [2, 3, 2], k = 2, return true.
"""


def identical_elements(nums: list[int], max_dist: int) -> bool:
    """Returns whether or not an identical element exists in the list at
    max `max_dist` elements apart"""
    size = len(nums)
    for i in range(size):
        if nums[i] in nums[i+1:i+max_dist+1]:
            return True

    return False


def main() -> None:
    """Main function"""
    nums = [1, 2, 1]
    max_dist = 1
    # nums = [2, 3, 2]
    # max_dist = 2

    print(identical_elements(nums, max_dist))


if __name__ == "__main__":
    main()
