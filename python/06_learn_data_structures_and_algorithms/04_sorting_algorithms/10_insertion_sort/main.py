"""
Assignment
Our influencers want to sort their affiliate deals by revenue. 
None of our users have more than a couple hundred affiliate deals, so we don't need an n * log(n) algorithm like merge sort. 
In fact, insertion_sort can be faster than merge_sort, and uses less of our server's memory.

Complete the insertion_sort function according to the given pseudocode:

1. For each index in the input list, starting with the second element:
    1. Set a j variable to the current index
    2. While j is greater than 0 and the element at index j-1 is greater than the element at index j:
        1. Swap the elements at indices j and j-1
        2. Decrement j by 1
2. Return the list
"""

def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums
