"""
Given a linked list and a value n, remove the nth to last node and
return the resulting list.

Ex: Given the following linked lists...

1->2->3->null, n = 1, return 1->2->null
1->2->3->null, n = 2, return 1->3->null
1->2->3->null, n = 3, return 2->3->null
"""

from typing import List


class NodeList:
    """Linked List implementation"""

    def __init__(self, value: int, _next=None) -> None:
        self.value = value
        self.next = _next

    def print(self) -> None:
        """Prints the list"""
        node = self
        while node is not None:
            print(node.value, end='->')
            node = node.next
        print('null')

    def __add__(self, other):
        """Merge two linked lists"""
        node1, node2 = self, other
        new_list = None
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


def create_node_list(values: List[int]) -> NodeList:
    """Creates a NodeList out of a list of values"""
    head = NodeList(values[0])

    last_node = head
    for value in values[1:]:
        node = NodeList(value)
        last_node.next = node
        last_node = node

    return head


def remove_nth_to_last_node(head: NodeList, num: int) -> NodeList:
    """Removes Nth to last node from linked list"""
    tail = head
    queue: List[NodeList] = []
    while tail is not None:
        queue.append(tail)
        tail = tail.next
        # We only care about the last N+1 elements
        if len(queue) > num + 1:
            queue.pop(0)

    # Edge case:
    if num == len(queue):
        return head.next

    # Now, queue[0] is N+1th from last,
    # queue[1] ia Nth from last and so on
    # We want N+1th node to point to N-1th node,
    # so that Nth node is removed from the link
    if len(queue) <= 2:
        queue[0].next = None
    else:
        queue[0].next = queue[2]

    return head


def main() -> None:
    """Main Function"""
    node_list = create_node_list([1, 2, 3])

    node_list = remove_nth_to_last_node(node_list, 1)
    # node_list = remove_nth_to_last_node(node_list, 2)
    # node_list = remove_nth_to_last_node(node_list, 3)

    node_list.print()


if __name__ == "__main__":
    main()
