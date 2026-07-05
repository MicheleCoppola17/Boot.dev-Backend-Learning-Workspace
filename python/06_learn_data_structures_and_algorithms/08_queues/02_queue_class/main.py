"""
Assignment
LockedIn uses a Queue to keep track of the order that recruiters should use to reach out to job seekers.

Implement the following operations on the Queue class:

- queue.push(item): Adds an item to the tail of the queue (index 0 of list)
- queue.pop(): Removes and returns an item from the head of the queue (last index of list)
- queue.peek(): Returns an item from the head of the queue
- queue.size(): Returns the number of items in the queue
Note: You'll often hear words used interchangeably in programming. For example, here we're saying push and pop, but enqueue and dequeue are also common words for the same ideas.

term 1	| term 2	 | description
Push	| Enqueue	 | Adds an item to the tail of the queue
Pop	    | Dequeue	 | Removes and returns an item from the head of the queue
"""

from typing import Any


class Queue:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        self.items.insert(0, item)

    def pop(self) -> Any:
        if len(self.items) != 0:
            return self.items.pop()

    def peek(self) -> Any:
        if len(self.items) != 0:
            return self.items[-1]

    def size(self) -> int:
        return len(self.items)