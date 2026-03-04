class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        return f"{self.name} работает как {self.position}"


class Programmer(Employee):
    def code(self):
        return f"{self.name} Пишет код"

    def debug(self):
        return f"{self.name} Изет баги"

    def commit(self):
        return f"{self.name} Делает коммит в Git"

class Desinger(Employee):
    def design(self):
        return f"{self.name} создает дизайн"

    def prototype(self):
        return f"{self.name} делает прототип"

    def present(self):
        return f"{self.name} презентует идею"


prog = Programmer("Ivan", "Boxer")

desinger = Desinger("Piter", "Wheeller")

print(prog.work())
print(prog.code())
print(prog.debug())
print(prog.commit())

