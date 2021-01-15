"""
Given an array of numbers, move all zeroes in the array to the end while
maintaining the relative order of the other numbers.

Note: You must modify the array you’re given (i.e. you cannot create a
new array).

Ex: Given the following array nums...

nums = [3, 7, 0, 5, 0, 2]

rearrange nums to look like the following: [3, 7, 5, 2, 0, 0]
"""


def rearrange1(nums: list[int]) -> None:
    """Rearrange the zeroes at the end of list"""
    index = len(nums) - 1
    while index >= 0:
        num = nums[index]
        if num == 0:
            nums.pop(index)
            nums.append(0)

        index -= 1

    print(nums)


def rearrange2(nums: list[int]) -> None:
    """Rearrange the zeroes at the end of list"""
    zero_count = 0
    for index, num in enumerate(nums):
        while num == 0:
            nums.pop(index)
            zero_count += 1
            num = nums[index]

    nums.extend(0 for _ in range(zero_count))
    print(nums)


def main() -> None:
    """Main function"""
    nums = [3, 7, 0, 0, 5, 0, 2]

    rearrange1(nums.copy())
    rearrange2(nums.copy())


if __name__ == "__main__":
    main()
