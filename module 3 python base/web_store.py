class Product:
    def __init__(self, name, price, category, stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
    def get_info(self):
        return f"Наименование товара: {self.name}, цена за единицу: {self.price}, Категория: {self.category}, Количество на складе: {self.stock}."

    def is_available(self):
        if self.stock > 0:
            return True

    def reduce_stock(self):
        pass
    def add_stock(self):
        pass



class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name = customer_name

    items = {}

    def add_item(self, product, qantity):
        pass

    def remove_item(self, product_name):
        pass

    def calculate_total(self):
        pass

    def get_cart_info(self):
        pass

    def checkout(self):
        pass
