"""
Given a singly linked list, re-order and group its nodes in such a way
that the nodes in odd positions come first and the nodes in even
positions come last.

Ex: Given the reference to the following linked list...

4->7->5->6->3->2->1->NULL, return 4->5->3->1->7->6->2->NULL
Ex: Given the reference to the following linked list...

1->2->3->4->5->NULL, return 1->3->5->2->4->NULL
"""
from typing import Optional

from data_types.node_list import NodeList, create_node_list


def odd_even(head: NodeList) -> None:
    """Puts all odd nodes before even nodes in linked list"""
    odd_start = head
    even_start = head.next

    last_odd_node = odd_start

    odd_node: Optional[NodeList] = odd_start
    even_node: Optional[NodeList]

    while odd_node is not None:
        last_odd_node = odd_node

        if odd_node.next is None:
            odd_node = None
            break

        even_node = odd_node.next

        next_odd_node = odd_node.next.next
        odd_node.next = next_odd_node
        odd_node = next_odd_node

        if even_node.next is None:
            even_node = None
            break

        next_even_node = even_node.next.next
        even_node.next = next_even_node
        even_node = next_even_node

    last_odd_node.next = even_start


def main() -> None:
    """Main function"""
    head = create_node_list([4, 7, 5, 6, 3, 2, 1])
    # head = create_node_list([1, 2, 3, 4, 5])

    odd_even(head)
    head.print()


if __name__ == "__main__":
    main()
