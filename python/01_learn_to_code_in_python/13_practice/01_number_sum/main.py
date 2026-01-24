"""
Assignment
Complete the number_sum function. It should add up all the numbers from 1 to n and return the result. For example:

- number_sum(5) -> 1+2+3+4+5 -> 15
- number_sum(3) -> 1+2+3 -> 6
Remember that a range is not inclusive of the last number.
"""

def number_sum(n):
    sum = 0
    for i in range(0, n + 1):
        sum += i
    return sum
