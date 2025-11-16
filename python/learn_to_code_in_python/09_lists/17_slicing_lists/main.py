"""
Assignment:
Complete the given get_champion_slices function. It takes a list of champions and should return three new lists based on the given champions:

1. First, return a slice of the champions list that starts with the third champion and goes to the end of the list.
2. Next, return a slice of the champions list that starts at the beginning of the list and includes all champions except for the very last champion.
3. Last, return a slice of the champions list that only includes the champions in even numbered indexes.
"""

def get_champion_slices(champions):
    from_third_champ = champions[2:]
    except_last_champ = champions[:len(champions) - 1]
    even_champ = champions[::2]
    return from_third_champ, except_last_champ, even_champ
