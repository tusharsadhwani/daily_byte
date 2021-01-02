"""
Given a list of points, return the k closest points to the origin
(0, 0).

Ex: Given the following points and value of k...

points = [[1,1],[-2,-2]], k = 1, return [[1, 1]].
"""


def main() -> None:
    """Main function"""
    points = [[1, 1], [-2, -2]]
    count = 1

    print(sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:count])


if __name__ == "__main__":
    main()
