class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Man {self.name}"


class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def __str__(self):
        return f"Student {self.name} is studie in {self.university}"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def __str__(self):
        return f"The teacher {self.name}, предмет {self.subject}"



people = [
    Person("Алексей", 30),
    Student("Мария", 20, "МГУ"),
    Teacher("Елена", 35, "Математика")
]

for person in people:
    print(person)  # Вызывается переопределенный __str__ для каждого типа