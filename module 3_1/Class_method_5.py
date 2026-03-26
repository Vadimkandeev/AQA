class Book:
    books = []
    def __init__(self, title):
        self.title = title

    @classmethod
    def add_book(cls, title):
        if title not in  Book.books:
            cls.books.append(title)

    @classmethod
    def show_books(cls):
        print (cls.books)


b1 = Book("War and Peace")
b2 = Book("1984")
b3 = Book("1984")

Book.show_books()