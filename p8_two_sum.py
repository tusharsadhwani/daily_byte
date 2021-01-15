"""
Given an array of integers, return whether or not two numbers sum to a
given target, k. You may not sum a number with itself.

Ex: Given the following...

[1, 3, 8, 2], k = 10, return True (as 8 + 2 == 10)
[3, 9, 13, 7], k = 8, return False
[4, 2, 6, 5, 2], k = 4, return True (as 2 + 2 == 4)
"""


def check_two_sum(array: list[int], num: int) -> bool:
    """Returns if any two numbers in array add to num or not"""

    # not using array.sort() as we don't want to modify the original array
    sorted_array = sorted(array)

    low, high = 0, len(sorted_array) - 1
    while low < high:
        total = sorted_array[low] + sorted_array[high]

        if total == num:
            return True

        # As the array is sorted, any pair k and (num-k)
        # can simply be found by moving two pointers.
        #
        # No numbers will be missed by this method, because any number
        # bigger than (num-k) will be to the right of it, hence pushing
        # the second arrow towards (num-k).
        if total < num:
            low += 1
        else:
            high -= 1

    return False


def main() -> None:
    """Main function"""
    print(check_two_sum([1, 3, 8, 2], 10))
    print(check_two_sum([3, 9, 13, 7], 8))
    print(check_two_sum([4, 2, 6, 5, 2], 4))


if __name__ == "__main__":
    main()
