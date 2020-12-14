r"""
Given an N-ary tree, return its maximum depth.

Note: an N-ary tree is a tree in which any node may have at most N
children.

Ex: Given the following tree...

     4
   / | \
  3  9  2
 /       \
7         2

return 3.
"""
from data_types.node_nary_tree import NodeNaryTree, build_nary_tree


def max_depth(tree: NodeNaryTree, depth: int = 1) -> int:
    """Returns max depth of N-ary tree"""
    if not tree.children:
        return depth

    return max(max_depth(child, depth+1) for child in tree.children)


def main() -> None:
    """Main function"""
    tree = build_nary_tree([
        4, [
            [3, [7]],
            9,
            [2, [2]],
        ]
    ])
    print(max_depth(tree))


if __name__ == "__main__":
    main()
