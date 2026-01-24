"""
Assignment:
1. Complete the Dragon's constructor:
    1. Call constructor of the Unit class with the provided parameters
    2. Set the dragon-specific parameters as instance variables
    3. Create a new private __hit_box member. It's a Rectangle object representing the dragon's hit box. See the tips below if you need help.
2. Override the in_area method in the Dragon class:
    1. Create a new rectangle object with the given corner positions.
    2. Use the rectangle's overlaps method to check if the Dragon's self.__hit_box is inside it, and return the result.

The given pos_x and pos_y for any unit is the center point of that unit!
"""

class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1, y1, x2, y2):
        return (
            self.pos_x >= x1
            and self.pos_x <= x2
            and self.pos_y >= y1
            and self.pos_y <= y2
        )


# don't touch above this line


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.height = height
        self.width = width
        self.fire_range = fire_range
        self.__hit_box = Rectangle(x1=self.pos_x - (self.width / 2), 
                                   y1=self.pos_y - (self.height / 2), 
                                   x2=self.pos_x + (self.width / 2),
                                   y2=self.pos_y + (self.height / 2))

    def in_area(self, x1, y1, x2, y2):
        rect = Rectangle(x1, y1, x2, y2)
        return rect.overlaps(self.__hit_box)


# don't touch below this line


class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2
