r"""
Given a binary tree, return its level order traversal where the nodes in
each level are ordered from left to right.

Ex: Given the following tree...

      4
     / \
    2   7

return [[4], [2, 7]]

Ex: Given the following tree...

      2
     / \
    10  15
          \
           20

return [[2], [10, 15], [20]]

Ex: Given the following tree...

        1
       / \
      9   32
     /      \
    3        78

return [[1], [9, 32], [3, 78]]
"""
from data_types.node_tree import build_tree, level_order_traversal


def main() -> None:
    """Main function"""
    tree = build_tree([4, 2, 7])
    # tree = build_tree([2, 10, [15, None, 20]])
    # tree = build_tree([1, [9, 3, None], [32, None, 78]])

    levels = level_order_traversal(tree)
    print(levels)


if __name__ == "__main__":
    main()
