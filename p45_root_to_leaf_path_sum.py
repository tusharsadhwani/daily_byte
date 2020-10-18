r"""
Given a binary tree and a target, return whether or not there exists a
root to leaf path such that all values along the path sum to the target.

Ex: Given the following tree…

        1
       / \
      5   2
     /   / \
    1  12   29

and a target of 15, return true as the path 1->2->12 sums to 15.

Ex: Given the following tree…

         104
        /   \
      39     31
     / \    /  \
    32  1  9    10

and a target of 175, return true as the path 104->39->32 sums to 175.
"""
from data_types.node_tree import NodeTree, build_tree, get_leaf_paths


def check_tree_leaf_path_sum(tree: NodeTree, target: int) -> bool:
    """Returns if a root to leaf sum of `target` is present in the tree"""
    path_sum = [sum(path) for path in get_leaf_paths(tree)]
    return target in path_sum


def main() -> None:
    """Main function"""
    tree = build_tree([1, [5, 1, None], [2, 12, 29]])
    target = 15

    # tree = build_tree([104, [39, 32, 1], [31, 9, 10]])
    # target = 175

    print(check_tree_leaf_path_sum(tree, target))


if __name__ == "__main__":
    main()
