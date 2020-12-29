r"""
Given a binary tree, return the bottom-left most value.

Note: You may assume each value in the tree is unique.

Ex: Given the following binary tree...

        1
       / \
      2   3
     /
    4

return 4.

Ex: Given the following binary tree...

      8
     / \
    1   4
       /
      2

return 2.
"""
from data_types.node_tree import build_tree, level_order_traversal


def main() -> None:
    """Main function"""
    tree = build_tree([1, [2, 4, None], 3])
    # tree = build_tree([8, 1, [4, 2, None]])

    bottom_level = []
    for level in level_order_traversal(tree):
        bottom_level = level

    print(bottom_level[0])


if __name__ == "__main__":
    main()
