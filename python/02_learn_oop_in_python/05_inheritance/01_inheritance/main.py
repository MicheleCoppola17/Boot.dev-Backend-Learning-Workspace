"""
Assignment:
In Age of Dragons, all the archers are humans, but not all humans are necessarily archers. 
All humans have a name, but only archers have a __num_arrows property.

Complete the Archer class. It should inherit the Human class.

1. Its constructor should:
    - Call the parent constructor
    - Set the private __num_arrows property based on the constructor parameter
2. Its get_num_arrows() method should return the number of arrows the archer has.
"""

class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

