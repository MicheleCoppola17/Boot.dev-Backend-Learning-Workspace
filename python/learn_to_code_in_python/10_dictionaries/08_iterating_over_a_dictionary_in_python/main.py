"""
Assignment:
We need to display on our players' screens what the most common enemy in a given area of the game map is.

Complete the get_most_common_enemy function by iterating over all enemies in the dictionary and returning only the name of the enemy with the highest count.

If there are no enemies, return the Python None value (not a string). If there are multiple enemies with the same highest count, return the first one found.

enemies_dict is a dictionary of name -> count. Example:

{
    "jackal": 1,
    "kobold": 2,
    "soldier": 3,
    "gremlin": 5
}
"""

def get_most_common_enemy(enemies_dict):
    max_value = float("-inf")
    most_common_enemy = None
    for enemy in enemies_dict:
        enemy_count = enemies_dict[enemy]
        if enemy_count > max_value:
            max_value = enemy_count
            most_common_enemy = enemy
    return most_common_enemy
