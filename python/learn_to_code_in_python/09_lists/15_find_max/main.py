"""
Assignment:
Our players want a way to see their strongest attack from their last combat. Some enemies may be buffed to absorb either magic or melee attacks as health, which result in negative damage. Let's add another function to analyze data from our combat log.

Complete the find_max function. It takes as input a list of integers, nums, and returns an integer.

1. max_so_far is initialized as negative infinity.
2. Compare each number in nums to max_so_far. If any number is larger than max_so_far, replace max_so_far with that value.
3. Return max_so_far. If nums is empty, return negative infinity.

Here's an example of how your find_max function should work:

max_val = find_max([100, 10, 22])
print(max_val)
# 100
"""

def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far
