"""
Assignment:
Complete the following methods on the Wizard class:

1. get_fireballed() should:
    - Reduce the fireball_damage by the wizard's __stamina
    - Reduce the wizard's health by the resulting fireball_damage
2. drink_mana_potion() should:
    - Increase the potion_mana by the wizard's __intelligence
    - Increase the wizard's mana by the resulting potion_mana

Both methods operate directly on the instance of the class (self). They take one input and return no values explicitly.
"""

class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    # don't touch above this line

    def get_fireballed(self, fireball_damage):
        fireball_damage -= self.__stamina
        self.health -= fireball_damage

    def drink_mana_potion(self, potion_mana):
        potion_mana += self.__intelligence
        self.mana += potion_mana
