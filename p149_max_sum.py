r"""
Given the reference to a binary tree, return the maximum path sum.

Note: The path that creates the maximum sum does not need to pass
through the root of the tree.

Ex: Given the reference to the following binary tree...

      1
     / \
    4   9

return 14.
"""
# TODO: incomplete
from typing import Callable, Generator, TypeVar
from data_types.node_tree import NodeTree, build_tree


T = TypeVar('T')


def x(node: NodeTree) -> int:
    return node.value


def call_postorder(tree: NodeTree, callback: Callable[..., T]) -> Generator[T, None, None]:
    """Calls the given function in postorder"""
    if tree.left is not None:
        yield from call_postorder(tree.left, callback)
    if tree.right is not None:
        yield from call_postorder(tree.right, callback)

    yield callback(tree)


def max_sum(tree: NodeTree) -> int:
    """Find maximum"""
    max_value = 0
    for value in call_postorder(tree, x):
        if value > max_value:
            max_value = value

    return max_value


def main() -> None:
    """Main function"""
    tree = build_tree([1, [5, 1, None], [4, 9, 9]])

    print(max_sum(tree))


if __name__ == '__main__':
    main()
