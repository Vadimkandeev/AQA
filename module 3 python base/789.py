class A:
    def method(self):
        return "Метод из A"

class B(A):
    def method(self):
        return "Метод из B"

class C(B):
    def another_method(self):
        return "Метод из C"


obj = C()

print(C.__mro__)
