"""
Given an array nums, return the third largest (distinct) value.
Note: If the third largest number does not exist, return the largest
value.

Ex: Given the following array nums...

nums = [1, 4, 2, 3, 5], return 3.

Ex: Given the following array nums...

nums = [2, 3, 3, 5], return 2.

Ex: Given the following array nums...

nums = [9, 5], return 9.
"""


def main() -> None:
    """Main function"""
    nums = [1, 4, 2, 3, 5]
    # nums = [2, 3, 3, 5]
    # nums = [9, 5]

    nums = list(sorted(set(nums)))

    if len(nums) >= 3:
        print(nums[-3])
    else:
        print(nums[-1])


if __name__ == "__main__":
    main()
