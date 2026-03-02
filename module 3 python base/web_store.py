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
        return self.stock > 0


    def reduce_stock(self, quantity):
        if self.stock < quantity:
            raise DataError("Недостаточно товара")
        else:
            self.stock -= quantity

    def add_stock(self, quantity):
        self.stock += quantity


# ------------------------------------------------------------------

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
            self.items[product] = {"quantity": quantity, "selected": False}


    def remove_item(self, product):
        try:
            del self.items[product]
        except KeyError:
            print("Товар не найден")


    def calculate_total(self):
        total_sum = 0
        for product, data in self.items.items():
            if data["selected"] == True:
                total_sum += product.price * data["quantity"]
        return total_sum

    def get_cart_info(self):
        cart_list = []
        if not self.items:
            return "Корзина пуста"
        else:
            for product, data in self.items.items():
                quantity = data["quantity"]
                selected = data["selected"]
                cart_list.append(f"Наименование: {product.name}, цена:{product.price}, количество: {quantity},\
                выбран: {data['selected']}")
        cart_list.append(f"Общая сумма: {self.calculate_total()}")
        return "\n".join(cart_list)

    def select_item(self, product):
        """
        Выделяем товар в корзине для поупки
        """
        if product not in self.items:
            raise DataError("Товара нет в корзине")
        self.items[product]["selected"] = True


    def unselect_item(self, product):
        """
        Снимаем выделение с товара
        """
        if product not in self.items:
            raise DataError("Товара нет в корзине")
        self.items[product]["selected"] = False


    def checkout(self):
        """
        Оформить заказ (уменьшить stock у всех товаров)
        """
        if not self.items:
            return "Корзина пуста"
        else:
            for product in list(self.items.keys()):
                data = self.items[product]
                quantity = data["quantity"]
                selected = data["selected"]
                if selected == True:
                    if product.stock < quantity:
                        raise DataError("Товара недостаточно. Уменьшите количество")
                    else:
                        product.stock -= quantity
                        self.remove_item(product)
        return "Заказ оформлен"









