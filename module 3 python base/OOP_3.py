class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} издает звук"

class Dog(Animal):
    def bark(self):
        return f"{self.name} лает"

class Cat(Animal):
    def neow(self):
        return f"{self.name} мяукает"

animal = Animal("Animal")
dog = Dog("Snoopy")
cat = Cat("Spike")

print(animal.speak())