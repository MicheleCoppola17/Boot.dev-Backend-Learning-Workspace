"""
Assignment:
Complete the fortify() method on the wall class. It should double the current armor property.
"""

class Wall:
    armor = 10
    height = 5

    def fortify(self):
        self.armor *= 2
