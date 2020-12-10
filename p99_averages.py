r"""
Given a reference to the root of a binary tree, return a list containing
the average value in each level of the tree.

Ex: Given the following binary tree...

         1
        / \
      6    8
     / \
    1   5

return [1.0, 7.0, 3.0]
"""
from statistics import mean

from data_types.node_tree import build_tree, level_order_traversal


def main() -> None:
    """Main function"""
    tree = build_tree([1, [6, 1, 5], 8])
    print([mean(level) for level in level_order_traversal(tree)])


if __name__ == "__main__":
    main()
