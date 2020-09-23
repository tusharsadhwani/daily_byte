"""
Given a linked list and a value, remove all nodes containing the
provided value, and return the resulting list.

Ex: Given the following linked lists and values...

1->2->3->null, value = 3, return 1->2->null
8->1->1->4->12->null, value = 1, return 8->4->12->null
7->12->2->9->null, value = 7, return 12->2->9->null
"""
from data_types.node_list import NodeList, create_node_list


def remove_value(node_list: NodeList, value: int) -> NodeList:
    """Removes any instance of given value from the linked list"""
    head = node_list

    while head.value == value:
        if head.next is None:
            raise ValueError('No values left in linked list')

        head = head.next

    prev_node = head
    node = prev_node.next
    while node is not None:
        if node.value == value:
            prev_node.next = node.next
            node = node.next

        if node is not None:
            prev_node = node
            node = node.next

    return head


def main() -> None:
    """Main function"""
    node_list, value = create_node_list([1, 2, 3]), 3
    # node_list, value = create_node_list([8, 1, 1, 4, 12]), 1
    # node_list, value = create_node_list([7, 12, 2, 9]), 7

    node_list = remove_value(node_list, value)
    node_list.print()


if __name__ == "__main__":
    main()
