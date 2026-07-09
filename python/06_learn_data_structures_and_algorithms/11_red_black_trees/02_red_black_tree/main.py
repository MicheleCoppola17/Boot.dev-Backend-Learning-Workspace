"""
Assignment
As it turns out, we've been inserting user records into our tree with incrementing numerical IDs (pre sorted data)! 
The app's user lookups are starting to get really slow. Let's start implementing a Red-Black tree to speed things up.

In a normal BST, the child nodes don't need to know about, or carry a reference to their parent. 
The same is not true for Red-Black trees.

The RBNode class is already implemented for you, as well as the __init__ constructor method of the RBTree class.
There's also a data member, self.nil created for you in the constructor. 
self.nil contains the value we'll use to designate all the nil (empty) leaf nodes, which are used for rebalancing purposes but contain no "actual" value.

Complete the insert method. It should take a value as input and add the value as a new node in the tree if the value doesn't already exist.

1. Create the new_node:
    1. Create a new RBNode from the given input value
    2. The new_node shouldn't have a parent yet
    3. The new_node's left and right children should be nil
    4. The new_node is red. (new_node.red = True)
2. Find the parent of the new_node if there will be one:
    1. Initialize a parent variable to None
    2. Initialize a current variable to the root node of the tree
    3. While current isn't a nil node:
        1. Set parent to the current
        2. If the new_node's value is less than the current node's, set current to its own left child. If new_node's value is greater, set current to its own right child. If the values are equal, just return because this value is a duplicate.
    4. If you followed the steps correctly, parent will be a reference to the node that will become the parent of the new_node
3. Insert the new_node by setting the parent's child:
    1. Set the new_node's parent to the parent we just found
    2. If the parent is None, we are dealing with a new root, so set the tree's root data member to the new_node
    3. Otherwise, compare the values of the parent and new_node and set the parent's left or right child based on the results

We're done for now! We've really just made another (more complicated) regular binary tree, seeing as it's not a fully-fledged red-black tree yet... but these upgrades will allow us to implement the rest of the logic in the next few lessons.

So far we've added:

a parent pointer from child to parent (so children know who their parents are)
the mechanisms for coloring the nodes, but have defaulted them all to red for now
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
        
        while current is not self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return
        new_node.parent = parent
        if not parent:
            self.root = new_node
        if new_node.val > parent.val:
            parent.right = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
