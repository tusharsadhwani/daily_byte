"""
Given an integer array nums and a value, val, remove all instances of
val in-place and return the length of the new array.

Note: It does not matter what values you leave in the array beyond the
array’s new length.

Ex: Given the following nums and val...

nums = [1, 2, 3], val = 2, return 2 (after your modifications your array
could look like [1, 3, 3]).
"""


def remove_value(nums: list[int], val: int) -> int:
    """Removes val from nums inplace, and returns new length"""
    offset = 0
    for index, num in enumerate(nums):
        nums[index - offset] = num

        if num == val:
            offset += 1

    new_length = len(nums) - offset
    return new_length


def main() -> None:
    """Main function"""
    nums = [1, 2, 3]
    val = 2

    nums = [1, 2, 3, 2, 7, 8, 2, 2, 2, 4, 5, 2, 9, 2, 1, 2]

    new_length = remove_value(nums, val)
    print(nums)
    print(nums[:new_length])


if __name__ == '__main__':
    main()
