# class Vehicle:
#     def move(self):
#         print("What?")
#
# class Car(Vehicle):
#     pass
#
# car = Car()
#
# print(dir(car))
#
# #print(Car.__str__)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def func(self):
#         return self.name, self.age
#
# class Student(Person):
#     pass
#
# person = Person("Oggy")
#
# student = Student()
#
# student_2 = Student("Piter", 21, "Bob")
#
#
#
# print(student_2.func())


class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return f"Цвет: {self.color}"

    def describe(self):
        return "Это геометрическая фигура"

class Circle(Shape):
    pass

circle = Circle("Blue")


# print(circle.get_color())
#
# print(circle.describe())

#print(Shape.__dict__.get("color"))


# print(Circle.__dict__)
#
# print(circle.__dict__)

class Father:
    pass

class Son(Father):
    pass

