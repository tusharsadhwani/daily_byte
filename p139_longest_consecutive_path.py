r"""
Given the reference to a binary tree, return the length of the longest
path in the tree that contains consecutive values.

Note: The path must move downward in the tree.
Ex: Given the following binary tree...

    1
     \
      2
       \
        3
return 3.

Ex: Given the following binary tree...

        1
       / \
      2   2
     / \ / \
    4  3 5  8
      /
     4
return 4.
"""
from functools import cache

from data_types.node_tree import NodeTree, build_tree


@cache
def longest_chain(node: NodeTree) -> int:
    """Returns the number of consecutive numbers below given node"""
    max_consecutives = 1  # itself

    if node.left and node.left.value == node.value + 1:
        consecutive_count = 1 + longest_chain(node.left)
        max_consecutives = max(max_consecutives, consecutive_count)

    if node.right and node.right.value == node.value + 1:
        consecutive_count = 1 + longest_chain(node.right)
        max_consecutives = max(max_consecutives, consecutive_count)

    return max_consecutives


def main() -> None:
    """Main function"""
    tree = build_tree([1, None, [2, None, 3]])
    # tree = build_tree([1, [2, 4, [3, 4, None]], [2, 5, 8]])

    max_length = max(longest_chain(node) for node in tree)
    print(max_length)


if __name__ == "__main__":
    main()
