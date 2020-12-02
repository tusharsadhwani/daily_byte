"""
Given a 2D array of integers with ones representing land and zeroes
representing water, return the number of islands in the grid.

Note: an island is one or more ones surrounded by water connected either
vertically or horizontally. Ex: Given the following grid...

11000
11010
11001
return 3.
Ex: Given the following grid...

00100
00010
00001
00001
00010
return 4.
"""

from typing import List
from pprint import pprint


def flood_island(grid: List[str], row: int, col: int, visited: List[List[bool]]) -> None:
    """Recursively floods the island to mark visited cells as True"""
    visited[row][col] = True

    rows, cols = len(grid), len(grid[0])

    for i, j in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        new_row, new_col = row+i, col+j
        if new_row < 0 or new_row >= rows:
            continue
        if new_col < 0 or new_col >= cols:
            continue

        if visited[new_row][new_col]:
            continue

        if grid[new_row][new_col] == '1':
            flood_island(grid, new_row, new_col, visited)


def count_islands(grid: List[str]) -> int:
    """Count the number of islands in the grid"""
    rows = len(grid)
    cols = len(grid[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    island_count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and not visited[i][j]:
                island_count += 1
                flood_island(grid, i, j, visited)

    return island_count


def main() -> None:
    """Main function"""

    grid = [
        '11000',
        '11010',
        '11001',
    ]
    # grid = [
    #     '00100',
    #     '00010',
    #     '00001',
    #     '00001',
    #     '00010',
    # ]

    count = count_islands(grid)
    print(count)


if __name__ == "__main__":
    main()
