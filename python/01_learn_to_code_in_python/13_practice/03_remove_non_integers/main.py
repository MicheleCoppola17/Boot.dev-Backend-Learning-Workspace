"""
Assignment:
Complete the remove_nonints() function. It takes a list and returns a new list but with all the non-integer types removed.

new_list = remove_nonints(["1", 1, "3", "400", 4, 500])
print(new_list)
# [1, 4, 500]

Do not change the input nums list. Return a new list with only the integers.
"""

def remove_nonints(nums):
    int_list = []
    for item in nums:
        if type(item) == int:
            int_list.append(item)
    return int_list
