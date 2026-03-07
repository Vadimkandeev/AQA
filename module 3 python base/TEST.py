class DataError(Exception):
    pass


class BankAccount:

    def __init__(self, balance):
        self.balance = balance
#--------------------------------------------------

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть больше нуля")

        self.balance += amount
        return f"Пополнение на {amount}Р, баланс {self.balance}Р"
#--------------------------------------------------
#************************************************************
#************************************************************
    def _validate(self, amount):

        if amount <= 0:
            raise ValueError("Сумма должна быть больше нуля")

        if self.balance < amount:
            raise DataError("Недостаточно средств")

#----------------------------------------------------

    def _get_fee(self, amount):
        return 0
#-------------------------------------------------


    def withdraw(self, amount):

        self._validate(amount)

        total = amount + self._get_fee(amount)

        self.balance -= total

        return f"Снятие {amount}Р, комиссия {total - amount}Р, баланс {self.balance}Р"
#------------------------------------------------------------------------------

#---------------------------------------------------------------------------



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