r"""
Given a binary tree, containing unique values, determine if it is a
valid binary search tree.

Note: the invariants of a binary search tree (in our case) are all
values to the left of a given node are less than the current node’s
value, all values to the right of a given node are greater than the
current node’s value, and both the left and right subtrees of a given
node must also be binary search trees.

Ex: Given the following binary tree…

      1
     / \
    2   3

return false.

Ex: Given the following tree…

      2
     / \
    1   3

return true.
"""
from data_types.node_tree import NodeTree, build_tree


def validate_bst(tree: NodeTree) -> bool:
    """Returns if a tree is a BST or not"""
    if tree.left is not None:
        if tree.left.value > tree.value:
            return False

        left_valid = validate_bst(tree.left)
        if not left_valid:
            return False

    if tree.right is not None:
        if tree.right.value < tree.value:
            return False

        right_valid = validate_bst(tree.right)
        if not right_valid:
            return False

    return True


def main():
    """Main function"""
    tree = build_tree([1, 2, 3])
    # tree = build_tree([2, 1, 3])

    print(validate_bst(tree))


if __name__ == "__main__":
    main()
