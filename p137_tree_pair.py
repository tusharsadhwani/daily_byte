r"""
Given the reference to the root of a binary search tree and a target
value, return whether or not two individual values within the tree can
sum to the target.

Ex: Given the following tree and target…

      1
     / \
    2   3, target = 4, return true.

Ex: Given the following tree and target…

      1
     / \
    2   3, target = 7, return false.
"""
from data_types.node_tree import NodeTree, build_tree


def main() -> None:
    """Main function"""
    tree = build_tree([1, 2, 3])
    value = 4
    # value = 7

    print(tree_pair(tree, value))


def tree_pair(tree: NodeTree, value: int) -> bool:
    """Returns if two values in the tree sum to given value"""
    for a in tree:
        for b in tree:
            if a.value + b.value == value:
                return True
    return False


if __name__ == "__main__":
    main()
