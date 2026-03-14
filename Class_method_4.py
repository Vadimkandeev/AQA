class Book:
    count = 0
    def __init__(self):
        Book.count += 1

    @classmethod
    def total_book(cls):
        return cls.count

print(Book.count)
