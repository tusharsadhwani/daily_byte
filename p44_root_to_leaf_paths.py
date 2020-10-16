r"""
Given a binary tree, return a list of strings containing all root to
leaf paths.

Ex: Given the following tree…

      1
     / \
    2   3

return ["1->2", "1->3"]
Ex: Given the following tree…

      8
     / \
    2  29
      /  \
     3    9

return ["8->2", "8->29->3", "8->29->9"]
"""
from typing import List, Optional

from data_types.node_tree import NodeTree, build_tree


def get_leaf_paths(
        node: NodeTree,
        paths: Optional[List[str]] = None,
        path: str = '') -> List[str]:
    """Traverses the binary tree level by level"""
    if paths is None:
        paths = []

    if not path:
        path = f'{node.value}'
    else:
        path = '->'.join([path, f'{node.value}'])

    if node.left is None and node.right is None:
        paths.append(path)

    if node.left is not None:
        get_leaf_paths(node.left, paths, path)

    if node.right is not None:
        get_leaf_paths(node.right, paths, path)

    return paths


def main() -> None:
    """Main function"""
    tree = build_tree([1, 2, 3])
    # tree = build_tree([8, 2, [29, 3, 9]])

    print(get_leaf_paths(tree))


if __name__ == "__main__":
    main()
