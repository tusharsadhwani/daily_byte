"""
Given an array of unsorted integers, return the length of its longest
increasing subsequence.

Note: You may assume the array will only contain positive numbers.

Ex: Given the following array nums...

nums = [1, 9, 7, 4, 7, 13], return 4.
The longest increasing subsequence is 1, 4, 7, 13.
"""
# NOTE: so, i thought this problem is asking for a continuous
# subsequence, turns out, it wasn't.


def find_longest_increasing_subsequence(nums: list[int]) -> list[int]:
    """Finds the longest continuous increasing subsequence"""
    max_subsequence_start = 0
    max_subsequence_length = 0

    start_index = 0
    for index, num in enumerate(nums):
        prev_num = nums[index-1]
        if num < prev_num:
            # sequence broken
            subsequence_length = index - start_index
            if subsequence_length > max_subsequence_length:
                max_subsequence_start = start_index
                max_subsequence_length = subsequence_length

            start_index = index

    max_subsequence_end = max_subsequence_start + max_subsequence_length
    subsequence = nums[max_subsequence_start:max_subsequence_end]
    return subsequence


def main() -> None:
    """Main function"""
    nums = [1, 9, 7, 4, 7, 13]

    sequence = find_longest_increasing_subsequence(nums)
    print(sequence)


if __name__ == "__main__":
    main()
