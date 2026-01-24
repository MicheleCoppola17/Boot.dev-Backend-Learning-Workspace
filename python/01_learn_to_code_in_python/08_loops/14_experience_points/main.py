"""
Assignment:
Complete the calculate_experience_points function.

It accepts a level (integer) and returns the total XP a player has gained so far.
"""

def calculate_experience_points(level):
    xp = 0
    for i in range(0, level):
        xp += i * 5
    return xp
