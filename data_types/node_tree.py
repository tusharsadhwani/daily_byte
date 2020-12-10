"""Standard binary tree implementation"""
from __future__ import annotations
from itertools import zip_longest
from typing import Any, Generator, List, Optional  # Protocol, Tuple, Union


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

    def leaves(self) -> Generator[NodeTree, None, None]:
        """Returns all leaves in the tree, in order"""
        for node in self:
            if node.left is None and node.right is None:
                yield node


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


def level_order_traversal(
        node: NodeTree,
        levels: Optional[List[List[int]]] = None,
        level: int = 0) -> List[List[int]]:
    """Traverses the binary tree level by level"""
    if levels is None:
        levels = []

    if level == len(levels):  # check if new level needs to be added
        levels.append([node.value])
    else:
        levels[level].append(node.value)

    if node.left is not None:
        level_order_traversal(node.left, levels, level+1)

    if node.right is not None:
        level_order_traversal(node.right, levels, level+1)

    return levels


def level_order_traversal_iter(
        node: NodeTree,
        queue: Optional[List[int]] = None) -> List[int]:
    """Traverses the binary tree level by level, without keeping level count"""
    if queue is None:
        queue = [node.value]

    if node.left is not None:
        queue.append(node.left.value)
    if node.right is not None:
        queue.append(node.right.value)

    if node.left is not None:
        level_order_traversal_iter(node.left, queue)
    if node.right is not None:
        level_order_traversal_iter(node.right, queue)

    return queue


def get_leaf_paths(
        node: NodeTree,
        paths: Optional[List[List[int]]] = None,
        path: Optional[List[int]] = None) -> List[List[int]]:
    """Traverses the binary tree level by level"""
    if paths is None:
        paths = []

    if not path:
        path = []

    path = [*path, node.value]

    if node.left is None and node.right is None:
        paths.append(path)

    if node.left is not None:
        get_leaf_paths(node.left, paths, path)

    if node.right is not None:
        get_leaf_paths(node.right, paths, path)

    return paths
