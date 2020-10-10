r"""
Given a binary search tree, return its mode (you may assume the answer
is unique). If the tree is empty, return -1.

Note: the mode is the most frequently occurring value in the tree.

Ex: Given the following tree...

      2
     / \
    1   2

return 2.

Ex: Given the following tree...

         7
       /   \
      4     9
     / \   / \
    1   4 8   9
               \
                9

return 9.
"""

from typing import Optional

from data_types.node_tree import build_tree


def main() -> None:
    """Main function"""
    bst = build_tree([2, 1, 2])
    # bst = build_tree([7, [4, 1, 4], [9, 8, [9, None, 9]]])

    max_count = 0
    max_value = -1
    last_value: Optional[int] = None
    for node in bst:
        if last_value != node.value:
            last_value = node.value
            count = 1
        else:
            count += 1

        if count > max_count:
            max_count = count
            max_value = node.value

    print(max_value)


if __name__ == "__main__":
    main()
