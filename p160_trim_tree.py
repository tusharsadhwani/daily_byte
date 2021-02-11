r"""
You are given the reference to the root of a binary tree and are asked
to trim the tree of “dead” nodes. A dead node is a node whose value is
listed in the provided dead array. Once the tree has been trimmed of all
dead nodes, return a list containing references to the roots of all the
remaining segments of the tree.

Ex: Given the following binary tree and array dead...

         3
       /   \
      1     7
     / \   / \
    2   8 4   6,

dead = [7, 8],
return a list containing a reference to the following nodes: [3, 4, 6].
"""
from collections import deque
from typing import Deque

from data_types.node_tree import NodeTree, build_tree


def trim_tree(root: NodeTree, dead: list[int]) -> list[NodeTree]:
    """Trims dead tree nodes, and returns new head nodes"""
    new_heads: list[NodeTree] = []
    queue: Deque[NodeTree] = deque()
    dead_set = set(dead)

    if root.value not in dead_set:
        new_heads.append(root)

    queue.append(root)
    while queue:
        node = queue.popleft()
        node_dead = node.value in dead_set

        if node.left is not None:
            if node_dead and node.left.value not in dead_set:
                new_heads.append(node.left)

            queue.append(node.left)

        if node.right is not None:
            if node_dead and node.right.value not in dead_set:
                new_heads.append(node.right)

            queue.append(node.right)

    return new_heads


def main() -> None:
    """Main function"""
    tree = build_tree([3, [1, 2, 8], [7, 4, 6]])
    dead = [7, 8]

    print([node.value for node in trim_tree(tree, dead)])


if __name__ == '__main__':
    main()
