from calendar import error


# class Pet:
#     name = ""
#     animal_type = ""
#     age = 0
#     is_hungry = True
#
#
# my_pet = Pet()
# my_pet.name = "Bob"
# my_pet.animal_type = "Dog"
# my_pet.age = 2
# my_pet.is_hungry = True
#
# print(f"Имя моей собаки {my_pet.name}")

# class Smartphone:
#     brand = ""
#     model = ""
#     storage = ""
#     battery = ""
#     is_on = False
#
# phone_1 = Smartphone()
# phone_2 = Smartphone()
# phone_3 = Smartphone()
#
# phone_1.brand = "Honor"
# phone_1.model = "12S"
# phone_1.battery = "5500mA/h"
# phone_1.storage = 64
# phone_1.is_on = False
#
#
# phone_2.brand = "Readme"
# phone_2.model = "10Pro"
# phone_2.battery = "5800mA/h"
# phone_2.storage = 128
# phone_2.is_on = True
#
# phone_3.brand = "Samsung"
# phone_3.model = "Galaxy 20pro"
# phone_3.battery = "15500mA/h"
# phone_3.storage = 128
# phone_3.is_on = True
#
# phones = [phone_1, phone_2, phone_3]
#
# for phone in phones:
#     print(f"Марка телефона {phone.brand}")
#     print(f"Модель {phone.model}")
#     print(f"Ёмкость аккумулятора {phone.battery}")
#     print(f"Объем памяти {phone.storage}")
#     if phone.is_on:
#         print("Телефон включен")
#     else:
#         print("Телефон отключен")
#     print()
#     print()

# class Movie:
#     def __init__(self, title, year, genre, rating):
#         self.title = title
#         self.year = year
#         self.genre = genre
#         self.rating = rating
#
# movie = Movie("В джазе только девушки", 1942, "Мьюзикл", 8.2)
#
# movie.rating = 10.1
#
# print(movie.rating)

class ValueAccountError(Exception):
    pass

class Bank_Account:
    def __init__(self, account_number, owner_name, balance, is_active, transaction_count):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.is_active = is_active
        self.transaction_count = transaction_count

    def withdraw(self, subtraction):
        if subtraction <= 0:
            raise ValueError("Сумма должна быть больше нуля")
        if self.balance < subtraction:
            raise ValueAccountError("Недостаточно средства на счету, для проведения операции")
        self.balance -= subtraction
        #self.transaction_count += 1
        return self.balance

    def deposit(self, addition):
        if addition <= 0:
            raise ValueError("Сумма должна быть больше нуля")
        self.balance += addition
        return self.balance

my_account = Bank_Account(500500458, "IVAN IVANOV",500000, True, 10)

try:
    print(my_account.withdraw(70))
except ValueAccountError as err:
    print(err)
except ValueError as err:
    print(err)



# account = Bank_Account(1234567899, "IVAN IVANOV", 360000, True, 0)

# print("==== Начальное состояние====")
# print(f"Номер счета {account.account_number}")
# print(f"Владелец {account.owner_name}")
# print(f"Баланс счета {account.balance}")
# print(f"Количество транзакций{account.is_active}")
# print(f"Активность счета {account.transaction_count}")


# account.balance += 5000
# print(f"Пополнение счета {account.balance}P")
#
# if account.balance >= 3000:
#     account.balance -= 3000
#     print(f"Снятие наличных со счета. Остаток {account.balance}P")


#
# def out_of_change(out_sum):
#     if account.balance < out_sum:
#         raise ValueAccountError("Недостаточно средства на счету, для проведения операции")
#     account.balance -= out_sum
#     return f"Снятие средств со счета {out_sum}, остаток {account.balance}Р"
#
# try:
#     print(out_of_change(2000000))
# except ValueAccountError as err:
#     print(err)




