"""
Assignment
Complete the insert method of the BSTNode class. It takes a User object as input and adds it to a new node if the value doesn't already exist in the tree.

1. If the node doesn't have a value yet, store the given value and return
2. If the node's value is equal to the given value, just return, no duplicates allowed
3. If the given value is less than the node's value and the node doesn't have a left child, create a new left child node with the given value and return
4. If the given value is less than the node's value and the node does have a left child, recursively call insert off of that left child with the given value and return
5. Since we already checked if the given value is equal to or less than the node, the value must be greater than the node. Handle whether or not the node already has a right
"""

from typing import Any


class BSTNode:
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
            
