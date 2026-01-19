"""
Assignment:
Finish implementing the empty methods of the Rectangle and Square classes. All squares are rectangles, but not all rectangles are squares.

Due to inheritance of methods, the Square class should only need to implement the __init__ method and re-use Rectangle's initialization by calling super().__init__(length, length).
"""

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__length * self.__width

    def get_perimeter(self):
        return (self.__length + self.__width) * 2


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
