r"""
Given a binary search tree, return the minimum difference between any
two nodes in the tree.

Ex: Given the following tree...

      2
     / \
    3   1

return 1.

Ex: Given the following tree...

         29
        /  \
      17   50
     /     / \
    1    42  59

return 8.

Ex: Given the following tree...

    2
     \
     100

return 98.
"""
from typing import Optional

from data_types.node_tree import NodeTree, build_tree


def main() -> None:
    """Main function"""
    bst = build_tree([2, 3, 1])
    # bst = build_tree([29, [17, 1, None], [50, 42, 59]])
    # bst = build_tree([2, None, 100])

    prev_node: Optional[NodeTree] = None
    least_difference: Optional[int] = None
    for node in bst:
        if prev_node is None:
            prev_node = node
            continue

        difference = abs(node.value - prev_node.value)

        if least_difference is None:
            least_difference = difference
            continue

        if difference < least_difference:
            least_difference = difference

        prev_node = node

    print(least_difference)


if __name__ == "__main__":
    main()
