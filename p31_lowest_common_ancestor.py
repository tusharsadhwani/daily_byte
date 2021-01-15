r"""
Given a binary search tree that contains unique values and two nodes
within the tree, a, and b, return their lowest common ancestor.

Note: the lowest common ancestor of two nodes is the deepest node within
the tree such that both nodes are descendants of it.

Ex: Given the following tree...

        7
       / \
      2   9
     / \
    1   5

and a = 1, b = 9, return a reference to the node containing 7.
Ex: Given the following tree...

        8
       / \
      3   9
     / \
    2   6

and a = 2, b = 6, return a reference to the node containing 3.
Ex: Given the following tree...

      8
     / \
    6   9

and a = 6, b = 8, return a reference to the node containing 8.
"""
from typing import Optional

from data_types.node_tree import NodeTree, build_tree


def find_trail(
        tree: NodeTree,
        value: int,
        trail: Optional[list[NodeTree]] = None) -> tuple[bool, list[NodeTree]]:
    """Returns the ancestor trail of a value in a tree, if found"""
    if trail is None:
        trail = []

    trail = [*trail, tree]
    found = False

    if tree.value == value:
        found = True
        return found, trail

    if tree.left is not None:
        found, new_trail = find_trail(tree.left, value, trail)
        if found:
            return found, new_trail

    if tree.right is not None:
        found, new_trail = find_trail(tree.right, value, trail)
        if found:
            return found, new_trail

    return False, []


def main() -> None:
    """Main function"""
    tree = build_tree([7, [2, 1, 5], 9])
    value_a, value_b = 1, 9

    # tree = build_tree([8, [3, 2, 6], 9])
    # value_a, value_b = 2, 6

    # tree = build_tree([8, 6, 9])
    # value_a, value_b = 6, 8

    _, trail_a = find_trail(tree, value_a)
    _, trail_b = find_trail(tree, value_b)

    common_trail: list[NodeTree] = []
    for node_a, node_b in zip(trail_a, trail_b):
        if node_a != node_b:
            break

        common_trail.append(node_a)

    if common_trail:
        lowest_common_ancestor = common_trail[-1]
        print(lowest_common_ancestor)
    else:
        print(None)


if __name__ == "__main__":
    main()
