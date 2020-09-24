"""
Given a linked list, containing unique numbers, return whether or not it
has a cycle. A cycle is a circular arrangement (i.e. one node
points back to a previous node)

Ex: Given the following linked lists...

1->2->3->1 -> true (3 points back to 1)
1->2->3 -> false
1->1 true (1 points to itself)
"""
from typing import Dict, Sequence

from data_types.node_list import NodeList


def contains_cycle(node_list: NodeList) -> bool:
    """Uses Floyd's algorithm to find if the list contains a cycle"""
    turtle, hare = node_list, node_list.next

    while hare is not None:
        if hare == turtle:
            return True

        # Move turtle ahead 1 step
        if turtle.next is not None:
            turtle = turtle.next

        # Move hare ahead 2 steps
        hare = hare.next
        if hare is not None:
            hare = hare.next

    return False


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
    nums = [1, 2, 3, 1]
    # nums = [1, 2, 3]
    # nums = [1, 1]

    node_list = create_linked_list_unique_items(nums)
    print(contains_cycle(node_list))


if __name__ == "__main__":
    main()
