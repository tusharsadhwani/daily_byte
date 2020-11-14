r"""
Given a binary tree, return the largest value in each of its levels.

Ex: Given the following tree...

      2
     / \
    10  15
          \
           20

return [2, 15, 20]

Ex: Given the following tree...

        1
       / \
      5   6
     / \   \
    5   3   7

return [1, 6, 7]
"""
from data_types.node_tree import build_tree, level_order_traversal


def main() -> None:
    """Main function"""
    tree = build_tree([2, 10, [15, None, 20]])
    # tree = build_tree([1, [5, 5, 3], [6, None, 7]])

    levels = level_order_traversal(tree)
    print([max(level) for level in levels])


if __name__ == "__main__":
    main()
