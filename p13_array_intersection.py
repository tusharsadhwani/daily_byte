"""
Given two integer arrays, return their intersection.
Note: the intersection is the set of elements that are common to both
arrays.

Ex: Given the following arrays...

nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []
"""

from typing import List


def array_intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """Obtains the intersection of two arrays and returns it"""
    nums = set(nums1)
    intersection = set()
    for num in nums2:
        if num in nums:
            intersection.add(num)

    return list(intersection)


def main():
    """Main Function"""
    print(array_intersection([2, 4, 4, 2], [2, 4]))
    print(array_intersection([1, 2, 3, 3], [3, 3]))
    print(array_intersection([2, 4, 6, 8], [1, 3, 5, 7]))


if __name__ == "__main__":
    main()
