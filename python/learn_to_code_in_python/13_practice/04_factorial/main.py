"""
Assignment:
Complete the factorial() function. It should return the factorial of a given number.

In mathematics, the ! symbol denotes a factorial, but is not a valid Python Factorial operator. Use a loop and multiplication to compute the proper result.
"""

def factorial(num):
    factorial = 1

    for i in range(num, 0, -1):
        factorial *= i

    return factorial