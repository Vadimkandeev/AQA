class Student:
    students = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.add_student(name)

    @classmethod
    def add_student(cls, name):
        if name not in cls.students:
            cls.students.append(name)

    @classmethod
    def show_students(cls):
        print(cls.students)

    def info(self):
        print(f"Student: {self.name}, age: {self.age}")
