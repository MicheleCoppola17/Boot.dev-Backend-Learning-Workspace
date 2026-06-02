"""
Assignment
While our avocado toast influencers were happy with our search functionality, now they want to be able to sort all their followers by follower count. Bubble sort is a straightforward sorting algorithm that we can implement quickly, so let's do that!

Complete the bubble_sort function according to the described algorithm above.
"""

def bubble_sort(nums: list[int]) -> list[int]:
    swapping = True
    end = len(nums) 
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
        end -= 1
    return nums

