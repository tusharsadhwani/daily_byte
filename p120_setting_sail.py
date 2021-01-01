"""
You’re about to set sail off a pier and first want to count the number
of ships that are already in the harbor. The harbor is deemed safe to
sail in if the number of boats in the harbor is strictly less than
limit. Given a 2D array that presents the harbor, where O represents
water and S represents a ship, return whether or not it’s safe for you
to set sail.

Note: All ships in the harbor can only lie entirely vertically or
entirely horizontally and cannot be connected to another ship.

Ex: Given the following 2D array harbor and value limit...

harbor = [
    [O, O, S],
    [S, O, O],
    [O, O, S]
], limit = 5, return true.
You setting sail would cause there to be 4 ships in the harbor which is
under the limit of 5.

Ex: Given the following 2D array harbor and value limit...

harbor = [
    [O, O, O],
    [S, O, S],
    [O, O, S]
], limit = 3, return false.
The harbor is not safe to sail in since you setting sail would cause the
number of boats in the harbor to reach the limit.
"""


from utils.grid import count_entities


def main() -> None:
    """Main function"""
    harbor = [
        ['O', 'O', 'S'],
        ['S', 'O', 'O'],
        ['O', 'O', 'S']
    ]
    limit = 5
    # harbor = [
    #     ['O', 'O', 'O'],
    #     ['S', 'O', 'S'],
    #     ['O', 'O', 'S']
    # ]
    # limit = 3

    count = count_entities(harbor, 'S')
    print(count+1 < limit)


if __name__ == "__main__":
    main()
