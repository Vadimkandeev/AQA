class Employee:
    def __init__(self, salary, bonus):
        self.salary = salary
        self.bonus = bonus
        self._salary = 0
        self._bonus = 0
    @property
    def salary(self):
        return self._salary + self._bonus


    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)):
            raise TimeoutError("Ошибка ввода данных")
        if value < 0:
            raise ValueError("Размер не может быть меньше нуля")
        self._salary = value



    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        if not isinstance(value, (int, float)):
            raise TimeoutError("Ошибка ввода данных")
        if value < 0:
            raise ValueError("Бонус не может быть меньше нуля")
        if value > self._salary / 2:
            raise ValueError("Бонус не может быть более половины цены")
        self._bonus = value



employee = Employee(2500, 50)

print(employee.salary)


