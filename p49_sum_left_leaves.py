r"""
Given a binary tree, return the sum of all left leaves of the tree.

Ex: Given the following tree...

      5
     / \
    2   12
       /  \
      3    8

return 5 (i.e. 2 + 3)

Ex: Given the following tree...

        2
       / \
      4   2
     / \
    3   9

return 3
"""
from data_types.node_tree import NodeTree, build_tree


def sum_left_leaves(tree: NodeTree) -> int:
    """Returns the sum of all left leaves of the tree."""

    def is_leaf(node: NodeTree) -> bool:
        return node.left is None and node.right is None

    leaf_sum = 0

    # Special case: if root node has no left child
    if tree.left is None:
        leaf_sum += tree.value

    for node in tree:
        left_child = node.left
        if left_child is not None and is_leaf(left_child):
            leaf_sum += left_child.value

    return leaf_sum


def main() -> None:
    """Main function"""
    tree = build_tree([5, 2, [12, 3, 8]])
    # tree = build_tree([2, [4, 3, 9], 2])

    print(sum_left_leaves(tree))


if __name__ == "__main__":
    main()
