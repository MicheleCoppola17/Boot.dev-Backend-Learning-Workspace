"""
Assignment:
Take a look at the Brawler class and the fight function provided, then complete the main function by doing the following:

1. Create 4 new brawlers with the following stats:
    1. Name: Aragorn. Speed: 4. Strength: 4.
    2. Name: Gimli. Speed: 2. Strength: 7.
    3. Name: Legolas. Speed: 7. Strength: 7.
    4. Name: Frodo. Speed: 3. Strength: 2.
2. Call fight twice:
    1. The first fight should be Aragorn vs Gimli.
    2. The second will be Legolas vs Frodo.
"""

def main():
    aragorn = Brawler("Aragorn", 4, 4)
    gimli = Brawler("Gimli", 2, 7)
    legolas = Brawler("Legolas", 7, 7)
    frodo = Brawler("Frodo", 3, 2)
    
    fight(aragorn, gimli)
    fight(legolas, frodo)


# don't touch below this line


class Brawler:
    def __init__(self, name, speed, strength):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.power = speed * strength


def fight(attacker, defender):
    print(f"{attacker.name}: {attacker.power} power")
    print(f"{defender.name}: {defender.power} power")
    if attacker.power > defender.power:
        print(f"{attacker.name} wins!")
    elif attacker.power < defender.power:
        print(f"{defender.name} wins!")
    else:
        print("It's a tie!")
    print("---------------------------------")


main()