r"""
This question is asked by Amazon. Given the root of a binary tree where
every node’s value is either 0 or 1 remove every subtree that does not
have a 1 in it.

Ex: Given the following binary tree...

      1
     / \
    1   0

Return the tree such that it’s been modified to look as follows...

      1
     /
    1

Ex: Given the following binary tree...

      1
     / \
    1   1

Return the tree such that it’s been modified to look as follows...

      1
     / \
    1   1

(No modifications are necessary)
"""
from typing import Optional
from data_types.node_tree import NodeTree, build_tree


def is_zeroes(tree: NodeTree) -> bool:
    """Returns if a subtree is made up of all zeroes"""
    if tree.value != 0:
        return False

    if tree.left and not is_zeroes(tree.left):
        return False

    if tree.right and not is_zeroes(tree.right):
        return False

    return True


def clean_tree(tree: NodeTree) -> Optional[NodeTree]:
    """Cleans out zero-subtrees in a binary tree"""
    if is_zeroes(tree):
        return None

    if tree.left is not None:
        if is_zeroes(tree.left):
            tree.left = None
    if tree.right is not None:
        if is_zeroes(tree.right):
            tree.right = None

    return tree


def main() -> None:
    """Main function"""
    tree = build_tree([1, 1, 0])
    # tree = build_tree([1, 1, 1])
    # tree = build_tree([1, [0, 1, 0], [0, 0, 0]])

    cleaned_tree = clean_tree(tree)
    if cleaned_tree:
        cleaned_tree.print_inorder()
    else:
        print(None)


if __name__ == "__main__":
    main()
