"""
Assignment
1. Complete the peek method. It should return the top item from the stack without modifying the stack. If the stack is empty, return None.
2. Complete the pop method. It should remove and return the top item from the stack. If the stack is empty, return None.
"""

from typing import Any


class Stack:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> Any:
        if len(self.items) != 0:
            return self.items[-1]
        return None

    def pop(self) -> Any:
        if len(self.items) != 0:
            return self.items.pop()
        return None