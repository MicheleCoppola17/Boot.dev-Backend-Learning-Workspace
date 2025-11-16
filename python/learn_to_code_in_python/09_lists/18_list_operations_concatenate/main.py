"""
Assignment:
Fantasy Quest allows users to keep lists of their favorite items. Your job is to finish the concatenate_favorites function. 
It takes three different lists - the player's favorite_weapons, favorite_armor and favorite_items.

1. Create a new list that combines the lists favorite_weapons, favorite_armor, and favorite_items in this order.
2. Return the list containing the combined favorites.
"""

def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    all_favorites = favorite_weapons + favorite_armor + favorite_items
    return all_favorites
