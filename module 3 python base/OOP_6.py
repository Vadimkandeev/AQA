class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        return f"{self.name} - {self.price}P ({self.category})"


class Electronics(Product):
    def check_warranty(self):
        return "Warranty is not valid"

    def power_on(self):
        return f"{self.name} ON"

class Clothing(Product):
    def try_on(self):
        return f"Примерка {self.name}"

    def wash_instruction(self):
        return f"Стирать при 30 градусах"

class Book(Product):
    def read_sample(self):
        return f"Читаем отрывок {self.name}"

    def bookmark(self):
        return f"Закладка добавлена в {self.name}"


boombox = Electronics("Honor", 20000, "smartphone")

suite = Clothing("cotton_suite", 15000, "white suites")

book = Book("Преступление и наказание", 500, "Русская классика")

print (boombox.check_warranty())
print (boombox.power_on())
print (boombox.get_info())
print ("-------------------")
print (suite.try_on())
print (suite.wash_instruction())
print (suite.get_info())
print ("-------------------")
print (book.read_sample())
print (book.bookmark())
print (book.get_info())

