"""
Given an integer array that is sorted in ascending order and a value
target, return two unique indices (one based) such that the values at
those indices sums to the given target.

Note: If no two such indices exist, return null.

Ex: Given the following nums and target...

nums = [1, 2, 5, 7, 9], target = 10, return [1, 5].

Ex: Given the following nums and target...

nums = [1, 3, 8], target = 13, return null.
"""
from typing import Optional


def binary_search(
        array: list[int],
        value: int,
        start: Optional[int] = None,
        end: Optional[int] = None) -> int:
    """Returns the index of a number in an array, or -1"""
    if start is None or end is None:
        start, end = 0, len(array)-1

    if start > end:
        return -1

    mid = (start + end) // 2

    if array[mid] == value:
        return mid

    if array[mid] < value:
        return binary_search(array, value, mid+1, end)

    return binary_search(array, value, start, mid-1)


def find_pair(nums: list[int], target: int) -> Optional[tuple[int, int]]:
    """Returns two numbers from nums whose sum equals target, otherwise None"""
    for index, num in enumerate(nums):
        complement = target-num
        complement_index = binary_search(nums, complement)
        if complement_index >= 0:
            return (index+1, complement_index+1)

    return None


def main() -> None:
    """Main function"""
    nums = [1, 2, 5, 7, 9]
    target = 10
    # nums = [1, 3, 8]
    # target = 13

    print(find_pair(nums, target))


if __name__ == '__main__':
    main()
