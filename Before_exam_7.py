class GoblinBank:
    #__gold = 0
    def __init__(self, gold):
        if gold < 0:
            raise ValueError(f"Количество золота не может быть отрицательным")
        self.__gold = gold


    def get_gold(self):
        return self.__gold

    def deposit_gold(self, amount):
        if amount > 0:
            self.__gold += amount
            print(f"Добавлено {amount} золота, текущий баланс {self.__gold}")

    def withdraw_gold(self, amount):
        if self.__gold < amount:
            raise  ValueError("Недостаточно золота!")
        self.__gold -= amount
        print(f"Снято {amount} золота, текущий баланс {self.__gold}")




bank = GoblinBank(100)

print(bank.get_gold())  # Вывод: 100
bank.deposit_gold(50)   # Вывод: Добавлено 50 золота. Текущий баланс: 150
bank.withdraw_gold(30)  # Вывод: Снято 30 золота. Текущий баланс: 120
bank.withdraw_gold(200) # Вывод: Недостаточно золота!