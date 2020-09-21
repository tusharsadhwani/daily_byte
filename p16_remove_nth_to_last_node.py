"""
Given a linked list and a value n, remove the nth to last node and
return the resulting list.

Ex: Given the following linked lists...

1->2->3->null, n = 1, return 1->2->null
1->2->3->null, n = 2, return 1->3->null
1->2->3->null, n = 3, return 2->3->null
"""

from typing import List

from data_types.node_list import NodeList, create_node_list


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
