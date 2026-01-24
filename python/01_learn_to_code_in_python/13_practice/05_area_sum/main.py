"""
Assignment:
Complete the area_sum() function. It accepts a list of rectangles, where each rectangle is a dictionary that has the following structure:

{
  "height": 5,
  "width": 6
}

It should calculate the area of each rectangle and return the sum of all the areas.
"""

def area_sum(rectangles):
    area_sum = 0
    for rectangle in rectangles:
        area_sum += rectangle["height"] * rectangle["width"]
    return area_sum
