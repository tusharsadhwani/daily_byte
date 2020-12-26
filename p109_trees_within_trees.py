r"""
Given two trees s and t return whether or not t is a subtree of s.
Note: For t to be a subtree of s not only must each node’s value in t
match its corresponding node’s value in s, but t must also exhibit the
exact same structure as s. You may assume both trees s and t exist.

Ex: Given the following trees s and t...

s = 1
   / \
  3   8

t = 1
     \
      8

return false

Ex: Given the following trees s and t...

s = 7
   / \
  8   3

t = 7
   / \
  8   3

return true

Ex: Given the following trees s and t...

s = 7
   / \
  8   3

t = 7
   / \
  8   3
     /
    1

return false
"""
from data_types.node_tree import NodeTree, build_tree


def is_subtree(tree: NodeTree, subtree: NodeTree) -> bool:
    """Returns if given subtree is a valid subtree"""
    if tree.value != subtree.value:
        return False

    left_subtree = True
    right_subtree = True

    if subtree.left:
        if tree.left is None:
            return False
        left_subtree = is_subtree(tree.left, subtree.left)

    if subtree.right:
        if tree.right is None:
            return False
        right_subtree = is_subtree(tree.right, subtree.right)

    return left_subtree and right_subtree


def main() -> None:
    """Main function"""
    tree = build_tree([1, 3, 8])
    subtree = build_tree([1, None, 8])
    # tree = build_tree([7, 8, 3])
    # subtree = build_tree([7, 8, 3])
    # tree = build_tree([7, 8, 3])
    # subtree = build_tree([7, 8, [3, 1, 1]])

    print(is_subtree(tree, subtree))


if __name__ == "__main__":
    main()
