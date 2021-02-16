r"""
Given the reference to a binary search tree, “level-up” the tree.
Leveling-up the tree consists of modifying every node in the tree such
that every node’s value increases by the sum of all the node’s values
that are larger than it.

Note: The tree will only contain unique values and you may assume that
it is a valid binary search tree.

Ex: Given a reference to the following binary search tree...

    0
     \
      3, modify the tree such that it becomes...

    3
     \
      3

Ex: Given a reference to the following binary search tree...

      2
     / \
    1   3, modify the tree such that it becomes...

      5
     / \
    6   3
"""
from typing import Generator
from data_types.node_tree import NodeTree, build_tree


def reverse_inorder(tree: NodeTree) -> Generator[NodeTree, None, None]:
    """Traverse in reverse inorder"""
    if tree.right is not None:
        yield from reverse_inorder(tree.right)

    yield tree

    if tree.left is not None:
        yield from reverse_inorder(tree.left)


def level_up(tree: NodeTree) -> None:
    """Levels up the tree"""
    total = 0
    for node in reverse_inorder(tree):
        total += node.value
        node.value = total


def main() -> None:
    """Main function"""
    tree = build_tree([0, None, 3])
    # tree = build_tree([2, 1, 3])

    level_up(tree)
    tree.print_inorder()


if __name__ == '__main__':
    main()
