"""Standard binary tree implementation"""
from typing import Any, Optional  # Protocol, Tuple, Union


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
