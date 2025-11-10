"""
Assignment:
Complete the check_mount_rental function. It takes two inputs:

1. time_used - the amount of time the mount has been used in minutes
2. time_purchased - the amount of time the character rented the mount for
- If time_used meets or exceeds time_purchased, then the rental is expired and greedy Uper will charge a fee, so the function should return the string "overtime charged"
- Otherwise, return the string "no charges yet"

Bonus: Try to accomplish this without an "else" statement.
"""

def check_mount_rental(time_used, time_purchased):
    if time_used >= time_purchased:
        return "overtime charged"
    return "no charges yet"
