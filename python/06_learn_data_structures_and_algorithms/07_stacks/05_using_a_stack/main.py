"""
Balanced Parentheses
Parentheses are balanced when each parenthesis has a corresponding parenthesis, and the pairs of parentheses are properly nested. 
For example:

()
()()
((()))
(()(()))
Unbalanced Parentheses
(
())
(()()
(()))
)(

Assignment
Complete the is_balanced function.

It takes a string as input and returns True if the parentheses in the string are balanced, and False otherwise. Use an instance of the provided Stack class in stack.py to keep track of the parentheses.

If the parentheses are balanced, then the stack should be empty.
You only need to consider the characters ( and ) for this challenge.
"""

from stack import Stack


def is_balanced(input_str: str) -> bool:
    stack = Stack()
    for char in input_str:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.size() == 0:
                return False
            else:
                stack.pop()
    return stack.size() == 0

