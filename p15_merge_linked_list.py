"""
Given two sorted linked lists, merge them together in ascending order
and return a reference to the merged list

Ex: Given the following lists...

list1 = 1->2->3, list2 = 4->5->6->null, return 1->2->3->4->5->6->null
list1 = 1->3->5, list2 = 2->4->6->null, return 1->2->3->4->5->6->null
list1 = 4->4->7, list2 = 1->5->6->null, return 1->4->4->5->6->7->null
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


def main():
    """Main Function"""
    list1 = create_node_list([1, 2, 3])
    # list1 = create_node_list([1, 3, 5])
    # list1 = create_node_list([4, 4, 7])
    list1.print()
    list2 = create_node_list([4, 5, 6])
    # list2 = create_node_list([2, 4, 6])
    # list2 = create_node_list([1, 5, 6])
    list2.print()

    list3 = list1 + list2
    list3.print()


if __name__ == "__main__":
    main()
