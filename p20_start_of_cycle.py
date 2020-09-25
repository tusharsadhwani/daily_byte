"""
Given a potentially cyclical linked list where each value is unique,
return the node at which the cycle starts. If the list does not contain
a cycle, return null.

Ex: Given the following linked lists...

1->2->3, return null
1->2->3->4->5->2 (5 points back to 2), return a reference to the node containing 2
1->9->3->7->7 (7 points to itself), return a reference to the node containing 7
"""

from typing import Dict, Optional, Sequence

from data_types.node_list import NodeList


def start_of_cycle(node_list: NodeList) -> Optional[NodeList]:
    """
    Uses Floyd's algorithm to find if the list contains a cycle, and
    returns the node at which the cycle starts
    """
    turtle = node_list
    hare: Optional[NodeList] = node_list
    while hare is not None:
        # Move turtle ahead 1 step
        if turtle.next is not None:
            turtle = turtle.next

        # Move hare ahead 2 steps
        hare = hare.next
        if hare is not None:
            hare = hare.next

        if hare == turtle:
            # We have now reached the meeting point, which means there
            # is a cycle. Floyd's algorithm says that if you were to
            # move two pointers ahead at the same rate, one from the
            # start of the list and another from the meeting point, the
            # node at which they end up is the start of the cycle.
            meeting_point = hare
            node1, node2 = node_list, meeting_point
            while node1 != node2:
                assert node1.next is not None and node2.next is not None
                node1 = node1.next
                node2 = node2.next
            # As soon as node1 == node2, start of cycle has been found
            return node1

    return None


def create_linked_list_unique_items(items: Sequence[int]):
    """
    Creates a linked list out of items, whose values when repeated,
    refer to the previously existing node in the list.
    """
    head = NodeList(items[0])
    node = head
    nodes: Dict[int, NodeList] = {items[0]: head}

    for item in items[1:]:
        if item in nodes:
            node.next = nodes[item]
        else:
            new_node = NodeList(item)
            nodes[item] = new_node
            node.next = new_node

        node = node.next

    return head


def main():
    """Main function"""
    nums = [1, 2, 3]
    # nums = [1, 2, 3, 4, 5, 2]
    # nums = [1, 9, 3, 7, 7]

    node_list = create_linked_list_unique_items(nums)
    start_node = start_of_cycle(node_list)
    if start_node is None:
        print('null')
    else:
        print(start_node.value)


if __name__ == "__main__":
    main()
