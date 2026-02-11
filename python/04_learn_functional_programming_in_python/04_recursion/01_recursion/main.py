"""
Assignment
Doc2Doc can automatically generate various layouts for a page. There are a lot of possible layouts, so we need a factorial function to calculate the total number of possible layouts.

Complete the factorial_r function. It should recursively calculate the factorial of a number.

A factorial is the product of all positive integers less than or equal to a number. For example, 5! (read: "five factorial") is 5 * 4 * 3 * 2 * 1, which is 120.
"""

def factorial_r(x):
    if x <= 0:
        return 1
    return x * factorial_r(x - 1)
