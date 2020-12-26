"""
Given an array of integers, nums, and a value k, return the kth largest
element.

Ex: Given the following array nums...

[1, 2, 3], k = 1, return 3.

Ex: Given the following array nums...

[9, 2, 1, 7, 3, 2], k = 5, return 2.
"""


def main() -> None:
    """Main function"""
    array = [1, 2, 3]
    index = 1
    # array = [9, 2, 1, 7, 3, 2]
    # index = 5

    print(sorted(array)[-index])


if __name__ == "__main__":
    main()
