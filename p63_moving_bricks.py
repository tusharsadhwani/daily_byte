"""
You are transporting bricks on a construction site and want to work as
efficiently as possible. The weight of each brick is given by bricks[i].

Given a wheelbarrow that can carry up to (not including) 5000 pounds,
return then maximum number of bricks you can place in your wheelbarrow
to transport.

Ex: Given the following bricks...

bricks = [1000, 1000, 1000, 2000], return 3.

Ex: Given the following bricks...

bricks = [1000, 200, 150, 200], return 4.
"""


def main() -> None:
    """Main function"""
    bricks = [1000, 1000, 1000, 2000]
    # bricks = [1000, 200, 150, 200]

    bricks.sort()

    total_weight = 0
    for count, weight in enumerate(bricks):
        total_weight += weight
        if total_weight >= 5000:
            break
    else:
        count += 1

    print(count)


if __name__ == "__main__":
    main()
