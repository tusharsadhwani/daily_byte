"""
Given two sorted linked lists, merge them together in ascending order
and return a reference to the merged list

Ex: Given the following lists...

list1 = 1->2->3, list2 = 4->5->6->null, return 1->2->3->4->5->6->null
list1 = 1->3->5, list2 = 2->4->6->null, return 1->2->3->4->5->6->null
list1 = 4->4->7, list2 = 1->5->6->null, return 1->4->4->5->6->7->null
"""

from data_types.node_list import create_node_list


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
