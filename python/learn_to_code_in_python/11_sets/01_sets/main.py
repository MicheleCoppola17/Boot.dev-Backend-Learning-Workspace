"""
Assignment:
Complete the remove_duplicates function. It should take a list of spells that a player has learned and return a new List where there is at most one of each title. You can accomplish this in at least two ways:

Iteration:
1. Create a set to track spells that have been seen
2. Create a list to store the unique spells
3. Iterate over the list
    1. If the spell is not in the set, add it to the set and the list
4. Return the list

Set conversion:
1. Convert the list to a set
2. Convert the set back to a list and return it.

It makes no sense to learn a spell twice! Once it's learned, it's learned forever.
"""

"""
# ITERATION
def remove_duplicates(spells):
    spells_set = set()
    no_duplicates_spells = []

    for spell in spells:
        if spell not in spells_set:
            spells_set.add(spell)
            no_duplicates_spells.append(spell)

    return no_duplicates_spells 
"""


# SET CONVERSION
def remove_duplicates(spells):
    spells_set = set(spells)
    no_duplicates_spells = list(spells_set)

    return no_duplicates_spells