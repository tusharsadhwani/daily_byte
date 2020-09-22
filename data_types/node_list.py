"""Standard singly linked list implementation"""
from __future__ import annotations
from typing import List, Optional


class NodeList:
    """Linked List implementation"""

    def __init__(self, value: int, _next: Optional[NodeList] = None) -> None:
        self.value = value
        self.next = _next

    def __add__(self, other: NodeList) -> NodeList:
        """Merge two linked lists"""
        node1: Optional[NodeList] = self
        node2: Optional[NodeList] = other
        assert node1 is not None and node2 is not None

        smaller_node = node1 if node1.value < node2.value else node2
        if smaller_node is node1:
            new_list = node1
            node1 = node1.next
        else:
            new_list = node2
            node2 = node2.next

        node = new_list

        while node1 is not None and node2 is not None:
            smaller_node = node1 if node1.value < node2.value else node2
            if not new_list:
                new_list = smaller_node
                node = new_list
            else:
                node.next = smaller_node
                node = node.next

            if smaller_node is node1:
                node1 = node1.next
            else:
                node2 = node2.next

        while node1 is not None:
            node.next = node1
            node = node.next
            node1 = node1.next

        while node2 is not None:
            node.next = node2
            node = node.next
            node2 = node2.next

        return new_list

    def print(self) -> None:
        """Prints the list"""
        node = self
        while node.next is not None:
            print(node.value, end='->')
            node = node.next
        print(f'{node.value}->null')


def create_node_list(values: List[int]) -> NodeList:
    """Creates a NodeList out of a list of values"""
    head = NodeList(values[0])

    last_node = head
    for value in values[1:]:
        node = NodeList(value)
        last_node.next = node
        last_node = node

    return head
