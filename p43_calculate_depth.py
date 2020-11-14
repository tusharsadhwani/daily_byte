r"""
Given a binary tree, return its maximum depth.
Note: the maximum depth is defined as the number of nodes along the
longest path from root node to leaf node.

Ex: Given the following tree...

      9
     / \
    1   2

return 2
Ex: Given the following tree...

      5
     / \
    1  29
      /  \
     4   13

return 3
"""
from data_types.node_tree import NodeTree, build_tree


def calculate_depth(node: NodeTree, level: int = 1) -> int:
    """Calculates depth of binary tree"""
    left_level = right_level = level

    if node.left is not None:
        left_level = calculate_depth(node.left, level+1)

    if node.right is not None:
        right_level = calculate_depth(node.right, level+1)

    return max(left_level, right_level)


def main() -> None:
    """Main function"""
    tree = build_tree([9, 1, 2])
    tree = build_tree([5, 1, [29, 4, 13]])

    print(calculate_depth(tree))


if __name__ == "__main__":
    main()
