"""
Given a staircase with N steps and the ability to climb either one or
two steps at a time, return the total number of ways to arrive at the
top of the staircase.

Ex: Given the following value of N...

N = 2, return 2
1 step + 1 step
2 steps

Ex: Given the following value of N...

N = 3, return 3
1 step + 1 step + 1 step
1 step + 2 steps
2 steps + 1 step
"""
from functools import lru_cache
from typing import Dict


def stairs_fib(count: int) -> int:
    """The solution is exactly the same as Nth fibonacci number"""
    @lru_cache
    def fibonacci(num: int) -> int:
        if num <= 1:
            return 1
        return fibonacci(num-1) + fibonacci(num-2)

    return fibonacci(count)


def stairs_dp(count: int) -> int:
    """Dynamic Programming solution to find ways to climb the stairs"""
    # Dictionary to hold number of solutions for i stairs
    num_solutions: Dict[int, int] = {}

    num_solutions[0] = 1
    num_solutions[1] = 1

    for i in range(2, count+1):
        num_solutions[i] = num_solutions[i-1] + num_solutions[i-2]

    return num_solutions[count]


def stairs_recursive(count: int) -> int:
    """Recursive solution to find number of ways to climb the stairs"""
    if count <= 1:
        return 1

    solutions = 0
    # Number of solutions for climbing 1 step at the beginning
    solutions += stairs_recursive(count-1)
    # Number of solutions for climbing 2 steps at the beginning
    solutions += stairs_recursive(count-2)

    return solutions


def main() -> None:
    """Main function"""
    count = 2
    # count = 3

    print(stairs_recursive(count))
    print(stairs_dp(count))
    print(stairs_fib(count))


if __name__ == "__main__":
    main()
