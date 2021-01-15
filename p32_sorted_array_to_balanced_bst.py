r"""
Given an array of numbers sorted in ascending order, return a height
balanced binary search tree using every number from the array.

Note: height balanced meaning that the level of any node’s two subtrees
should not differ by more than one.

Ex: nums = [1, 2, 3] return the following tree...

      2
     / \
    1   3

Ex: nums = [1, 2, 3, 4, 5, 6] return the following tree...

        3
       / \
      2   5
     /   / \
    1   4   6
"""
from typing import Optional

from data_types.node_tree import NodeTree


def _create_balanced_bst(items: list[int]) -> Optional[NodeTree]:
    """Recursive function to create the BST"""
    if not items:
        return None

    mid = len(items) // 2

    tree = NodeTree(items[mid])

    left_child = _create_balanced_bst(items[:mid])
    tree.left = left_child

    right_child = _create_balanced_bst(items[mid+1:])
    tree.right = right_child

    return tree


def create_balanced_bst(items: list[int]) -> NodeTree:
    """Create a balanced binary search tree out of a sorted list"""
    assert len(items) > 0, 'Items must not be empty list'

    tree = _create_balanced_bst(items)

    assert tree is not None
    return tree


def main() -> None:
    """Main function"""
    nums = [1, 2, 3]
    # nums = [1, 2, 3, 4, 5, 6]

    tree = create_balanced_bst(nums)
    assert tree is not None
    tree.print_inorder()


if __name__ == "__main__":
    main()
