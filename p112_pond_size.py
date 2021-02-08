"""
You are given two-dimensional matrix that represents a plot of land.
Within the matrix there exist two values: ones which represent land and
zeroes which represent water within a pond. Given that parts of a pond
can be connected both horizontally and vertically (but not diagonally),
return the largest pond size.
Note: You may assume that each zero within a given pond contributes a
value of one to the total size of the pond.

Ex: Given the following plot of land...

land = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
],
return 1.

Ex: Given the following plot of land...

land = [
    [1,0,1],
    [0,0,0],
    [1,0,1]
],
return 5.
"""
from typing import Optional


def get_pond_size(
        grid: list[list[int]],
        row: int,
        col: int,
        visited: list[list[bool]],
        pond_cells: Optional[list[tuple[int, int]]] = None) -> int:
    """Recursively floods the pond to count pond cells"""
    if pond_cells is None:
        pond_cells = []

    visited[row][col] = True
    pond_cells.append((row, col))

    rows, cols = len(grid), len(grid[0])

    for i, j in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        new_row, new_col = row+i, col+j
        if new_row < 0 or new_row >= rows:
            continue
        if new_col < 0 or new_col >= cols:
            continue

        if visited[new_row][new_col]:
            continue

        if grid[new_row][new_col] == 0:
            get_pond_size(grid, new_row, new_col, visited, pond_cells)

    return len(pond_cells)


def get_max_pond_size(grid: list[list[int]]) -> int:
    """Finds and returns size of largest pond in the grid"""
    rows = len(grid)
    cols = len(grid[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]

    max_pond_size = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 and not visited[i][j]:
                # new pond found
                pond_size = get_pond_size(grid, i, j, visited)
                max_pond_size = max(max_pond_size, pond_size)

    return max_pond_size


def main() -> None:
    """Main function"""
    grid = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]
    # grid = [
    #     [1, 0, 1],
    #     [0, 0, 0],
    #     [1, 0, 1],
    # ]

    print(get_max_pond_size(grid))


if __name__ == "__main__":
    main()
