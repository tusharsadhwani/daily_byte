r"""
Given the reference to the root of a binary search tree and a search
value, return the reference to the node that contains the value if it
exists and null otherwise.

Note: all values in the binary search tree will be unique.

Ex: Given the tree...

      3
     / \
    1   4

and the search value 1 return a reference to the node containing 1.
Ex: Given the tree

      7
     / \
    5   9
       / \
      8   10

and the search value 9 return a reference to the node containing 9.
Ex: Given the tree

      8
     / \
    6   9

and the search value 7 return null.
"""

from __future__ import annotations
from typing import Any, Optional


class NodeTree:
    """Standard binary tree implementation"""

    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional[NodeTree] = None
        self.right: Optional[NodeTree] = None

    def print_inorder(self) -> None:
        if self.left is not None:
            self.left.print_inorder()

        print(self.value)

        if self.right is not None:
            self.right.print_inorder()


# It is pretty sad that mypy doesn't support recursive types yet
#
# BuildTreeTuple = Union[
#     int,
#     Tuple[
#         Union[int, 'BuildTreeTuple'],
#         Union[int, 'BuildTreeTuple'],
#         Union[int, 'BuildTreeTuple']
#     ]
# ]


def build_tree(value: Any) -> NodeTree:
    """Builds binary tree"""
    tree: Optional[NodeTree] = None
    if isinstance(value, int):
        tree = NodeTree(value)
    else:
        tree = build_tree(value[0])
        tree.left = build_tree(value[1])
        tree.right = build_tree(value[2])

    assert tree is not None
    return tree


def main() -> None:
    """Main function"""
    tree = build_tree([1, 2, [3, 4, 5]])
    tree.print_inorder()


if __name__ == "__main__":
    main()
