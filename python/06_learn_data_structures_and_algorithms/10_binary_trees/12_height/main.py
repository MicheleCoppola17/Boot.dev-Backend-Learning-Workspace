"""
Assignment
Complete the height method. It returns the height of the tree rooted at the current node.

1. If the node's value is None, return 0.
2. Recursively calculate the height of the left subtree.
3. Recursively calculate the height of the right subtree.
4. Use the max() function to return the maximum of the left and right subtree heights plus 1.
"""

from typing import Any


class BSTNode:
    def height(self) -> int:
        left_height = 0
        right_height = 0
        if not self.val:
            return 0
        if self.left:
            left_height = self.left.height()
        if self.right:
            right_height = self.right.height()
        return max(left_height, right_height) + 1

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
