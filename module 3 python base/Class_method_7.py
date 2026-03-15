class Product:
    products = {"laptop": 10, "phone": 5}
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.add_product(name, quantity)

    @classmethod
    def add_product(cls, name, quantity):
        if name in cls.products:
            cls.products[name] += quantity
            print(f"------- {name}")
        else:
            cls.products[name] = quantity
            print(f"*** {name}")

    @classmethod
    def show_products(cls):
        print(cls.products)


p1 = Product("phone", 5)
p2 = Product("mouse", 10)
p3 = Product("laptop", 3)

Product.show_products()