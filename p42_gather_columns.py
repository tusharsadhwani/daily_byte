r"""
Given a binary tree, return its column order traversal from top to
bottom and left to right. Note: if two nodes are in the same row and
column, order them from left to right.

Ex: Given the following tree...

      8
     / \
    2   29
       /  \
      3    9

return [[2], [8, 3], [29], [9]]
Ex: Given the following tree...

         100
        /   \
      53     78
     / \    /  \
    32  3  9    20

return [[32], [53], [100, 3, 9], [78], [20]]
"""
from typing import Optional

from data_types.node_tree import NodeTree, build_tree


def gather_columns(
        node: NodeTree,
        levels: Optional[list[list[int]]] = None,
        level: int = 0) -> list[list[int]]:
    """Returns column order traversal list of binary tree"""
    if levels is None:
        levels = []

    if level == len(levels):  # check if new level needs to be added
        levels.append([node.value])
    else:
        if level == -1:
            levels.insert(0, [node.value])
            level = 0
        else:
            levels[level].append(node.value)

    list_length_before = len(levels)
    if node.left is not None:
        gather_columns(node.left, levels, level-1)
    list_length_after = len(levels)

    # Since the previous gather_columns will cause the length of the
    # list to grow, we need to track the offset to make sure we insert
    # our right hand nodes into the right index
    list_length_delta = list_length_after - list_length_before
    if node.right is not None:
        gather_columns(node.right, levels, level+1 + list_length_delta)

    return levels


def main() -> None:
    """Main function"""
    tree = build_tree([8, 2, [29, 3, 9]])
    # tree = build_tree([100, [53, 32, 3], [78, 9, 20]])

    print(gather_columns(tree))


if __name__ == "__main__":
    main()
