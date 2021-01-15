r"""
Given the reference to a binary search tree and a value to insert,
return a reference to the root of the tree after the value has been
inserted in a position that adheres to the invariants of a binary search
tree.

Note: It is guaranteed that each value in the tree, including the value
to be inserted, is unique.

Ex: Given the following tree and value...

      2
     / \
    1   3

value = 4, return the following tree...

      2
     / \
    1   3
         \
          4
"""
from typing import Optional
from data_types.node_tree import NodeTree


class NodeBST(NodeTree):
    """Standard Binary Search Tree implementation"""

    def __init__(self, value: int) -> None:
        super().__init__(value)
        self.left: Optional[NodeBST] = None
        self.right: Optional[NodeBST] = None

    def __repr__(self) -> str:
        return f'<NodeBST value={self.value}>'


def bst_insert(tree: NodeBST, value: int) -> None:
    """Inserts value into BST"""
    if tree.value > value:
        if tree.left is None:
            tree.left = NodeBST(value)
        else:
            bst_insert(tree.left, value)
    else:
        if tree.right is None:
            tree.right = NodeBST(value)
        else:
            bst_insert(tree.right, value)


def build_bst(values: list[int]) -> NodeBST:
    """Builds a binary search tree from given values"""
    if len(values) == 0:
        raise ValueError("Cannot create empty BST")

    tree = NodeBST(values[0])
    for value in values[1:]:
        bst_insert(tree, value)

    return tree


def main() -> None:
    """Main function"""
    bst = build_bst([2, 1, 3])
    bst_insert(bst, 4)
    bst.print_inorder()


if __name__ == "__main__":
    main()
