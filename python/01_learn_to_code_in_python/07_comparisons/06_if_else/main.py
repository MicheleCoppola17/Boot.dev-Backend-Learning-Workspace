"""
Assignment:
Complete the player_status function. If the player's health is less than or equal to 0, return the string:

'dead'

Otherwise, if it's less than or equal to 5 return the string:

'injured'

Otherwise, return the string:

'healthy'
"""

def player_status(health):
    if health <= 0:
        return "dead"
    elif health <= 5:
        return "injured"
    else:
        return "healthy"

