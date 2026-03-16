class Test:

    def __init__(self):
        self.__a = 1
        self._b = 2
        self.c = 3


t = Test()

print(t.__dict__)
