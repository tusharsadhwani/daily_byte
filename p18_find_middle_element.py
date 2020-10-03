"""
Given a non-empty linked list, return the middle node of the list.
If the linked list contains an even number of elements, return the node
closer to the end.

1->2->3->null, return 2
1->2->3->4->null, return 3
1->null, return 1
"""
# Author's note: I could think of two solutions for this: a naive one
# (traversing twice), and one that would require a mapping that would
# store the last N/2 numbers in a list.
# Since I've already implemented one such mapping method in p16, and the
# fact that the naive one is also O(n) time but only takes constant
# space, I decided to go with the naive solution here.
import math

from data_types.node_list import NodeList, create_node_list


def find_moddle_element(node_list: NodeList) -> NodeList:
    """Finds the middle element in list and returns it"""
    element_count = 1
    node = node_list
    while node.next is not None:
        element_count += 1
        node = node.next

    node = node_list
    index = 1
    middle_index = math.ceil((1 + element_count) / 2)
    while node.next is not None and index < middle_index:
        index += 1
        node = node.next

    return node


def main() -> None:
    """Main function"""
    node_list = create_node_list([1, 2, 3])
    # node_list = create_node_list([1, 2, 3, 4])
    # node_list = create_node_list([1])

    middle_element = find_moddle_element(node_list)
    print(middle_element.value)


if __name__ == "__main__":
    main()
