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
from utils.grid import count_entities


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

    count = count_entities(grid, '1')
    print(count)


if __name__ == "__main__":
    main()
