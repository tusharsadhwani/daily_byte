"""
Given two arrays of numbers, where the first array is a subset of the
second array, return an array containing all the next greater elements
for each element in the first array, in the second array. If there is no
greater element for any element, output -1 for that number.

Ex: Given the following arrays…

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2],
-> return [-1, 3, -1]
because no element in nums2 is greater than 4, 3 is the first number in
nums2 greater than 1, and no element in nums2 is greater than 2.

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
-> return [3, -1]
because 3 is the first greater element that occurs in nums2 after 2 and
no element is greater than 4.
"""

# I personally found the wording for this horrible, so I'll try my best
# to rephrase:
# For every element N in nums1, return the first number that is bigger
# than N in and occurs after N in nums2. If no such number exists,
# return -1.

from typing import Dict, List


def nearest_greater_to_the_right(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    For every N in nums1, finds the nearest greater number in nums2 to
    the right of N.

    For more on the algorithm refer:
    https://www.geeksforgeeks.org/next-greater-element/
    """
    nums2_indices: Dict[int, int] = dict()
    for index, num in enumerate(nums2):
        nums2_indices[num] = index

    ngr_reverse_list: List[int] = []
    ngr_stack: List[int] = []

    for num in reversed(nums2):
        while len(ngr_stack) > 0 and ngr_stack[-1] < num:
            ngr_stack.pop()

        if len(ngr_stack) == 0:
            ngr_reverse_list.append(-1)
        else:
            ngr_reverse_list.append(ngr_stack[-1])

        ngr_stack.append(num)

    answer: List[int] = []
    for num in nums1:
        index = nums2_indices[num]
        reverse_index = -1 - index
        answer.append(ngr_reverse_list[reverse_index])

    return answer

    # Alternative:
    # return [ngr_reverse_list[-1 - nums2_indices[num]] for num in nums1]


def main() -> None:
    """Main function"""
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    # nums1 = [2, 4]
    # nums2 = [1, 2, 3, 4]

    print(nearest_greater_to_the_right(nums1, nums2))


if __name__ == "__main__":
    main()
