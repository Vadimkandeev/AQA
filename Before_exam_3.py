class GoblinMerchant:
    def __init__(self, gold):
        self.gold = gold

    @staticmethod
    def tax_rate(pay_sum):
        return pay_sum * 0.1

    @classmethod
    def from_rich_merchant(cls):
        return cls(1000)



    def buy_item(self, item_name, item_price):
        tax = self.tax_rate(item_price)
        total_sum = item_price + tax
        if self.gold < total_sum:
            raise ValueError(f"На хватает золота на покупку {item_name}")
        self.gold = self.gold - total_sum
        return f"{item_name} успешно куплен"


#goblin = GoblinMerchant(500)

goblin = GoblinMerchant.from_rich_merchant()

print(goblin.buy_item("Magic Swodr", 1000))

