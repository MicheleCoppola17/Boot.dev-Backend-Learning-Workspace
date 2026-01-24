"""
Assignment:
Fix the avg_luck_boost function in main.py.

- At the beginning of the function, check if luck_boosts is an empty list. If so, just return 0.0 to avoid a divide-by-zero error.
"""

def avg_luck_boost(luck_boosts):
    if len(luck_boosts) == 0:
        return 0.0
    else:
        total = 0
        for boost in luck_boosts:
            total += boost
        return total / len(luck_boosts)
