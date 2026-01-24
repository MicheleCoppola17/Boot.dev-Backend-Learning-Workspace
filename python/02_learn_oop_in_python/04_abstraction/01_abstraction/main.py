"""
Assignment:
We don't want our coworkers at Age of Dragons Studios™ to have to worry about how Humans move. 
We'll abstract that away from them by encapsulating the private __pos_x, __pos_y, and __speed variables behind some simple methods.

Complete the following methods in the Human class:

1. move_right(): Adds the human's speed to its x position.
2. move_left(): Subtracts the human's speed from its x position.
3. move_up(): Adds the human's speed to its y position.
4. move_down(): Subtracts the human's speed from its y position.
5. get_position(): Returns the x position and y position as a tuple.
"""

class Human:
    def __init__(self, pos_x, pos_y, speed):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return self.__pos_x, self.__pos_y
