r"""
Given the root of a binary tree and two values low and high return the
sum of all values in the tree that are within low and high.

Ex: Given the following tree where low = 3 and high = 5...

        1
       / \
      7   5
     /   / \
    4   3   9

return 12 (3, 4, and 5 are the only values within low and high and they
sum to 12)
"""
from data_types.node_tree import build_tree


def main() -> None:
    """Main function"""
    tree = build_tree([1, [7, 4, None], [5, 3, 9]])
    low = 3
    high = 5

    total = 0
    for node in tree:
        if low <= node.value <= high:
            total += node.value

    print(total)


if __name__ == "__main__":
    main()
