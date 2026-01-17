"""
Assignment:
1. Complete the cast_fireball method:
    1. If there isn't enough mana to cast a fireball (based on the fireball_cost argument), raise an Exception with the message ____ cannot cast fireball, where ____ is the wizard's name.
    2. If the wizard has enough mana, reduce their mana by the fireball_cost and call get_fireballed on the target wizard with the given fireball_damage.
2. Complete the is_alive method. It should return True if the wizard's health is greater than 0 and False otherwise.
"""

class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def cast_fireball(self, target, fireball_cost, fireball_damage):
        if self.mana < fireball_cost:
            raise Exception(f"{self.name} cannot cast fireball")
        self.mana -= fireball_cost
        target.get_fireballed(fireball_damage)

    def is_alive(self):
        return self.health > 0

    def get_fireballed(self, fireball_damage):
        fireball_damage -= self.__stamina
        self.health -= fireball_damage

    def drink_mana_potion(self, potion_mana):
        potion_mana += self.__intelligence
        self.mana += potion_mana
