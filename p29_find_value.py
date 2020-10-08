r"""
Given the reference to the root of a binary search tree and a search
value, return the reference to the node that contains the value if it
exists and null otherwise.

Note: all values in the binary search tree will be unique.

Ex: Given the tree...

      3
     / \
    1   4

and the search value 1, return a reference to the node containing 1.
Ex: Given the tree

      7
     / \
    5   9
       / \
      8   10

and the search value 9, return a reference to the node containing 9.
Ex: Given the tree

      8
     / \
    6   9

and the search value 7, return null.
"""

from __future__ import annotations
from typing import Any, Optional  # , Protocol, Tuple, Union


class NodeTree:
    """Standard binary tree implementation"""

    def __init__(self, value: Optional[int] = None) -> None:
        self.value = value
        self.left: Optional[NodeTree] = None
        self.right: Optional[NodeTree] = None

    def __repr__(self) -> str:
        return f'NodeTree(value={self.value})'

    def print_inorder(self) -> None:
        """Prints the binary tree in-order"""
        if self.value is not None:
            if self.left is not None:
                self.left.print_inorder()

                print(self.value)

            if self.right is not None:
                self.right.print_inorder()


# It is pretty sad that mypy doesn't support direct recursive types yet
#
# class _BuildTreeTuple(Protocol):
#     # _value: int
#     # children: Optional[Tuple['_BuildTreeTuple',
#     #                          '_BuildTreeTuple', '_BuildTreeTuple']]

#     @property
#     def value(self) -> Union[
#         int,
#         Tuple[
#             '_BuildTreeTuple',
#             '_BuildTreeTuple',
#             '_BuildTreeTuple',
#         ]
#     ]: ...


# class BuildTreeTuple(_BuildTreeTuple):
#     value: Union[
#         int,
#         Tuple[
#             '_BuildTreeTuple',
#             '_BuildTreeTuple',
#             '_BuildTreeTuple',
#         ]
#     ]


def build_tree(value: Any) -> NodeTree:
    """Builds binary tree, input is in pre-order form"""
    tree: Optional[NodeTree] = None

    if value is None:
        tree = NodeTree()
    elif isinstance(value, int):
        tree = NodeTree(value)
    else:
        tree = build_tree(value[0])
        tree.left = build_tree(value[1])
        tree.right = build_tree(value[2])

    assert tree is not None
    return tree


def find_tree_node(tree: NodeTree, value: int) -> Optional[NodeTree]:
    """Returns the first node with given value, otherwise None"""
    node: Optional[NodeTree] = None

    if tree.value == value:
        return tree

    if tree.value is not None:
        if tree.left is not None:
            node = find_tree_node(tree.left, value)

        if node:
            return node

        if tree.right is not None:
            node = find_tree_node(tree.right, value)

    return node


def main() -> None:
    """Main function"""
    tree = build_tree([3, 1, 4])
    node = find_tree_node(tree, 1)

    # tree = build_tree([7, 5, [9, 8, 10]])
    # node = find_tree_node(tree, 9)

    # tree = build_tree([8, 6, 9])
    # node = find_tree_node(tree, 7)

    print(node)


if __name__ == "__main__":
    main()
