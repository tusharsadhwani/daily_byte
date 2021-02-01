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
    new_intervals: list[list[int]] = []

    for interval in intervals:
        for index, new_interval in enumerate(new_intervals):
            if ((interval[1] >= new_interval[0] and interval[0] <= new_interval[1]) or
                    (new_interval[1] >= interval[0] and new_interval[0] <= interval[1])):
                new_intervals[index] = [
                    min(interval[0], new_interval[0]),
                    max(interval[1], new_interval[1]),
                ]
                break
        else:
            new_intervals.append(interval)

    return new_intervals


def main() -> None:
    """Main function"""
    intervals = [[1, 3], [1, 8]]
    # intervals = [[1, 2], [2, 6], [7, 10]]

    print(combine_times(intervals))


if __name__ == '__main__':
    main()
