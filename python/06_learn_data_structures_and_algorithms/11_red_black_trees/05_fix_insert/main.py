"""
Assignment
In our implementation, we'll perform a "normal" insert, and then call a fix_insert method that will recolor and rotate the tree as necessary. 
This will ensure that the red-black properties are maintained.

1. Complete the insert method to call our balancing method after inserting a new node.
2. Complete the fix_insert method that maintains red-black tree properties, starting with the newly inserted node as the current node:
    1. While the current node is not the root and has a red parent:
        1. Identify the parent and grandparent nodes of the current node
        2. If the parent is a right child of the grandparent:
            1. Identify the uncle node (the grandparent's left child)
            2. If the uncle is red:
                - Recolor the uncle and parent to black
                - Recolor the grandparent to red
                - Move up the tree by making the current node the grandparent
            3. If the uncle is black:
                - If the current node is the left child of the parent:
                    - Move up the tree by making the current node the parent
                    - Call rotate_right with the current node as the pivot_parent
                    - Set the parent to be the current node's parent
                - Recolor the parent to black
                - Recolor the grandparent to red
                - Call rotate_left with the grandparent as the pivot_parent
        3. If the parent is a left child of the grandparent:
            1. Identify the uncle node (the grandparent's right child)
            2. If the uncle is red:
                - Recolor the uncle and parent to black
                - Recolor the grandparent to red
                - Move up the tree by making the current node the grandparent
            3. If the uncle is black:
                - If the current node is the right child of the parent:
                    - Move up the tree by making the current node the parent
                    - Call rotate_left with the current node as the pivot_parent
                    - Set the parent to be the current node's parent
                - Recolor the parent to black
                - Recolor the grandparent to red
                - Call rotate_right with the grandparent as the pivot_parent
    2. Recolor the root to black
"""

from typing import Any


class RBNode:
    def __init__(self, val: Any) -> None:
        self.red = False
        self.parent: "RBNode | None" = None
        self.val = val
        self.left: "RBNode" = self
        self.right: "RBNode" = self


class RBTree:
    def __init__(self) -> None:
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.root = self.nil

    def insert(self, val: Any) -> None:
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent: RBNode | None = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate, just ignore
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, new_node: RBNode) -> None:
        while new_node != self.root and new_node.parent.red == True:
            parent = new_node.parent
            grandparent = parent.parent

            if grandparent.right == parent:
                uncle = grandparent.left
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    new_node = grandparent
                else:
                    if parent.left == new_node:
                        new_node = parent
                        self.rotate_right(new_node)
                        parent = new_node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_left(grandparent)
            elif grandparent.left == parent:
                uncle = grandparent.right
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    new_node = grandparent
                else:
                    if parent.right == new_node:
                        new_node = parent
                        self.rotate_left(new_node)
                        parent = new_node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)
        self.root.red = False
            

    def exists(self, val: Any) -> RBNode:
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def rotate_left(self, pivot_parent: RBNode) -> None:
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent: RBNode) -> None:
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        else:
            pivot_parent.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot
