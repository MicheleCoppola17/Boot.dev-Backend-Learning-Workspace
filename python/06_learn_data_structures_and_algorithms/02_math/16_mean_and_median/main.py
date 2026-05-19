"""
Assignment
We now need a way to show our LockedIn influencers the average (mean) follower count of the people they follow. This will help them know if they're following people who are more or less popular than them.

Complete the average_followers function.

It should return the average of the given list of numbers.
If the list is empty, it should return None.
"""

def average_followers(nums):
    num_of_followers = len(nums)
    if num_of_followers == 0:
        return None
    sum = 0
    for num in nums:
        sum += num
    return sum / num_of_followers
