"""
Fantasy Quest doesn't have any way for players to know if they are strong enough to hold their own against certain enemies.

If a player's power level is greater than the enemy's defense, that player has an "advantage"
If the player's power and enemy's defense are equal, they are "evenly matched"
Otherwise, that player has a "disadvantage".

Assignment:
On line 17 write an if/elif/else block. Using the rules specified above, set advantage, disadvantage, or evenly_matched to True depending on the values of player_power and enemy_defense.

For example, if the player's power is greater than the enemy's defense, advantage should be set to True. etc.
"""

def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    if player_power > enemy_defense:
        advantage = True
    elif player_power == enemy_defense:
        evenly_matched = True
    else:
        disadvantage = True

    return advantage, disadvantage, evenly_matched
