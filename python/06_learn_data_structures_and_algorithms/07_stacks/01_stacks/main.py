"""
Assignment
In this chapter we'll build a stack from scratch! A stack will be useful at LockedIn when we need undo/redo functionality. For example, a user can add other users to their "connections" list, and then undo the last connection they added. Stacks are a great way to implement undo functionality.

For now, we'll just focus on two methods: push and size. Notice that the Stack class already has a constructor and the underlying List that we'll use to store items.

1. Complete the push method. It should add an item to the top of the stack. The "top" of the stack is the end of the list in our implementation.
2. Complete the size method. It should return the number of items in the stack.
"""

from typing import Any


class Stack:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)
