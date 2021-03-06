"""Grid functions"""
from typing import Sequence, TypeVar

T = TypeVar('T')


def _flood(
        grid: Sequence[Sequence[T]],
        value: T,
        row: int,
        col: int,
        visited: list[list[bool]]) -> None:
    """Recursively floods grid to mark visited cells as True"""
    visited[row][col] = True

    rows, cols = len(grid), len(grid[0])

    for i, j in (-1, 0), (0, -1), (0, 1), (1, 0):
        new_row, new_col = row+i, col+j
        if new_row < 0 or new_row >= rows:
            continue
        if new_col < 0 or new_col >= cols:
            continue

        if visited[new_row][new_col]:
            continue

        if grid[new_row][new_col] == value:
            _flood(grid, value, new_row, new_col, visited)


def count_entities(grid: Sequence[Sequence[T]], value: T) -> int:
    """Count the number of entities in the grid matching given value"""
    rows = len(grid)
    cols = len(grid[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == value and not visited[i][j]:
                count += 1
                _flood(grid, value, i, j, visited)

    return count


def transpose(grid: Sequence[Sequence[T]]) -> Sequence[Sequence[T]]:
    """Returns a matrix transpose"""
    rows = len(grid)
    cols = len(grid[0])
    return [[grid[j][i] for j in range(cols)] for i in range(rows)]


def rotate_clockwise(grid: Sequence[Sequence[T]]) -> Sequence[Sequence[T]]:
    """Returns a matrix rotated 90 degrees clockwise"""
    rows = len(grid)
    cols = len(grid[0])
    return [[grid[cols-1-j][i] for j in range(cols)] for i in range(rows)]
