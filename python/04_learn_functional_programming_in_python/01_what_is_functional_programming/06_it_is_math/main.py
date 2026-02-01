"""
Assignment:
In the world of document conversion, we sometimes need to handle fonts and font sizes.

Complete the get_median_font_size function. Given a list of numbers representing font sizes, return the median of the list.

For example:

[1, 2, 3] => 2
[10, 8, 7, 5] => 7

Notice the second list is out of order. Sort the list so that it is in ascending order, then find the middle index, and return the middle number. If there is an even amount of numbers, return the smaller of the two middle numbers (I know it's not a true median, but good for our purposes). If the list is empty, just return None.

Here are some helpful docs:

- sorted
- len
- // (floor division)

To be a good little functional programmer, your code for this lesson should not:

1. Use loops
2. Mutate any variables (it's okay to create new ones)
"""
"""
# My first implementation:
def get_median_font_size(font_sizes):
    sizes_number = len(font_sizes)
    sorted_font_sizes = sorted(font_sizes)
    middle_index = sizes_number // 2
    if not sorted_font_sizes:
        return None
    if sizes_number % 2 == 0:
        return sorted_font_sizes[middle_index - 1]
    else:
        return sorted_font_sizes[middle_index]

# It is functional enough, but it's slightly more “imperative-feeling” because it reads like a sequence of steps.
"""

# Another implementation could be this:
def get_median_font_size(font_sizes):
    if len(font_sizes) == 0:
        return None
    return sorted(font_sizes)[(len(font_sizes) - 1) // 2]
