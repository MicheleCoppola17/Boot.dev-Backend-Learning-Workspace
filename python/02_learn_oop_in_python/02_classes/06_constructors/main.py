"""
Assignment:
Add a constructor to the Wall class.

1. It should take depth, height and width as parameters, in that order, and set them as instance properties.
2. Compute an additional property called volume. Volume is the depth times height times width.
"""

class Wall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = depth * height * width
