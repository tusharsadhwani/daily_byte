"""
Given an integer n, return whether or not it is a power of three.

Ex: Given the following value for n...

n = 9, return true

Ex: Given the following value for n...

n = 50, return false
"""


def is_power_of_three(num: float) -> bool:
    """Returns if num is a power of three"""
    while num > 1:
        num /= 3

    return num == 1


def main() -> None:
    """Main function"""
    num = 9
    # num = 50

    print(is_power_of_three(num))


if __name__ == '__main__':
    main()
