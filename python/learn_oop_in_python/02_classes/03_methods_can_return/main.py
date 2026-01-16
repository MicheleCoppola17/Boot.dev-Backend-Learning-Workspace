"""
Assignment:
Building walls in Age of Dragons can be expensive, the larger and stronger the wall, the more it costs.

Complete the .get_cost() method on the Wall class. It should return the cost of a wall, where the cost is its armor multiplied by its height.
"""

class Wall:
    armor = 10
    height = 5

    def get_cost(self):
        return self.armor * self.height

    # don't touch below this line

    def fortify(self):
        self.armor *= 2
