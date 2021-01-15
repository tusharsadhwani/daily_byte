"""
Design a class to implement a stack using only a single queue.
Your class, QueueStack, should support the following stack methods:
push() (adding an item),
pop() (removing an item),
peek() (returning the top value without removing it), and
empty() (whether or not the stack is empty).
"""
from typing import Iterator
from data_types.node_list import NodeList, create_node_list


class Queue:
    """Simple Queue"""

    def __init__(self, values: list[int]) -> None:
        self.head = create_node_list(values)

        temp_node = self.head
        while temp_node.next is not None:
            temp_node = temp_node.next
        self.tail = temp_node

    def __iter__(self) -> NodeList:
        return self.head.__iter__()

    def insert(self, item: int) -> None:
        """Inserts an item into the queue"""
        new_node = NodeList(item)
        self.tail.next = new_node
        self.tail = new_node

    def delete(self) -> int:
        """Deletes an item from queue"""
        if self.head.next is None:
            raise Exception('Cannot empty the queue')

        head = self.head
        self.head = self.head.next
        return head.value


class QueueStack:
    """Implementing a stack using a queue"""

    def __init__(self, values: list[int]) -> None:
        self.queue = Queue(values)

    def __iter__(self) -> Iterator[int]:
        return self.queue.__iter__()

    def push(self, item: int) -> None:
        """Pushes an item onto the stack"""
        self.queue.insert(item)

    def pop(self) -> int:
        """Pops an item off the stack"""
        prev = self.queue.head
        if prev.next is None:
            raise Exception('Cannot empty the stack')
        curr = prev.next

        while curr.next is not None:
            prev = curr
            curr = curr.next

        prev.next = None
        # Since we are messing with the queue directly, we need to fix the tail
        self.queue.tail = prev
        return curr.value

    def peek(self) -> int:
        """Returns the top of the stack"""
        last = -1
        for value in self:
            last = value

        return last

    def empty(self) -> bool:
        """Return if the queue is empty"""
        return self.queue.head.value is not None


def main() -> None:
    """Main function"""
    stack = QueueStack([1, 2, 3])
    for value in stack:
        print(value)

    popped = stack.pop()
    print(popped)

    for value in stack:
        print(value)

    stack.push(4)
    print(stack.peek())

    for value in stack:
        print(value)


if __name__ == "__main__":
    main()
