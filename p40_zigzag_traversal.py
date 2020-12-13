r"""
Given a binary tree, return its zig-zag level order traversal
(i.e. its level order traversal from left to right the first level,
right to left the level the second, etc.).

Ex: Given the following tree...

      1
     / \
    2   3

return [[1], [3, 2]]

Ex: Given the following tree...

      8
     / \
    2  29
      /  \
     3    9

return [[8], [29, 2], [3, 9]]
"""
from data_types.node_tree import build_tree, level_order_traversal


def main() -> None:
    """Main function"""
    tree = build_tree([1, 2, 3])
    # tree = build_tree([8, 2, [29, 3, 9]])

    levels = level_order_traversal(tree)
    print([level[::-1] if i % 2 else level for i, level in enumerate(levels)])


if __name__ == "__main__":
    main()
