"""
Assignment:
Complete the Wizard class's constructor.

1. Set 2 private properties (be sure to include the private __ prefix):
    1. stamina
    2. intelligence
2. Set 3 public properties:
    1. name: Use the value passed into the constructor
    2. health: 100x the value of "stamina"
    3. mana: 10x the value of "intelligence"
"""

class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.health = self.__stamina * 100
        self.mana = self.__intelligence * 10
