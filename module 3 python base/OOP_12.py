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

    def withdraw(self, subtraction):
        if subtraction <= 0:
            raise ValueError("Сумма должна быть больше нуля")
        elif self.balance < subtraction:
            raise DataError("На счету недостаточно средств. Уменьшите сумму снятия")
        self.balance -= subtraction
        return f"Снятие средств в сумме {subtraction}Р, баланс {self.balance}Р"

#-------------------------------------------------------------------------

class SavingAccount(BankAccount):

    def withdraw(self, subtraction):
        if subtraction <= 0:
            raise ValueError("Сумма должна быть больше нуля")
        elif self.balance < subtraction:
            raise DataError("На счету недостаточно средств. Уменьшите сумму снятия")
        self.balance -= (subtraction + subtraction * 0.01)
        return f"Снятие средств в сумме {subtraction}Р,  в том числе комиссия 1% ({subtraction*0.1})P, баланс {self.balance}Р"

#------------------------------------------------------------------------

class CheckingAccount(BankAccount):

    def __init__(self, balance):
        super().__init__(balance)


    def withdraw(self, subtraction):
        commission = 0
        if subtraction <= 0:
            raise ValueError("Сумма должна быть больше нуля")
        elif self.balance < subtraction:
            raise DataError("На счету недостаточно средств. Уменьшите сумму снятия")
        if subtraction < 1000:
            self.balance -= subtraction
        else:
            commission = subtraction * 0.02
            self.balance -= (subtraction + commission)
        return f"Снятие средств в сумме {subtraction}Р, в том числе {commission}Р комиссии, баланс {self.balance}Р"

#------------------------------------------------------------------------

class PremiumAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)


    def withdraw(self, subtraction):
        commission = 0
        if subtraction <= 0:
            raise ValueError("Сумма должна быть больше нуля")
        elif self.balance < subtraction:
            raise DataError("На счету недостаточно средств. Уменьшите сумму снятия")
        if self.balance >= 10000:
            self.balance -= subtraction
        else:
            commission = subtraction * 0.02
            self.balance -= (subtraction + commission)
        return f"Снятие средств в сумме {subtraction}Р, в том числе {commission}Р комиссии, баланс {self.balance}Р"

