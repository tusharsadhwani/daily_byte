"""
Given a 2D matrix that represents a gold mine, where each cell’s value
represents an amount of gold, return the maximum amount of gold you can
collect given the following rules:

1. You may start and stop collecting gold from any position
2. You can never visit a cell that contains 0 gold
3. You cannot visit the same cell more than once

From current cell, you may walk one cell to the left, right, up, or down

Ex: Given the following gold mine…

goldMine = [
    [0, 2, 0],
    [8, 6, 3],
    [0, 9, 0]
],
return 23 (start at 9 and then move to 6 and 8 respectively)
"""
from __future__ import annotations
from typing import Generator, List, NamedTuple, Optional, Set


class TrailItem(NamedTuple):
    """Represents a cell in a gold trail"""
    row_index: int
    col_index: int
    value: int


class TrailSet:
    """Holds a set of all cells in a gold trail"""

    def __init__(self, trail: Optional[Set[TrailItem]] = None) -> None:
        self._trail: Set[TrailItem] = trail or set()

    def __repr__(self) -> str:
        return f'TrailSet{[item.value for item in self._trail]}'

    def __iter__(self) -> Generator[TrailItem, None, None]:
        for item in self._trail:
            yield item

    def add(self, cell: TrailItem) -> None:
        """Adds cell to trail set"""
        self._trail.add(cell)

    def copy(self) -> TrailSet:
        """Creates copy of trail set"""
        new_trail = TrailSet(self._trail)
        return new_trail


def flood(
        gold_mine: List[List[int]],
        row_index: int,
        col_index: int,
        visited: List[List[bool]],
        trail: Optional[TrailSet] = None) -> Optional[TrailSet]:
    """Finds and returns the gold trail associated with given index"""
    cell_value = gold_mine[row_index][col_index]
    if cell_value == 0 or visited[row_index][col_index]:
        return None

    if trail is None:
        trail = TrailSet()

    visited[row_index][col_index] = True
    cell = TrailItem(row_index, col_index, cell_value)
    trail.add(cell)

    rows, cols = len(gold_mine), len(gold_mine[0])

    for i, j in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        new_row_index, new_col_index = row_index+i, col_index+j
        if (new_row_index < 0 or new_row_index >= rows or
                new_col_index < 0 or new_col_index >= cols):
            continue

        if visited[new_row_index][new_col_index]:
            continue

        cell_value = gold_mine[new_row_index][new_col_index]
        if cell_value <= 0:
            continue

        flood(gold_mine, new_row_index, new_col_index, visited, trail)

    return trail


def find_max_gold_trail(gold_mine: List[List[int]]) -> int:
    """Finds the gold trail with maximum value and returns its sum"""

    visited = [[False for cell in row] for row in gold_mine]
    trail_sets: Set[TrailSet] = set()

    for row_index, row in enumerate(gold_mine):
        for col_index, _ in enumerate(row):
            trail_set = flood(gold_mine, row_index, col_index, visited)
            if trail_set is None:
                continue

            trail_sets.add(trail_set)

    for trail_set in trail_sets:
        # TODO: find edges in trail set
        #       (a trail is a cell with only 1 valid neighbour)
        # TODO: for each edge, find all possible trails via the same
        #       floodfill (floodfill cells which are marked visited, and
        #       add it to possible trails when you hit an edge)
        pass

    return -1


def main() -> None:
    """Main function"""
    gold_mine = [
        [0, 2, 0, 0, 0, 2],
        [8, 6, 3, 0, 0, 2],
        [0, 9, 0, 0, 0, 2]
    ]

    print(find_max_gold_trail(gold_mine))


if __name__ == "__main__":
    main()
