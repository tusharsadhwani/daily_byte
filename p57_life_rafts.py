"""
A ship is about to set sail and you are responsible for its safety
precautions. More specifically, you are responsible for determining how
many life rafts to carry onboard. You are given a list of all the
passengers’ weights and are informed that a single life raft has a
maximum capacity of limit and can hold at most two people.

Return the minimum number of life rafts you must take onboard to ensure
the safety of all your passengers.

Note: You may assume that a the maximum weight of any individual is at
most limit.

Ex: Given the following passenger weights and limit…

weights = [1, 3, 5, 2] and limit = 5, return 3
weights = [1, 2] and limit = 3, return 1
weights = [4, 2, 3, 3] and limit = 5 return 3
"""
from typing import List


def find_largest_value_below(
        limit: int,
        array: List[int],
        start: int,
        end: int) -> int:
    """Uses binary search to find index of largest value below limit"""
    if len(array) <= start or array[start] > limit:
        return -1

    mid = (start + end) // 2
    if array[mid] == array[start] or array[mid] == array[end]:
        return mid

    if array[mid] > limit:
        return find_largest_value_below(limit, array, start, mid-1)

    return find_largest_value_below(limit, array, mid, end)


def minimum_containers(weights: List[int], limit: int) -> int:
    """Find minimum number of containers required to fit all weights"""
    weights.sort()

    containers = 0
    while weights:
        if len(weights) == 1:
            containers += 1
            return containers

        last_weight = weights.pop()

        last_index = len(weights) - 1
        limit_left = limit - last_weight
        while True:
            index = find_largest_value_below(
                limit_left, weights, 0, last_index
            )
            if index == -1:
                containers += 1
                break

            value = weights.pop(index)
            limit_left -= value

    return containers


def main() -> None:
    """Main function"""
    weights = [1, 3, 5, 2]
    limit = 5

    # weights = [1, 2]
    # limit = 3

    # weights = [4, 2, 3, 3]
    # limit = 5

    print(minimum_containers(weights, limit))


if __name__ == "__main__":
    main()
