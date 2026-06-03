"""
Assignment
Our LockedIn influencers are complaining that when they sort their followers by follower count, it gets really slow if they have more than 1,000 followers (because we're using Bubble Sort). Let's speed it up for them with merge sort.

Complete the merge_sort and merge functions according to the described algorithms.
"""

def merge_sort(nums: list[int]) -> list[int]:
    nums_len = len(nums)
    if nums_len < 2:
        return nums
    left_half = nums[:nums_len//2]
    right_half = nums[nums_len//2:]
    sorted_left_side = merge_sort(left_half)
    sorted_right_side = merge_sort(right_half)
    return merge(sorted_left_side, sorted_right_side)
    


def merge(first: list[int], second: list[int]) -> list[int]:
    final = []
    i, j = 0, 0 
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    final += first[i:]
    final += second[j:]
    return final

        