class Animal:
    def sound(self):
        return "Звук животного"

class Mammal(Animal):
    def sound(self):
        return "Звук млекопитающего"

class Dog(Mammal):
    def sound(self):
        # super() найдет следующий в MRO - это Mammal, а не Animal
        return super().sound() + " - Гав!"

dog = Dog()
print(dog.sound())  # Звук млекопитающего - Гав!
print(Dog.__mro__)  # Покажет порядок поиска