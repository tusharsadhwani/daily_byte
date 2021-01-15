r"""
Given the reference to the root of a binary tree and a value k, return
the number of paths in the tree such that the sum of the nodes along the
path equals k.

Note: The path does not need to start at the root of the tree, but must
move downward.

Ex: Given the following binary tree and value k...

      3
     / \
    1   8

k = 11, return 1 (3 -> 8).

Ex: Given the following binary tree and value k...

        2
       / \
     -4   9
     /
    2

k = 2, return 3 (2, 2 -> -4, -4 -> 2).
"""
from functools import cache

from data_types.node_tree import NodeTree, build_tree


@cache
def tree_path_sums(node: NodeTree) -> list[int]:
    """Returns the sums of all tree paths from given node"""
    sums: list[int] = [node.value]

    if node.left is not None:
        child_sums = tree_path_sums(node.left)
        sums.extend(node.value + value for value in child_sums)

    if node.right is not None:
        child_sums = tree_path_sums(node.right)
        sums.extend(node.value + value for value in child_sums)

    return sums


def main() -> None:
    """Main function"""
    tree = build_tree([3, 1, 8])
    num = 11
    # tree = build_tree([2, [-4, 2, None], 9])
    # num = -2

    path_sums: list[int] = []
    for node in tree:
        path_sums.extend(tree_path_sums(node))

    print(path_sums.count(num))


if __name__ == "__main__":
    main()
