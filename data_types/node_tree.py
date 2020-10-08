"""Standard binary tree implementation"""
from __future__ import annotations
from typing import Any, Generator, Optional  # Protocol, Tuple, Union


class NodeTree:
    """Standard binary tree implementation"""

    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional[NodeTree] = None
        self.right: Optional[NodeTree] = None

    def __repr__(self) -> str:
        return f'NodeTree(value={self.value})'

    def traverse_inorder(self) -> Generator[NodeTree, None, None]:
        """Traverses the binary tree in-order"""
        if self.value is not None:
            if self.left is not None:
                yield from self.left.traverse_inorder()

            yield self

            if self.right is not None:
                yield from self.right.traverse_inorder()

    def print_inorder(self) -> None:
        """Prints the binary tree in-order"""
        print(*[node.value for node in self.traverse_inorder()], sep=', ')


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

    if isinstance(value, int):
        tree = NodeTree(value)
    elif value is not None:
        tree = build_tree(value[0])
        tree.left = build_tree(value[1])
        tree.right = build_tree(value[2])

    assert tree is not None
    return tree
