class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def is_square(self):
        if self.width == self.height:
            return True

    def get_info(self):
        return {"Width": self.width, "Height": self.height, "Area": Rectangle.area(self), "Perimeter": Rectangle.perimeter(self), \
                "Is_square": Rectangle.is_square(self)}

    def scale(self, factor):
        self.width *= factor
        self.height *= factor

    def compare_area(self, other_rectangle):
        if Rectangle.area(self) < Rectangle.area(other_rectangle):
            return "Другой прямоугольник больше"
        elif Rectangle.area(self) > Rectangle.area(other_rectangle):
            return "Другой прямоугольник меньше"
        else:
            return "Прямоугольники равны"



my_rectangle = Rectangle(250, 350)

other_rectangle = Rectangle(280, 315)

print(my_rectangle.get_info())

print(my_rectangle.compare_area(other_rectangle))
