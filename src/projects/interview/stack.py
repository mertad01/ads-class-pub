#!/usr/bin/env python3
"""
`stack` implementation

@authors: Adam Mertzenich
@version: 2021.4
"""

from queue import SimpleQueue
from typing import Any


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)


class Stack:
    """
    LIFO data structure

    Items are added and removed on the same end of the collection
    """

    def __init__(self):
        """Initialize a stack using queue.SimpleQueue"""
        self.items = SimpleQueue()

    def push(self, item: Any) -> None:
        """
        Add a new item to stack

        @param item: a new item to push onto the stack
        """
        self.items.put(item)

    def pop(self) -> Any:
        """
        Remove an item from the stack

        @return the top element of the stack
        @raise StackError is the stack is empty
        """
        if self.items.empty():
            raise StackError("Cannot pop from an empty stack")

        worker: list = []
        while not self.items.empty():
            worker.append(self.items.get())
        output = worker.pop()
        for i in worker:
            self.items.put(i)
        return output

    def peek(self) -> Any:
        """
        Look at the top item without removing it

        @return the top element of the stack
        @raise StackError is the stack is empty
        """
        if self.items.empty():
            raise StackError("Nothing to see here, the stack is empty")
        output = self.pop()
        self.push(output)
        return output

    def __bool__(self) -> bool:
        """
        Evaluate the stack

        @return False if the stack is empty, True otherwise
        """
        return bool(self.__len__())

    def __len__(self) -> int:
        """
        Return the number of items in the stack

        @return number of items in the stack (0 if the stack is empty)
        """
        return self.items.qsize()


def main():
    """Main"""
    the_stack = Stack()
    the_stack.push("First")
    the_stack.push("Second")
    the_stack.push({1, 2, 3, 4, 5})
    print(the_stack.pop())
    the_stack.push([True, False, True, True])
    print(the_stack.pop())
    print(the_stack.pop())
    print(the_stack.pop())


if __name__ == "__main__":
    main()
