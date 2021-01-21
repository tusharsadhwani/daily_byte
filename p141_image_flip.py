"""
Given an image represented as a 2D array of pixels, return the image rotation ninety degrees.

Ex: Given the following image...

image = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
], return the image such that it's been modified as follows...
[
    [16, 13, 10],
    [17, 14, 11],
    [18, 15, 12]
]
"""
from utils.grid import rotate_clockwise


def main() -> None:
    """Main function"""
    image = [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ]
    flipped_image = rotate_clockwise(image)
    for row in flipped_image:
        print(row)


if __name__ == "__main__":
    main()
