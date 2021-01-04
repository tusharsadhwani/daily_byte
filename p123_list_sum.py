"""
Given two linked lists that represent two numbers, return the sum of the
numbers also represented as a list.

Ex: Given the two linked lists...

a = 1->2, b = 1->3, return a list that looks as follows: 2->5

Ex: Given the two linked lists...

a = 1->9, b = 1, return a list that looks as follows: 2->0
"""
from itertools import zip_longest

from data_types.node_list import NodeList, create_node_list, reverse_node_list


def list_sum(list1: NodeList, list2: NodeList) -> NodeList:
    """Adds two node lists like integer addition"""
    list1 = reverse_node_list(list1)
    list2 = reverse_node_list(list2)

    new_list = NodeList(0)
    node = new_list
    carry = 0

    first_value = True
    for val1, val2 in zip_longest(list1, list2, fillvalue=0):
        if not first_value:
            node.next = NodeList(0)
            node = node.next
        else:
            first_value = False

        _sum = val1 + val2 + carry
        node.value = _sum % 10
        carry = _sum // 10

    node.next = None

    return reverse_node_list(new_list)


def main() -> None:
    """Main function"""
    list1 = create_node_list([1, 2])
    list2 = create_node_list([1, 3])
    # list1 = create_node_list([1, 9])
    # list2 = create_node_list([1])

    list_sum(list1, list2).print()


if __name__ == "__main__":
    main()
