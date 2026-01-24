"""
Assignment:
The Fantasy Quest character system needs a list of "heroes" to be able to run the game properly. 
Someone wrote some pretty nasty code, and the code in question creates a heroes list where every 3rd index defines a new hero. 
First their name, then their age, then whether or not they're an "elf".

Restructure the heroes list into a list of tuples by editing the syntax on lines 12 through 23, where each tuple represents one hero and contains their data in the same order.
"""

def get_heroes():
    heroes = [
        ("Glorfindel", 2093, True),
        ("Gandalf", 1054, False),
        ("Gimli", 389, False),
        ("Aragorn", 87, False)
    ]

    return heroes
