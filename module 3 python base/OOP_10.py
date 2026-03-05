class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Человек: {self.name}"


class Student(Person):
    def __init__(self, name, age, university):
        self.name = name
        self.age = age
        self.university = university

    def __str__(self):  # Переопределяем магический метод!
        return f"Студент: {self.name}, учится в {self.university}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def __str__(self):  # Переопределяем магический метод!
        return f"Преподаватель: {self.name}, предмет: {self.subject}"



people = [
    Person("Алексей", 30),
    Student("Мария", 20, "МГУ"),
    Teacher("Елена", 35, "Математика")
]

for person in people:
    print(person)  # Вызывается переопределенный __str__ для каждого типа