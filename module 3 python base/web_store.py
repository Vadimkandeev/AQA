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
        if product.stock == 0:
            raise DataError("Товар закончился")
        elif product.stock < quantity:
            raise DataError("Товара недостаточно. Уменьшите количество")
        else:
            self.items[product] = quantity


    def remove_item(self, product_name):
        try:
            del self.items[product_name]
        except KeyError:
            print("Товар не найден")


    def calculate_total(self):
        total_sum = 0
        for product, quantity in self.items.items():
            total_sum += product.price * quantity
        return total_sum

    def get_cart_info(self):
        if not self.items:
            return "Корзина пуста"
        else:
            for product, quantity in self.items.items():
                return  f"Наименование: {product.name}, цена:{product.price}, количество: {quantity},\
общая сумма: {self.calculate_total()}"

    def checkout(self):
        """
        Оформить заказ (уменьшить stock у всех товаров)
        """
        if not self.items:
            return "Корзина пуста"
        else:
            for product, quantity in self.items.items():
                product.stock -= quantity


