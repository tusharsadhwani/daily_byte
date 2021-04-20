"""
Given a list of interval object, merge all overlapping intervals and
return the result.

Note: an interval object is a simple object that contains a start time
and end time and can be constructed by passing a starting and ending
time to the constructor.

Ex: Given the following intervals...

intervals = [[1, 3], [1, 8]], return a list of interval objects
containing [[1, 8]].

Ex: Given the following intervals...

intervals = [[1, 2], [2, 6], [7 ,10]], return a list of interval objects
containing [[1, 6], [7, 10]].
"""


def combine_times(intervals: list[list[int]]) -> list[list[int]]:
    """Combines overlapping intervals"""
    intervals.sort()

    new_intervals: list[list[int]] = []

    prev_interval = intervals[0]
    for index in range(1, len(intervals)):
        interval = intervals[index]

        if interval[0] > prev_interval[1]:
            new_intervals.append(prev_interval)
            prev_interval = interval
        else:
            prev_interval = [
                min(prev_interval[0], interval[0]),
                max(prev_interval[1], interval[1]),
            ]

    new_intervals.append(prev_interval)

    return new_intervals


def main() -> None:
    """Main function"""
    intervals = [[1, 3], [1, 8]]
    # intervals = [[1, 2], [2, 6], [7, 10]]

    print(combine_times(intervals))


if __name__ == '__main__':
    main()
