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
from data_types.node_tree import build_tree, get_leaf_paths


def main() -> None:
    """Main function"""
    tree = build_tree([1, 2, 3])
    # tree = build_tree([8, 2, [29, 3, 9]])

    print(['->'.join(str(val) for val in path)
           for path in get_leaf_paths(tree)])


if __name__ == "__main__":
    main()
