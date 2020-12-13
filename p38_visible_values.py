r"""
Given a binary tree return all the values you’d be able to see if you
were standing on the left side of it with values ordered from top to
bottom.

Ex: Given the following tree...

      4
     / \
    2   7

return [4, 2]

Ex: Given the following tree...

         7
        / \
      4     9
     / \   / \
    1   4 8   9
               \
                9

return [7, 4, 1, 9]
"""
from data_types.node_tree import build_tree, level_order_traversal


def main() -> None:
    """Main function"""
    tree = build_tree([4, 2, 7])
    # tree = build_tree([7, [4, 1, 4], [9, 8, [9, None, 9]]])

    levels = level_order_traversal(tree)
    print([level[0] for level in levels])


if __name__ == "__main__":
    main()
