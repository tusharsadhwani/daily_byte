"""
Given a 2D array grid, where zeroes represent water and ones represent
land, return the size of the largest island.

Note: An island is one or more cells in grid containing a value of one
that may be connected vertically or horizontally. Each cell in an island
contributes a value of one to the current island’s size.

Ex: Given the following grid...

grid = [
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 1],
], return 4.
"""


from typing import Optional


def flood_island(
        grid: list[list[int]],
        row: int,
        col: int,
        visited: list[list[bool]],
        island_points: Optional[list[tuple[int, int]]] = None) -> int:
    """Recursively floods grid to find points on an island"""
    if island_points is None:
        island_points = []

    island_points.append((row, col))
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

        if grid[new_row][new_col] == 1:
            flood_island(grid, new_row, new_col, visited, island_points)

    return len(island_points)


def largest_island(grid: list[list[int]]) -> int:
    """Returns island with largest size"""
    rows = len(grid)
    cols = len(grid[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    max_island_size = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                island_size = flood_island(grid, i, j, visited)
                if island_size > max_island_size:
                    max_island_size = island_size

    return max_island_size


def main() -> None:
    """Main function"""

    grid = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1],
    ]
    print(largest_island(grid))


if __name__ == '__main__':
    main()
