r"""
Given two binary trees, return whether or not they are identical.

Note: identical meaning they exhibit the same structure and the same
values at each node. Ex: Given the following trees...

          2
         / \
        1   3

      2
     / \
    1   3

return true.

Ex: Given the following trees...

        1
         \
          9
           \
           18

    1
   /
  9
   \
    18

return false.

Ex: Given the following trees...

          2
         / \
        3   1

      2
     / \
    1   3

return false.
"""
from data_types.node_tree import build_tree


def main() -> None:
    """Main function"""
    items_a = [2, 1, 3]
    items_b = [2, 1, 3]

    # items_a = [1, None, [9, None, 18]]
    # items_b = [1, [9, None, 18], None]

    # items_a = [2, 3, 1]
    # items_b = [2, 1, 3]

    tree_a = build_tree(items_a)
    tree_b = build_tree(items_b)

    print(tree_a == tree_b)


if __name__ == "__main__":
    main()
