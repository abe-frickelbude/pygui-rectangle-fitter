"""
 2D Rectangle blah-blah
"""


class Rectangle:

    def __init__(self, x: float, y: float, width: float, height: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rect:[x: {self.x}, y: {self.y}, width: {self.width}, height: {self.height}]"

    def aspect_ratio(self):
        return self.width / self.height

    def is_defined(self):
        return self.width > 0 and self.height > 0
