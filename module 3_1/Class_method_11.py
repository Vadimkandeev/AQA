class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius



    @property
    def celsius(self):
        return f"Текущая температура: {self._celsius}°C"


    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Слишком холодно!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return f"Текущая температура: {(9/5) * self._celsius + 32}°F"



# Попробуйте запустить этот код:
temp = Temperature(25)
print(temp.celsius)
print(temp.fahrenheit)
