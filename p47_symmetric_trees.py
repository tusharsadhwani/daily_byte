r"""
Given a binary tree, return whether or not it forms a reflection across
its center (i.e. a line drawn straight down starting from the root).

Note: a reflection is when an image, flipped across a specified line,
forms the same image.

Ex: Given the following tree...

      2
     / \
    1   1

return true as when the tree is reflected across its center all the
nodes match.

Ex: Given the following tree...

      1
     / \
    5   5
     \   \
      7   7

return false as when the tree is reflected across its center the nodes
containing sevens do not match.
"""
from data_types.node_tree import NodeTree, build_tree


def create_inverted_tree(tree: NodeTree) -> NodeTree:
    """Creates an left-right inverted version of a binary tree"""
    inverted_tree = NodeTree(tree.value)

    if tree.left is not None:
        inverted_tree.right = create_inverted_tree(tree.left)

    if tree.right is not None:
        inverted_tree.left = create_inverted_tree(tree.right)

    return inverted_tree


def main() -> None:
    """Main function"""
    tree = build_tree([2, 1, 1])
    # tree = build_tree([1, [5, None, 7], [5, None, 7]])

    inverted_tree = create_inverted_tree(tree)
    print(tree == inverted_tree)


if __name__ == "__main__":
    main()
