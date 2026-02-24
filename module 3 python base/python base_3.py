# def greet():
#     print('Hello world')
#
# greet()

# def greet_user(name):
#     print(f'Привет {name}')
#     print('Привет', name)
#     print('Привет ' + name)
#
# greet_user('Вадим')
#
# def sum_numbers(a, b):
#     print(a+b)
#
# sum_numbers(10, 15)

# def is_even(number):
#     if number == 0:
#         print('На ноль делить нельзя')
#     elif number % 2 == 1:
#         print('Нечетное')
#     else:
#         print('Четное')
#
#
# is_even(0)

# def rectangle_area(width, height):
#     if width <= 0 or height <= 0:
#         print('Некорректные значения')
#     else:
#         print(f'Площадь прямоугольника {width * height}')
#
# rectangle_area(17, 22)

# def greet_person(name='Анна', age='18'):
#     print(f'Привет, {name}! Тебе {age} лет.')
#
#
# #greet_person(name = 'Вадим', age = 50)
#
# greet_person()

# def circle_area(radius, pi = 3.14159):
#     print(f"Площадь круга составляет {(pi * radius) ** 2}.")
#
# circle_area(500, 3.14)
#
# circle_area(500)

# def book_info(title, author, year, genre = 'Неизвестно'):
#     print(f'Название: {title}')
#     print(f'Автор: {author}')
#     print(f'Год издания: {year}')
#     print(f'Жанр: {genre}')
#
# book_info('Незнайка на Луне', 'Носов', '1972', 'Сказки')
#
# book_info('Незнайка на Луне', 'Носов', '1972')

# def convert_currency(amount, rate, from_currency='USD', to_currency='EUR'):
#     print(f'{amount} {from_currency} = {amount * rate} {to_currency}')
#
#
# convert_currency(511, 10.9)
#
# convert_currency(from_currency='UZS', rate=0.02, amount=11322)

# def read_text_file(path: str) -> str:
#     with open(path, "r", encoding="utf-8") as file:
#         context = file.read()
#     try:
#
#     except:
#         if

# def read_text_file(path: str) -> str:
#     if path == "":
#         return "Имя файла не может быть пустым"
#     try:
#         with open(path, "r", encoding="utf-8") as file:
#             return file.read()
#     except FileNotFoundError:
#         return "Файл не найден, проверьте правильность пути"
#
#
#
# print( read_text_file("e:/55.txt"))


# def divide_numbers(my_list):
#     n_list = []
#     for i in range(len(my_list)):
#         try:
#             n_list.append(100 / int(my_list[i]))
#         except ZeroDivisionError:
#             continue
#         except ValueError:
#             continue
#     return n_list
#
# print(divide_numbers(['10', '100', '0', 'g', '500']))


# def int_num(my_list:list):
#     finish_list = []
#     for i in range(len(my_list)):
#         try:
#             int(my_list[i])
#             finish_list.append(my_list[i])
#         except:
#             continue
#     return finish_list
#
# print(int_num(["werwe", "f", "5.8", "44", "22", "rr", "1225"]))


# def num_index(my_list:list, a:int):
#     try:
#         return my_list[a]
#     except IndexError:
#         return "Индекс вне диапазона"
#
#
# print(num_index(["werwe", "f", "5.8", "44", "22", "rr", "1225"], 15))

# def func_1(my_list:list):
#     my_sum = 0
#     for elememt in my_list:
#         try:
#             my_sum += int(elememt)
#         except ValueError:
#             continue
#     return my_sum
#
# print(func_1(["werwe", "f", "5.8", "44", "22", "rr", "1", "14", "****", "1sdf", "25.8", "17"]))



# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError("На ноль делить нельзя!")  # Генерируем исключение
#     return a / b
#
# try:
#     print(divide(10, 0))
# except ZeroDivisionError as e:
#     print("Ошибка:", e)