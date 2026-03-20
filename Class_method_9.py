from typing import TypeVarTuple


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TimeoutError("Ошибка ввода данных")
        if value <= 0:
            raise  ValueError("Размер не может быть меньше или равен нулю")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Ошибка ввода данных")
        if value <= 0:
            raise ValueError("Размер не может быть меньше или равен нулю")
        self._height = value

    @property
    def perimeter(self):
        return (self._width + self._height)*2

rectangle = Rectangle(25, 50)

print(rectangle.perimeter)