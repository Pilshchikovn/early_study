class Rectangle:
    __slots__ = '__width', 'height'

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Треугольник шириной {self.width}, высостой {self.height}'

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        print('setter called')
        self.__width = value

s =Rectangle(5,3)
print(s)
