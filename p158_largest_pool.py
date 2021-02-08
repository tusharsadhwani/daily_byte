"""
You are building a pool in your backyard and want to create the largest
pool possible. The largest pool is defined as the pool that holds the
most water. The workers you hired to dig the hole for your pool didn’t
do a great job and because of this the depths of the pool at different
areas are not equal. Given an integer array of non-negative integers
that represents a histogram of the different heights at each position of
the hole for your pool, return the largest pool you can create.

Ex: Given the following heights...

heights = [1, 4, 4, 8, 2], return 8.
You can build your largest pool (most water) between indices 1 and 3
(inclusive) for a water volume of 4 * 2 = 8.
"""
# So basically, each value in the histogram is an individual "hole",
# you're free to dig more but you can't add material on top. So the
# solution is to find the two long holes and maximize
# ((shorter height of the two) * distance)


def largest_pool_area_bruteforce(heights: list[int]) -> int:
    """Finds largest pool area"""
    max_area = 0
    for index1, height1 in enumerate(heights):
        for index2, height2 in enumerate(heights):
            area = min(height1, height2) * abs(index1 - index2)
            max_area = max(max_area, area)

    return max_area


def largest_pool_area(heights: list[int]) -> int:
    """Finds largest pool area"""
    start, end = 0, len(heights) - 1
    max_area = 0
    while start < end:
        height1 = heights[start]
        height2 = heights[end]
        min_height = min(height1, height2)
        area = (end - start) * min_height
        max_area = max(max_area, area)

        if height1 < height2:
            start += 1
        else:
            end -= 1

    return max_area


def main() -> None:
    """Main function"""
    heights = [1, 4, 4, 8, 2]

    print(largest_pool_area_bruteforce(heights))
    # better solution
    print(largest_pool_area(heights))


if __name__ == '__main__':
    main()
