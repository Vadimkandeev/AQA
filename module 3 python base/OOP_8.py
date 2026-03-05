class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} издает звук"


class Dog(Animal):
    def make_sound(self):
        return f"{self.name} лает"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} мяукает"


animal = Animal("Животное")
dog = Dog("Шарик")
cat = Cat("Мурка")

print(animal.make_sound())
print(cat.make_sound())
print(dog.make_sound())

