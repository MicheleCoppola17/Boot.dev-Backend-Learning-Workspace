"""
Assignment:
We need to be able to report to our players how many enemies are in their immediate vicinity - but they want the count of each enemy by its kind. 
Fix the count_enemies function. It accepts as input:

- enemy_names: a list of strings.

It should return a dictionary where:

- The keys are all the enemy names from the list
- The values are the counts of how many times each enemy appeared in the list.

1. Run the code in its current state. It will raise a KeyError.
2. Fix the code by checking if a key is in the dictionary before trying to update its value. If it isn't, set it to 1.
"""

def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        if enemy_name in enemies_dict:
            enemies_dict[enemy_name] += 1
        else:
            enemies_dict[enemy_name] = 1
    return enemies_dict
