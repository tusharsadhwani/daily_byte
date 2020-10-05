"""
Create a class CallCounter that tracks the number of calls a client has
made within the last 3 seconds. Your class should contain one method,
ping(int t) that receives the current timestamp (in milliseconds) of a
new call being made and returns the number of calls made within the last
3 seconds.

Note: you may assume that the time associated with each subsequent call
to ping is strictly increasing.

Ex: Given the following calls to ping…

ping(1), return 1 (1 call within the last 3 seconds)
ping(300), return 2 (2 calls within the last 3 seconds)
ping(3000), return 3 (3 calls within the last 3 seconds)
ping(3002), return 3 (3 calls within the last 3 seconds)
ping(7000), return 1 (1 call within the last 3 seconds)
"""
from typing import List


class CallCounter:
    """CallCounter implementation"""

    def __init__(self) -> None:
        self.past_timestamps: List[int] = []

    def __repr__(self) -> str:
        return 'CallCounter()'

    def ping(self, latest_timestamp: int) -> int:
        """
        Adds a new call to the call stack, and returns the number of
        calls within the past 3 seconds.
        """
        self.past_timestamps.append(latest_timestamp)

        # Note: can replace with binary search
        for index, timestamp in enumerate(self.past_timestamps):
            if latest_timestamp - timestamp < 3000:
                call_count = len(self.past_timestamps) - index
                return call_count

        # Code should never reach here
        return -1


def main():
    """Main function"""
    call_counter = CallCounter()
    print(call_counter.ping(1))
    print(call_counter.ping(300))
    print(call_counter.ping(3000))
    print(call_counter.ping(3002))
    print(call_counter.ping(7000))


if __name__ == "__main__":
    main()
