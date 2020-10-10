r"""
Given a binary tree, return its level order traversal where the nodes in
each level are ordered from left to right.

Ex: Given the following tree...

      4
     / \
    2   7

return [[4], [2, 7]]

Ex: Given the following tree...

      2
     / \
    10  15
          \
           20

return [[2], [10, 15], [20]]

Ex: Given the following tree...

        1
       / \
      9   32
     /      \
    3        78

return [[1], [9, 32], [3, 78]]
"""
from typing import List

from data_types.node_tree import NodeTree, build_tree

levels: List[List[int]] = []


def level_order_traversal(node: NodeTree, level: int = 0) -> None:
    """Traverses the binary tree in-order"""
    if level == len(levels):  # check if new level needs to be added
        levels.append([node.value])
    else:
        levels[level].append(node.value)

    if node.left is not None:
        level_order_traversal(node.left, level+1)

    if node.right is not None:
        level_order_traversal(node.right, level+1)


def main() -> None:
    """Main function"""
    tree = build_tree([4, 2, 7])
    # tree = build_tree([2, 10, [15, None, 20]])
    # tree = build_tree([1, [9, 3, None], [32, None, 78]])

    level_order_traversal(tree)
    print(levels)


if __name__ == "__main__":
    main()
