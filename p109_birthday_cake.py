"""
You are at a birthday party and are asked to distribute cake to your
guests. Each guess is only satisfied if the size of the piece of cake
they’re given, matches their appetite (i.e. is greater than or equal to
their appetite). Given two arrays, appetite and cake where the
ithelement of appetite represents the ith guest’s appetite, and the
elements of cake represents the sizes of cake you have to distribute,
return the maximum number of guests that you can satisfy.

Ex: Given the following arrays appetite and cake...

appetite = [1, 2, 3], cake = [1, 2, 3], return 3.

Ex: Given the following arrays appetite and cake...

appetite = [3, 4, 5], cake = [2], return 0.
"""

from typing import List


def max_guests(appetite: List[int], cake: List[int]) -> int:
    """Returns maximum number of guests you can satisfy"""
    guest_count = 0

    appetite_index = len(appetite) - 1
    cake_index = len(cake) - 1

    while appetite_index >= 0 and cake_index >= 0:
        appetite_size = appetite[appetite_index]
        cake_size = cake[cake_index]

        if cake_size >= appetite_size:
            # cake is fed
            cake_index -= 1
            guest_count += 1

        # else, the person is skipped
        appetite_index -= 1

    return guest_count


def main() -> None:
    """Main function"""
    appetite = [1, 2, 3]
    cake = [1, 2, 3]
    # appetite = [3, 4, 5]
    # cake = [2]

    print(max_guests(appetite, cake))


if __name__ == "__main__":
    main()
