"""
Assignment:
Your manager noticed that "Age of Dragons" has a lot of repetitive code. She's asked you to update the fight_soldiers function so that the DPS (damage-per-second) calculation logic is only written in one place.

Notice how these two lines are practically identical:

soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]

Create a new function called get_soldier_dps that takes a soldier and returns that soldier's DPS using the same logic as the lines above.
Inside fight_soldiers, replace the two DPS lines above with calls to get_soldier_dps
The soldier with the greater DPS will win the fight!
"""

# Initial function
def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
    soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"

# Submitted function
def get_soldier_dps(soldier):
    return soldier["damage"] * soldier["attacks_per_second"]

def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = get_soldier_dps(soldier_one)
    soldier_two_dps = get_soldier_dps(soldier_two)
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"
