"""
Assignment:
Inside the loop in the get_odd_numbers function, use the modulo operator to check if each number, i, is odd. 
If a number is odd, append it to the odd_numbers list. 
The function already returns the odd_numbers list for you. num is an integer.
"""

def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        # don't touch above this line
        if i % 2 != 0:
            odd_numbers.append(i)

    # don't touch below this line

    return odd_numbers
