"""
Assignment
Complete the exists method.

It should take a value as input and return True if the value exists in the tree, and False if it doesn't. 
It's a recursive method, as you probably guessed.
"""

from typing import Any


class BSTNode:
    def exists(self, val: Any) -> bool:
        if not self.val:
            return False
        
        if val == self.val:
            return True

        if val < self.val:
            if self.left:
                return self.left.exists(val)
            return False
        
        if val > self.val:
            if self.right:
                return self.right.exists(val)
            return False


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
