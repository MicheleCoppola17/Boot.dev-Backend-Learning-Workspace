"""
Assignment:
One of the greatest sins when trying to write "clean code" is using misleading variable and function names. Take a look at the destroy_wall function. It takes a list of numbers as input (each representing the health of a wall) and returns a new list with each entry of 0 or less removed.

Based on its name, you might assume that destroy_wall destroys a single wall, but if you look closely, you'll see that it handles multiple walls.

The test suite expects a different function name. Take a look at the main_test.py file to see what it's looking for, and rename the function accordingly.
Bonus: rename the variables inside the function to be more descriptive.
"""
# Initial function
def destroy_wall(wall_health):
    h = []
    for w in wall_health:
        if w > 0:
            h.append(w)
    return h

# Submitted function
def destroy_walls(wall_healths):
    new_wall_healths = []
    for wall_health in wall_healths:
        if wall_health > 0:
            new_wall_healths.append(wall_health)
    return new_wall_healths
