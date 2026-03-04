class Animal:
    species_count = 100  # Атрибут класса

    def __init__(self, name):
        self.name = name  # Атрибут экземпляра
        Animal.species_count += 1


class Dog(Animal):
    pass


class Cat(Animal):
    pass


# Пробуем:
dog1 = Dog("Бобик")
cat1 = Cat("Мурка")
dog2 = Dog("Шарик")
print("------------ dog1 ----------------")
print(dog1.species_count)
print(dog1.__dict__)
print("------------ cat1 ----------------")
print(cat1.species_count)
print(cat1.__dict__)
print("------------ dog2 ----------------")
print(dog2.species_count)
print(dog2.__dict__)
print("------------ Animal ----------------")
print(Animal.species_count)
print("------------ Dog ----------------")
print(Dog.__dict__)
print(Dog.species_count)
