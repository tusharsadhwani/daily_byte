r"""
Given a binary tree, returns of all its levels in a bottom-up fashion
(i.e. last level towards the root).

Ex: Given the following tree...

      2
     / \
    1   2

return [[1, 2], [2]]

Ex: Given the following tree...

        7
       / \
      6   2
     / \
    3   3

return [[3, 3], [6, 2], [7]]
"""

from data_types.node_tree import build_tree, level_order_traversal


def main() -> None:
    """Main function"""
    tree = build_tree([2, 1, 2])
    # tree = build_tree([7, [6, 3, 3], 2])

    levels = level_order_traversal(tree)
    print(levels[::-1])


if __name__ == "__main__":
    main()
