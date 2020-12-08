"""Assorted binary searches"""

from typing import List


def binary_search_greater(
        array: List[int],
        limit: int,
        start: int,
        end: int) -> int:
    """Uses binary search to find index of smallest value above limit"""
    if limit > array[end]:
        return end + 1

    if end == start:
        return start

    mid = (start + end) // 2

    if array[mid] < limit:
        return binary_search_greater(array, limit, mid+1, end)

    return binary_search_greater(array, limit, start, mid)
