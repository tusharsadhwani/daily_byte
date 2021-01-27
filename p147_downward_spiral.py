"""
Given a 2D matrix, return a list containing all of its element in spiral
order.

Ex: Given the following matrix...

matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
], return [1, 2, 3, 6, 9, 8, 7, 4, 5].
"""


def downward_spiral(grid: list[list[int]]) -> list[int]:
    """Returns the numbers iterated in spiral form"""
    nums: list[int] = []

    size = len(grid)
    for index in range(size//2 + 1):
        if index == size-1 - index:
            nums.append(grid[index][index])
            break

        i = j = index

        while j < size-index:
            nums.append(grid[i][j])
            j += 1
        j -= 1
        i += 1

        while i < size-index:
            nums.append(grid[i][j])
            i += 1
        i -= 1
        j -= 1

        while j >= index:
            nums.append(grid[i][j])
            j -= 1
        j += 1
        i -= 1

        while i >= index+1:
            nums.append(grid[i][j])
            i -= 1

    return nums


def main() -> None:
    """Main function"""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    # matrix = [
    #     [1, 2, 3, 4, 5, 6],
    #     [7, 8, 9, 10, 11, 12],
    #     [13, 14, 15, 16, 17, 18],
    #     [19, 20, 21, 22, 23, 24],
    #     [25, 26, 27, 28, 29, 30],
    #     [31, 32, 33, 34, 35, 36]
    # ]

    print(downward_spiral(matrix))


if __name__ == '__main__':
    main()
