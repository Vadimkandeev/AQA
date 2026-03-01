class DataError(Exception):
    pass

class Product:
    def __init__(self, name, price, category, stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
    def get_info(self):
        if self.stock == 0:
            return f"Товар закончился"
        else:
            return f"Наименование товара: {self.name}, цена за единицу: {self.price}, Категория: {self.category},\
            Количество на складе: {self.stock}."

    def is_available(self):
        if self.stock > 0:
            return True

    def reduce_stock(self):
        if self.stock == 0:
            return f"Товар закончился"
        else:
            self.stock -= 1

    def add_stock(self):
        self.stock += 1




class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = {}

    def add_item(self, product, quantity):
        if Product.stock == 0:
            raise DataError("Товар закончился")
        elif Product.stock < quantity:
            raise DataError("Товара недостаточно. Уменьшите количество")
        else:
            self.items[product] = quantity
            Product.stock -= quantity




    def remove_item(self, product_name):
        if
        pass

    def calculate_total(self):
        pass

    def get_cart_info(self):
        pass

    def checkout(self):
        pass
