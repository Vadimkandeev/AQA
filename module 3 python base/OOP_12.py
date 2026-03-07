class DataError(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, addition):
        if addition <= 0:
            raise ValueError("Сумма должна быть больше нуля")
        self.balance += addition
        return f"Пополнение на {addition}Р, баланс {self.balance}P."

    def _data_verification(self, subtraction):
        if subtraction <= 0:
            raise ValueError("Сумма должна быть больше нуля")

    def _commission(self, subtraction):
        return 0

    def _message(self, subtraction, commission_sum):
        return f"Снятие средств в сумме {subtraction}Р, в том числе комиссия: {commission_sum}. Баланс {self.balance}Р"

    def withdraw(self, subtraction):
        self._data_verification(subtraction)
        commission_sum = self._commission(subtraction)
        total = subtraction + commission_sum
        if self.balance < total:
            raise DataError("На счету недостаточно средств.")
        self.balance -= total
        return  self._message(subtraction, commission_sum)
#-------------------------------------------------------------------------

class SavingAccount(BankAccount):
    def _commission(self, subtraction):
        return subtraction * 0.01
#------------------------------------------------------------------------

class CheckingAccount(BankAccount):
    def _commission(self, subtraction):
        if subtraction < 1000:
            return 0
        return subtraction * 0.02
#------------------------------------------------------------------------

class PremiumAccount(BankAccount):
    def _commission(self, subtraction):
        if self.balance >= 10000:
            return 0
        else:
            return subtraction * 0.03