"""
Given a linked list, containing unique values, reverse it, and return
the result.

Ex: Given the following linked lists...

1->2->3->null, return a reference to the node that contains 3 which
    points to a list that looks like the following: 3->2->1->null
7->15->9->2->null, return a reference to the node that contains 2 which
    points to a list that looks like the following: 2->9->15->7->null
1->null, return a reference to the node that contains 1 which points to
    a list that looks like the following: 1->null
"""
from data_types.node_list import NodeList, create_node_list


def reverse_list(node_list: NodeList) -> NodeList:
    """Reverse the linked list and return the new head"""
    head = node_list
    prev_node, node = head, head.next

    while node is not None:
        node.next, prev_node, node = prev_node, node, node.next

    last_node = prev_node
    head.next = None

    return last_node


def main() -> None:
    """Main Function"""
    node_list = create_node_list([1, 2, 3])
    # node_list = create_node_list([7, 15, 9, 2])
    # node_list = create_node_list([1])

    node_list = reverse_list(node_list)
    node_list.print()


if __name__ == "__main__":
    main()
