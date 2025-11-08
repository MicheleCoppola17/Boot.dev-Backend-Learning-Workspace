"""
ASSIGNMENT:
Find the bug in the code on line 15. We're using variable names from the wrong scope. Fix it!
"""

def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10

## don't touch above this line

max_health = get_max_health(my_modifier, my_level)

# don't touch below this line

print(f"max_health is: {max_health}")