"""
Assignment:
In Age of Dragons, players craft new weapons from old ones. To keep this mechanic simple for other developers, we'll use operator overloading on the Sword class.

Observe how the test suite uses the + operator to craft the swords.

Create an __add__(self, other) method on the Sword class.

1. If two "bronze" swords are crafted together, return a new Sword of type "iron".
2. If two "iron" swords are crafted together, return a new Sword of type "steel".
3. If a player tries to craft anything other than 2 bronze swords or 2 iron swords, just raise an Exception with the message "cannot craft".

Note that a sword's sword_type is just a string, one of:

- bronze
- iron
- steel
"""

class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        if self.sword_type == "bronze" and other.sword_type == "bronze":
            return Sword(sword_type="iron")
        elif self.sword_type == "iron" and other.sword_type == "iron":
            return Sword(sword_type="steel")
        else:
            raise Exception("cannot craft")
