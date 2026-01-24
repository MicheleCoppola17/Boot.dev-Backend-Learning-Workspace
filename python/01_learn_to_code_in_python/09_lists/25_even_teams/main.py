"""
Assignment:
Complete the split_players_into_teams function.

It accepts a list of players (strings representing their names) and returns two lists in this order:

1. A new list of all the players with even-numbered indexes in the original list.
2. A new list of all the players with odd-numbered indexes in the original list.
Use a slice with a "step" to create two new lists from the players list. Don't be afraid to consult your spellbook for list slicing help!
"""

def split_players_into_teams(players):
    even_numbered_players = players[::2]
    uneven_numbered_players = players[1::2]
    return even_numbered_players, uneven_numbered_players
