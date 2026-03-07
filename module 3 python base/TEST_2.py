class DataError(Exception):
    pass


class BankAccount:

    def __init__(self, balance):
        self.balance = balance


    def deposit(self, addition):

        if addition <= 0:
            raise ValueError("Сумма должна быть больше нуля")

        self.balance += addition

        return f"Пополнение на {addition}Р, баланс {self.balance}Р"


    def _data_verification(self, subtraction):

        if subtraction <= 0:
            raise ValueError("Сумма должна быть больше нуля")

        if self.balance < subtraction:
            raise DataError("На счету недостаточно средств")


    def _commission(self, subtraction):

        return 0


    def _message(self, subtraction, commission):

        return f"Снятие {subtraction}Р, комиссия {commission}Р, баланс {self.balance}Р"


    def withdraw(self, subtraction):

        self._data_verification(subtraction)

        commission = self._commission(subtraction)

        total = subtraction + commission

        self.balance -= total

        return self._message(subtraction, commission)