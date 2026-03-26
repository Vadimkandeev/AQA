class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_stirng(cls, input_string):
        name, age = input_string.split(":")
        return cls(name, int(age))


