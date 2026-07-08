"""
Assignment
Complete the remove_from_head method. It should remove the first node from the list (the head) and return it.

1. If the list is empty, just return None.
2. Assign the head to be removed to a variable.
3. Set the list's head to the next node in the list.
4. If the list became empty, set the list's tail to None.
5. Detach the removed head by setting its next to None.
6. Return the removed head.
"""

from node import Node


class LLQueue:
    def remove_from_head(self) -> Node | None:
        if self.head is None:
            return None
        head_to_remove = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        head_to_remove.set_next(None)
        return head_to_remove

    # don't touch below this line

    def add_to_tail(self, node: Node) -> None:
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        assert self.tail is not None
        self.tail.set_next(node)
        self.tail = node

    def __init__(self) -> None:
        self.tail: Node | None = None
        self.head: Node | None = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)
