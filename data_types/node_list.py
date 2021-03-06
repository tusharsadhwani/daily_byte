"""Standard singly linked list implementation"""
from __future__ import annotations
from typing import Optional


class NodeList:
    """Linked List implementation"""

    def __init__(self, value: int, _next: Optional[NodeList] = None) -> None:
        self.value = value
        self.next = _next

        self.iternode: Optional[NodeList] = self

    def __iter__(self) -> NodeList:
        self.iternode = self
        return self

    def __next__(self) -> int:
        if self.iternode is None:
            raise StopIteration

        node = self.iternode
        self.iternode = self.iternode.next
        return node.value

    def __repr__(self) -> str:
        return f'NodeList(value={self.value})'

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


def create_node_list(values: list[int]) -> NodeList:
    """Creates a NodeList out of a list of values"""
    head = NodeList(values[0])

    last_node = head
    for value in values[1:]:
        node = NodeList(value)
        last_node.next = node
        last_node = node

    return head


def create_node_list_unique_items(items: list[int]) -> NodeList:
    """
    Creates a linked list out of items, whose values when repeated,
    refer to the previously existing node in the list.
    """
    head = NodeList(items[0])
    node = head
    nodes: dict[int, NodeList] = {items[0]: head}

    for item in items[1:]:
        if item in nodes:
            node.next = nodes[item]
            assert item is items[-1], 'Node pointing to previous value must be last node of list'
            return head

        new_node = NodeList(item)
        nodes[item] = new_node
        node.next = new_node

        node = node.next

    return head


def reverse_node_list(head: NodeList) -> NodeList:
    """Reverses given linked list. Destroys original list."""
    start_node = head
    prev_node, curr_node = start_node, start_node.next

    while curr_node is not None:
        temp = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = temp
    last_node = prev_node

    start_node.next = None
    return last_node
