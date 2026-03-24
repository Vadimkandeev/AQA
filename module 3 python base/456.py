class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def print_val(self):
        return f"Книга: {self.title} (автор: {self.author})"

    # def __str__(self):
    #     return f"Книга: {self.title} (автор: {self.author})"
    #
    # def __repr__(self):
    #     return f"Book('{self.title}', '{self.author}')"


book = Book("Война и мир", "Толстой")

print(str(book))  # Книга: Война и мир (автор: Толстой)  ← для людей
print(repr(book))  # Book('Война и мир', 'Толстой')       ← для программистов