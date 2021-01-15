"""
Design a class, MovingAverage, which contains a method, next that is
responsible for returning the moving average from a stream of integers.

Note: a moving average is the average of a subset of data at a given
point in time.

Ex: Given the following series of events...

// the moving average has a capacity of 3.
MovingAverage movingAverage = new MovingAverage(3);
m.next(3) returns 3 because (3 / 1) = 3
m.next(5) returns 4 because (3 + 5) / 2 = 4
m.next(7) = returns 5 because (3 + 5 + 7) / 3 = 5
m.next(6) = returns 6 because (5 + 7 + 6) / 3 = 6
"""
from collections import deque


class MovingAverage:
    """Calculates moving average of integer values"""

    def __init__(self, size: int) -> None:
        self.size = size
        self.queue: deque[int] = deque(maxlen=size)

    def __repr__(self) -> str:
        return f'MovingAverage(size={self.size})'

    def next_avg(self, num: int) -> float:
        """Adds a number to the queue and gets the new moving average"""
        # if queue is full, remove an item
        if len(self.queue) >= self.size:
            self.queue.popleft()

        self.queue.append(num)

        avg = sum(self.queue) / len(self.queue)
        return avg


def main() -> None:
    """Main function"""
    moving_average = MovingAverage(3)
    print(moving_average.next_avg(3))
    print(moving_average.next_avg(5))
    print(moving_average.next_avg(7))
    print(moving_average.next_avg(6))


if __name__ == "__main__":
    main()
