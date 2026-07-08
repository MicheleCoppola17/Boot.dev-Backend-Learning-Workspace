"""
Assignment
Let's lock-in and make LockedIn faster!

1. Complete the Node's constructor.
    1. Set its val field to the provided value.
    2. Set its next field to None.
2. Complete the Node's set_next method. It should set the next field to the provided node.
"""

from typing import Any


class Node:
    val: Any

    def __init__(self, val: Any) -> None:
        self.val = val
        self.next = None

    def set_next(self, node: "Node") -> None:
        self.next = node

    # don't touch below this line

    def __repr__(self) -> str:
        return self.val