"""Standard binary tree implementation"""
from __future__ import annotations
from itertools import zip_longest
from typing import Any, Generator, Optional  # Protocol, Tuple, Union


class NodeTree:
    """Standard binary tree implementation"""

    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional[NodeTree] = None
        self.right: Optional[NodeTree] = None

    def __repr__(self) -> str:
        return f'NodeTree(value={self.value})'

    def __eq__(self, other: object) -> bool:
        """Checks if two trees have identical shape and contents.
        It does so by checking if the in-order and pre-order contents
        of both the trees is identical."""
        if not isinstance(other, NodeTree):
            return NotImplemented

        for self_node, other_node in zip_longest(self, other):
            if self_node.value != other_node.value:
                return False

        for self_node, other_node in zip_longest(
                self.traverse_preorder(), other.traverse_preorder()):
            if self_node.value != other_node.value:
                return False

        return True

    def __iter__(self) -> Generator[NodeTree, None, None]:
        return self.traverse_inorder()

    def traverse_inorder(self) -> Generator[NodeTree, None, None]:
        """Traverses the binary tree in-order"""
        if self.value is not None:
            if self.left is not None:
                yield from self.left.traverse_inorder()

            yield self

            if self.right is not None:
                yield from self.right.traverse_inorder()

    def traverse_preorder(self) -> Generator[NodeTree, None, None]:
        """Traverses the binary tree pre-order"""
        if self.value is not None:
            yield self

            if self.left is not None:
                yield from self.left.traverse_preorder()

            if self.right is not None:
                yield from self.right.traverse_preorder()

    def print_inorder(self) -> None:
        """Prints the binary tree in-order"""
        print(*[node.value for node in self], sep=', ')


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


def _build_tree(value: Any) -> Optional[NodeTree]:
    """Recursive function for build_tree"""
    tree: Optional[NodeTree] = None

    if isinstance(value, int):
        tree = NodeTree(value)
    elif value is not None:
        tree = _build_tree(value[0])
        assert tree is not None

        tree.left = _build_tree(value[1])
        tree.right = _build_tree(value[2])

    return tree


def build_tree(value: Any) -> NodeTree:
    """Builds binary tree, input is in pre-order form"""
    assert value is not None
    tree = _build_tree(value)
    assert tree is not None
    return tree
