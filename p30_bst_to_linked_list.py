r"""
Given a binary search tree, rearrange the tree such that it forms a
linked list where all its values are in ascending order.

Ex: Given the following tree...
        5
       / \
      1   6

return...

    1
     \
      5
       \
        6

Ex: Given the following tree...

        5
       / \
      2   9
     / \
    1   3

return...

    1
     \
      2
       \
        3
         \
          5
           \
            9
Ex: Given the following tree...

    5
     \
      6

return...

    5
     \
      6
"""

from data_types.node_list import create_node_list
from data_types.node_tree import build_tree


def main() -> None:
    """Main function"""
    tree = build_tree([5, 1, 6])
    # tree = build_tree([5, [2, 1, 3], 9])
    # tree = build_tree([5, None, 6])

    node_list = create_node_list([
        node.value
        for node in tree.traverse_inorder()
    ])

    node_list.print()


if __name__ == "__main__":
    main()
