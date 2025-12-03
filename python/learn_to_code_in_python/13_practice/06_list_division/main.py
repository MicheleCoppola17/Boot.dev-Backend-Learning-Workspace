"""
Assignment:
Complete the divide_list() function. It takes a list and a number as input, and should return a new list that contains all the elements of the original list after dividing them by the second input.

For example:

divided_list = divide_list([6, 8, 10], 2)
print(divided_list)
# [3.0, 4.0, 5.0]

Do not round the resulting float numbers, just return them as they are.
"""

def divide_list(nums, divisor):
    divided_numbers = []
    for num in nums:
        divided_numbers.append(num / divisor)
    return divided_numbers
