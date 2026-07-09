"""
Assignment
Now that we can add users to our new Red Black Tree, we need to add the rotation functionality that will keep it balanced and running fast!

Use the exact same variables as specified in the instructions. 
For example, pivot_parent and pivot.parent are not interchangeable as they hold state that changes throughout the algorithm's steps.

1. Complete the rotate_left method. It takes a single node, pivot_parent, as input and rotates the tree with its pivot node – which in this case is its right child.
    1. If pivot_parent is nil or pivot_parent's right child is nil, return. Nothing to do here.
    2. Let pivot be pivot_parent's right child.
    3. Set pivot_parent's right child to be pivot's left child.
    4. If pivot's left child isn't a nil leaf node, set pivot's left child's parent to pivot_parent.
    5. Set pivot's parent to pivot_parent's parent.
    6. If pivot_parent is the root, set the root to pivot.
        1. Otherwise, if pivot_parent is its parent's left child, set pivot_parent's parent's left child to pivot.
        2. Otherwise, if pivot_parent is its parent's right child, set pivot_parent's parent's right child to pivot.
    7. Set pivot's left child to be pivot_parent.
    8. Set pivot_parent's parent to be pivot.
2. Complete the rotate_right method with all the directionality inverted.
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

    def rotate_left(self, pivot_parent: RBNode) -> None:
        # 1. If pivot_parent is nil or pivot_parent's right child is nil, return.
        # Nothing to do here.
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        
        # 2. Let pivot be pivot_parent's right child.
        pivot = pivot_parent.right

        # 3. Set pivot_parent's right child to be pivot's left child.
        pivot_parent.right = pivot.left

        # 4. If pivot's left child isn't a nil leaf node,
        # set pivot's left child's parent to pivot_parent.
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent

        # 5. Set pivot's parent to pivot_parent's parent.
        pivot.parent = pivot_parent.parent

        # 6. If pivot_parent is the root, set the root to pivot.
        if pivot_parent.parent is None:
            self.root = pivot
        else:
            # 6.1. Otherwise, if pivot_parent is its parent's left child,
             # set pivot_parent's parent's left child to pivot.
            if pivot_parent == pivot_parent.parent.left:
                pivot_parent.parent.left = pivot
            # 6.2. Otherwise, if pivot_parent is its parent's right child,
            # set pivot_parent's parent's right child to pivot.
            else:
                pivot_parent.parent.right = pivot

        # 7. Set pivot's left child to be pivot_parent.
        pivot.left = pivot_parent

        # 8. Set pivot_parent's parent to be pivot.
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent: RBNode) -> None:
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        
        pivot = pivot_parent.left

        pivot_parent.left = pivot.right

        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent

        pivot.parent = pivot_parent.parent

        if pivot_parent is None:
            self.root = pivot
        else:
            if pivot_parent == pivot_parent.parent.right:
                pivot_parent.parent.right = pivot
            else:
                pivot_parent.parent.left = pivot

        pivot.right = pivot_parent

        pivot_parent.parent = pivot

        # don't touch below this line

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
