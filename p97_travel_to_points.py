"""
Given N points on a Cartesian plane, return the minimum time required to
visit all points in the order that they’re given.

Note: You start at the first point and can move one unit vertically,
horizontally, or diagonally in a single second.

Ex: Given the following points...

points = [[0, 0], [1,1], [2,2]], return 2.
In one second we can travel from [0, 0] to [1, 1]
In another second we can travel from [1, 1,] to [2, 2]

Ex: Given the following points...

points = [[0, 1], [2, 3], [4, 0]], return 5.
"""
from typing import Tuple

from utils.pairwise import pairwise


Point = Tuple[int, int]


def distance(point_a: Point, point_b: Point) -> int:
    """Returns distance between two points"""
    x_a, y_a = point_a
    x_b, y_b = point_b

    return max(abs(x_a-x_b), abs(y_a-y_b))


def main() -> None:
    """Main function"""
    points = [(0, 0), (1, 1), (2, 2)]
    # points = [(0, 1), (2, 3), (4, 0)]

    total_distance = 0
    for point_a, point_b in pairwise(points):
        total_distance += distance(point_a, point_b)

    print(total_distance)


if __name__ == "__main__":
    main()
