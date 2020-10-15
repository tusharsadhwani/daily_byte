r"""
Given an n-ary tree, return its level order traversal.

Note: an n-ary tree is a tree in which each node has no more than N
children.

Ex: Give the following n-ary tree…

       8
     / | \
    2  3  29

return [[8], [2, 3, 29]]

Ex: Given the following n-ary tree…

         2
       / | \
      1  6  9
     /   |   \
    8    2    2
       / | \
     19 12 90

return [[2], [1, 6, 9], [8, 2, 2], [19, 12, 90]]
"""
from data_types.node_nary_tree import build_nary_tree, level_order_traversal


def main() -> None:
    """Main function"""
    tree = build_nary_tree([8, [2, 3, 29]])
    # tree = build_nary_tree([2, [[1, [8]], [6, [[2, [19, 12, 90]]]], [9, [2]]]])

    print(level_order_traversal(tree))


if __name__ == "__main__":
    main()
