"""
This question is asked by Amazon. Given N distinct rooms that are locked
we want to know if you can unlock and visit every room. Each room has a
list of keys in it that allows you to unlock and visit other rooms. We
start with room 0 being unlocked. Return whether or not we can visit
every room.

Ex: Given the following rooms...

rooms = [[1], [2], []], return true

Ex: Given the following rooms...

rooms = [[1, 2], [2], [0], []], return false, we can’t enter room 3.
"""


def can_unlock(rooms: list[list[int]]) -> bool:
    """Returns if you can unlock all rooms"""
    keys = {0}
    opened = set[int]()

    while keys:
        key = keys.pop()
        opened.add(key)

        new_keys = rooms[key]
        for new_key in new_keys:
            if new_key not in opened:
                keys.add(new_key)

    return len(opened) == len(rooms)


def main() -> None:
    """Main function"""
    rooms: list[list[int]]
    rooms = [[1], [2], []]
    # rooms = [[1, 2], [2], [0], []]

    print(can_unlock(rooms))


if __name__ == "__main__":
    main()
