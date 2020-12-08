"""Get pair-wise values from a list"""
from typing import Generator, List, Tuple, TypeVar

T = TypeVar('T')

Pair = Tuple[T, T]


def pairwise(array: List[T]) -> Generator[Pair[T], None, None]:
    """Get pair-wise values from a list"""
    prev_val = array[0]
    for value in array[1:]:
        yield prev_val, value
        prev_val = value
