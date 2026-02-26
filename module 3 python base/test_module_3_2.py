class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def is_square(self):
        return self.width == self.height

    def get_info(self):
        return {"Width": self.width, "Height": self.height, "Area": self.area(), "Perimeter": self.perimeter(),\
                "Is_square": self.is_square()}



my_rectangle = Rectangle(250, 350)

other_rectangle = Rectangle(280, 315)


def scale(factor, rec):
    """
    Увеличение сторон прямоугольника.
    (Хотя, непонятно, зачем нужна эта функция)
    """
    rec.width *= factor
    rec.height *= factor


rectangle_1 = Rectangle(10, 20)
rectangle_2 = Rectangle(11, 19)
rectangle_3 = Rectangle(12, 18)
rectangle_4 = Rectangle(13, 17)
rectangle_5 = Rectangle(14, 16)
rectangle_6 = Rectangle(15, 15)
rectangle_7 = Rectangle(16, 14)


rectangles = [rectangle_1, rectangle_2, rectangle_3, rectangle_4, rectangle_5, rectangle_6, rectangle_7]

def compare_area(rec_s):
    """
    Сравнение прямоугольников
    """
    largest = rec_s[0]
    for rec in rec_s[1:]:
        if largest.area() < rec.area():
            largest = rec
    return largest



def attache(rec_1: Rectangle, rec_2: Rectangle):
    """
    Вложенность
    """
    if (rec_1.width <= rec_2.width) and (rec_1.height <= rec_2.height):
        return 0
    elif (rec_1.width >= rec_2.width) and (rec_1.height >= rec_2.height):
        return 1
