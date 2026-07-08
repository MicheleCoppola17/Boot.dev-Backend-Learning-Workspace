"""
Assignment
Now that we can add users to our BST, our systems team wants us to start implementing search functionality.

Implement the get_min and get_max methods. They should return the minimum and maximum values in the BST respectively.
"""

from typing import Any


class BSTNode:
    # My implementation. I used recursion.
    """
    def get_min(self) -> Any:
        if self.left:
            return self.left.get_min()
        return self.val

    def get_max(self) -> Any:
        if self.right:
            return self.right.get_max()
        return self.val
    """

    # Boot.dev's implementation. Iterative.
    def get_min(self) -> Any:
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self) -> Any:
        current = self
        while current.right is not None:
            current = current.right
        return current.val
    
    # don't touch below this line

    def __init__(self, val: Any = None) -> None:
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
        self.val = val

    def insert(self, val: Any) -> None:
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
