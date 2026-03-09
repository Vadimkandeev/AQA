from datetime import  datetime

class DataError(Exception):
    pass

class OrderProcessor:

    def __init__(self):
        self.log = []
        self.log.append(f"{datetime.now()}. Заказ принят в обработку")
#--------------------------------------------------
    def process_order(self, order_data):
        try:
            order_data["order_id"]
        except KeyError:
            self.log.append(f"{datetime.now()}. Отсутствует ключ 'order_id'")
            raise DataError("Отсутствует ключ 'order_id'")
#--------------------------------------------------
        try:
            items = order_data["items"]
        except KeyError:
            self.log.append(f"{datetime.now()}. Отсутствует корзина")
            raise DataError("Отсутствует корзина")
        if not isinstance(items, dict):
            self.log.append(f"{datetime.now()}. Некорректный формат корзины")
            raise DataError("Некорректный формат корзины")
        if not items:
            self.log.append(f"{datetime.now()}. Корзина пуста")
            raise DataError("Корзина пуста")
        for value in items.values():
            if value <= 0:
                self.log.append(f"{datetime.now()}. Некорректное количество товара")
                raise DataError("Некорректное количество товара")
#-------------------------------------------------
        try:
            total_price = order_data["total_price"]
        except KeyError:
            self.log.append("Отсутствует ключ 'total_price'")
            raise DataError("Отсутствует ключ 'total_price'")
        if total_price <= 0:
            self.log.append(f"{datetime.now()}. Некорректная сумма заказа")
            raise DataError("Некорректная сумма заказа")
#-------------------------------------------------
        try:
            payment_method = order_data["payment_method"]
        except KeyError :
            self.log.append(f"{datetime.now()}. Отсутствует ключ 'payment_method'")
            raise DataError("Отсутствует ключ 'payment_method'")
        if payment_method != "card":
            self.log.append(f"{datetime.now()}. Не указан способ оплаты")
            raise DataError("Не указан способ оплаты")
#-------------------------------------------------
        try:
            payment_status = order_data["payment_status"]
        except KeyError:
            self.log.append(f"{datetime.now()}. Отсутствует ключ 'payment_status'")
            raise DataError("Недопустимый статус заказа")
        if payment_status != "pending":
            self.log.append(f"{datetime.now()}. Недопустимый статус заказа")
            raise DataError("Недопустимый статус заказа")
#-------------------------------------------------
        try:
            order_data["delivery_address"]
        except KeyError:
            self.log.append(f"{datetime.now()}. Отсутствует ключ 'delivery_address'")
            raise DataError("Не найден адрес для доставки")
#-------------------------------------------------
        try:
            order_data["card_number"]
        except KeyError:
            self.log.append(f"{datetime.now()}. Отсутствует ключ 'card_number'")
            raise DataError("Не указано платежное средство")
#-------------------------------------------------
        try:
            order_data["card_balance"]
        except KeyError:
            self.log.append(f"{datetime.now()}. Отсутствует ключ 'card_balance'")
            raise DataError("Не удается проверить баланс карты")




class PaymentProcessor(OrderProcessor):
    def __init__(self):
        pass

    def process_order(self, order_data):
        total = order_data["total price"]
        if order_data["card_balance"] < total:
            self.log.append(f"{self.data}. Сумма заказа превышает баланс карты")
            raise DataError(f"Сумма заказа превышает баланс карты")

class InventoryProcessor(OrderProcessor):
    def __init__(self):
        pass

class ShippingProcessor(OrderProcessor):
    def __init__(self):
        pass

