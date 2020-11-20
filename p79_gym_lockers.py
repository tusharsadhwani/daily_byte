"""
In a gym hallway there are N lockers. You walk back and forth down the
hallway opening and closing lockers. On your first pass you open all
the lockers. On your second pass, you close every other locker.
On your third pass you open every third locker. After walking the
hallway N times opening/closing lockers in the previously described
manner, how many locker are left open?

Ex: Given the following value of N...

N = 1, return 1.
You walk down the hallway once and open the only locker.
Ex: Given the following value of N...

N = 2, return 1.
You walk down the hallway and open both lockers.
You walk back down the hallway and close the last locker.
"""
from math import sqrt


def gym_lockers(num: int) -> int:
    """Returns how many lockers will be left open at the end"""
    lockers = [False for _ in range(num)]

    for step in range(1, num+1):
        for i in range(step, len(lockers)+1, step):
            is_open = lockers[i-1]
            lockers[i-1] = not is_open

    return lockers.count(True)


def main() -> None:
    """Main function"""
    num = int(input('> '))

    print(gym_lockers(num))
    # the answer should be the same as flooring the square root of N.
    print(int(sqrt(num)))


if __name__ == "__main__":
    main()
