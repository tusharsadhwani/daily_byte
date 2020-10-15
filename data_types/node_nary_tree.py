"""Standard N-ary tree implementation"""
from __future__ import annotations
from typing import Any, Generator, List, Optional


class NodeTree:
    """Standard N-ary tree implementation"""

    def __init__(self, value: int) -> None:
        self.value = value
        self.children: Optional[List[NodeTree]] = None

    def __repr__(self) -> str:
        return f'NodeTree(value={self.value})'

    def __iter__(self) -> Generator[NodeTree, None, None]:
        """Traverses the binary tree pre-order"""
        if self.value is not None:
            yield self

            if self.children is not None:
                for node in self.children:
                    yield from node

    def print(self) -> None:
        """Prints the binary tree in pre-order"""
        print(*[node.value for node in self], sep=', ')


def _build_nary_tree(value: Any) -> Optional[NodeTree]:
    """Recursive function for build_tree"""
    tree: Optional[NodeTree] = None

    if isinstance(value, int):
        tree = NodeTree(value)
    elif value is not None:
        tree = _build_nary_tree(value[0])
        assert tree is not None
        child_values = value[1]

        tree.children = []
        for child in child_values:
            child_node = _build_nary_tree(child)
            if child_node is not None:
                tree.children.append(child_node)

    return tree


def build_nary_tree(value: Any) -> NodeTree:
    """Builds binary tree, input is in pre-order form"""
    assert value is not None
    tree = _build_nary_tree(value)
    assert tree is not None
    return tree


def level_order_traversal(
        node: NodeTree,
        levels: Optional[List[List[int]]] = None,
        level: int = 0) -> List[List[int]]:
    """Traverses the binary tree level by level"""
    if not levels:
        levels = []

    if level == len(levels):  # check if new level needs to be added
        levels.append([node.value])
    else:
        levels[level].append(node.value)

    if node.children is not None:
        for child in node.children:
            level_order_traversal(child, levels, level+1)

    return levels
