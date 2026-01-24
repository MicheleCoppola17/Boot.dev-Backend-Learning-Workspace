"""
Assignment:
Complete the find_missing_ids function. It accepts two lists as input, and returns a new set of all the IDs that are in the first list but are not in the second.

Naturally, there will be no duplicates in the resulting set.
"""

def find_missing_ids(first_ids, second_ids):
    only_first_ids_set = set(first_ids) - set(second_ids)
    return only_first_ids_set

