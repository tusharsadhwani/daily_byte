r"""
Given the reference to a binary search tree, return the kth smallest value in the tree.

Ex: Given the following binary search tree and value k...

      3
     / \
    2   4

k = 1, return 2.

Ex: Given the following binary search tree and value k...

      7
     / \
    3   9
     \
      5

k = 3, return 7.
"""
from data_types.node_tree import build_tree


def main() -> None:
    """Main function"""
    tree = build_tree([3, 2, 4])
    index = 1
    # tree = build_tree([7, [3, None, 5], 9])
    # index = 3

    print(list(tree)[index-1].value)


if __name__ == "__main__":
    main()
