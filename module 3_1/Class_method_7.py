# class Person:
#     def __init__(self, age):
#         self._age = age
#
#     @property
#     def age(self):
#         return self._age
#------------------------------------------------

# class BankAccount:
#     def __init__(self, balance):
#         self._balance = balance
#
#     @property
#     def balance(self):
#         print("Баланс запрошен")
#         return self._balance
#
# bank_account = BankAccount(255)
#
# print(bank_account.balance)

#------------------------------------------------------
# class DataError(Exception):
#     pass

class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Нарушение формата указания возраста. Только целое число.")
        if value > 150:
            raise ValueError("Возраст не может быть больше 150 лет")
        if value < 0:
            raise ValueError("Возраст не может быть меньше нуля")
        self._age = value



person = Person(25.8)


print(person.age)

