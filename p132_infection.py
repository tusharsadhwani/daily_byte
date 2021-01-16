"""
Given a 2D array each cells can have one of three values. Zero
represents an empty cell, one represents a healthy person, and two
represents a sick person. Each minute that passes, any healthy person
who is adjacent to a sick person becomes sick. Return the total number
of minutes that must elapse until every person is sick.

Note: If it is not possible for each person to become sick, return -1.

Ex: Given the following 2D array grid…

grid = [
    [1, 1, 1],
    [1, 1, 0],
    [0, 1, 2]
], return 4.

[2, 1] becomes sick at minute 1.
[1, 1] becomes sick at minute 2.
[1, 0] and [0, 1] become sick at minute 3.
[0, 0] and [0, 2] become sick at minute 4.

Ex: Given the following 2D array grid…

grid = [
    [1, 1, 1],
    [0, 0, 0],
    [2, 0, 1]
], return -1.
"""


def infect(grid: list[list[int]]) -> None:
    """Runs the infection simulation for 1 minute"""
    rows = len(grid)
    cols = len(grid[0])
    infected_indices = [(i, j) for i in range(rows) for j in range(cols)
                        if grid[i][j] == 2]

    new_infections = list[tuple[int, int]]()
    for row, col in infected_indices:
        for i, j in ((0, -1), (-1, 0), (1, 0), (0, 1)):
            new_row = row + i
            new_col = col + j

            if new_row < 0 or new_row >= rows:
                continue
            if new_col < 0 or new_col >= cols:
                continue

            neighbour = grid[new_row][new_col]
            if neighbour == 1:
                new_infections.append((new_row, new_col))

    for i, j in new_infections:
        grid[i][j] = 2


def main() -> None:
    """Main function"""
    grid = [
        [1, 1, 1],
        [1, 1, 0],
        [0, 1, 2]
    ]

    minutes = 0
    while 1 in (num for row in grid for num in row):
        infect(grid)
        minutes += 1

    print(minutes)


if __name__ == "__main__":
    main()
