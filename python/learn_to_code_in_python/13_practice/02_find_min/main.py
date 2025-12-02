"""
Assignment:
Write a function called find_min() that finds the smallest number in a list. For example:

- find_min([1, 3, -1, 2]) -> -1
- find_min([18, 3, 7, 2]) -> 2

Do not use the built-in min() function.
"""

def find_min(nums):
    min_number = float("inf")
    
    for number in nums:
        if number < min_number:
            min_number = number
    
    return min_number

