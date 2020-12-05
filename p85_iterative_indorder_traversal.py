r"""
Given a binary tree, return a list containing its inorder traversal
without using recursion.

Ex: Given the following tree...

      2
     / \
    1   3

return [1, 2, 3]

Ex: Given the following tree...

        2
       / \
      1   7
     / \
    4   8

return [4, 1, 8, 2, 7]
"""

from typing import List, Optional
from data_types.node_tree import NodeTree, build_tree


def iterative_inorder_traversal(tree: NodeTree) -> List[int]:
    """Implements iterative inorder traversal"""
    current: Optional[NodeTree] = tree
    stack: List[NodeTree] = []

    items: List[int] = []

    while True:
        if current is not None:
            stack.append(current)
            current = current.left

        elif len(stack) > 0:
            current = stack.pop()
            items.append(current.value)
            current = current.right

        else:
            break

    return items


def main() -> None:
    """Main function"""
    tree = build_tree([2, 1, 3])
    # tree = build_tree([2, [1, 4, 8], 7])

    print(iterative_inorder_traversal(tree))


if __name__ == "__main__":
    main()
