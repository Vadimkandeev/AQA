class GoblinTrader:
    gold = 1000
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price


    def by_item(self):
        if self.gold < self.item_price:
            raise ValueError("Недостаточно денег на счету")
        else:
            self.gold = self.gold - self.item_price
        return f"Куплен {self.item_name}"


goblin = GoblinTrader("Меч восстановления девственности",  180)

print(goblin.by_item())