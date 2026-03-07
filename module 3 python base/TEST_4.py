# class Parent:
#     def greet(self):
#         return f"Привет от {self.__class__.__name__}"
#
# class Child(Parent):
#     def greet(self):
#         return super().greet() + " через Child"
#
# obj = Child()
# print(obj.greet())  # Привет от Child через Child


# class Parent:
#     def greet(self):
#         return "Привет от родителя"
#
#
# class Child(Parent):
#     def greet(self):
#         # Способ 1: Прямое обращение к классу (устаревший, НЕ рекомендуется)
#         result1 = Parent.greet(self)
#
#         # Способ 2: Через super() (рекомендуется)
#         result2 = super().greet()
#
#         # Способ 3: Расширение функциональности
#         result3 = super().greet() + " и от ребенка"
#
#         return result3


# class A:
#     def method(self):
#         return "A"
#
# class B(A):
#     def method(self):
#         return A.method(self) + " -> B"  # Жестко привязано к A
#
# class C(B):
#     def method(self):
#         return A.method(self) + " -> C"  # Пропускаем B!
#
# obj = C()
# print(obj.method())  # A -> C (потеряли B!)



class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return super().method() + " -> B"

class C(B):
    def method(self):
        return super().method() + " -> C"

obj = C()
print(obj.method())  # A -> B -> C (правильно!)