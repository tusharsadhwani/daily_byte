"""
Given a 2D matrix nums, return the matrix transposed.
Note: The transpose of a matrix is an operation that flips each value in
the matrix across its main diagonal.

Ex: Given the following matrix nums...

nums = [
  [1, 2],
  [3, 4]
]
return a matrix that looks as follows...
[
  [1,3],
  [2,4]
]
"""
from utils.grid import transpose


def main() -> None:
    """Main function"""
    nums = [
        [1, 2],
        [3, 4]
    ]

    print(transpose(nums))


if __name__ == "__main__":
    main()
