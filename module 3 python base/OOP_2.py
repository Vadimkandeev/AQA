class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.brand} {self.model} заводится"


class Car(Vehicle):
    def honk(self):
        return f"{self.brand} {self.model} сигналит Бип-бип!"

class Motorcycle(Vehicle):
    def wheel(self):
        return f"{self.brand} {self.model} делает вилли!"


car = Car("Toyota", "Camry", 2019)
print(car.start_engine())
print(car.honk())

moto = Motorcycle("Harley Davidson", "Fat Boy", 2000)
print(moto.start_engine())
print(moto.wheel())