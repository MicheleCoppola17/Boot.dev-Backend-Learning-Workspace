"""
Assignment:
Let's keep improving our inventory system. Complete the get_first_item function. It takes a list as input.

1. Return the first element from the items list.
2. If items is empty, return the string "ERROR" instead.
"""

def get_first_item(items):
    if len(items) == 0:
        return "ERROR"
    return items[0]
