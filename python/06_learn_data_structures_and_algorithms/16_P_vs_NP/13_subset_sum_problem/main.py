"""
Assignment
Complete the subset_sum function.

It should take a list of integers nums and an integer target, and return True if there exists a subset of nums that adds up to target, and False otherwise. 
We'll use a recursive, brute-force approach to solve the problem. Brute-force just means we'll try every possible combination to see if any of them add up to the target.

Pseudocode: subset_sum(nums, target)

Inputs
1. nums: A list of integers representing the follower counts of influencers.
2. target: The target sum we want to find a subset for.

Output
True if there exists a subset of nums that adds up to target. False otherwise.

Algorithm
1. Call the helper function starting with the last index in nums and return its result.

Pseudocode: find_subset_sum(nums, target, index)

Inputs
1. nums: A list of integers representing the follower counts of influencers.
2. target: The target sum we want to find a subset for.
3. index: The index of the current element we're considering.

Output
True if there exists a subset of nums that adds up to target. False otherwise.

Algorithm
1. If the target is 0, return True.
2. If the index is less than 0 and the target is not 0, return False.
3. If the number at the current index is greater than the target, call the helper function with the same target but with the index decremented by 1, and return the result, we're done.
4. Otherwise, call the helper function with the same target and index decremented by 1, and save the result.
5. Also, call the helper function with the target reduced by the value of the current element and the index decremented by 1
6. If either of these calls returns True, return True. Otherwise, return False.
"""

def subset_sum(nums: list[int], target: int) -> bool:
    return find_subset_sum(nums, target, len(nums) - 1)


def find_subset_sum(nums: list[int], target: int, index: int) -> bool:
    if target == 0:
        return True
    
    if index < 0 and target != 0:
        return False
    
    if nums[index] > target:
        return find_subset_sum(nums, target, index - 1)
    
    skip = find_subset_sum(nums, target, index - 1)
    include = find_subset_sum(nums, target - nums[index], index - 1)

    return skip or include
