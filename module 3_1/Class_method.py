class LibraryBook:
    library = {}
    def __init__(self, title, count):
        self.count = count
        self.title = title
        self.add_book(title, count)

    @classmethod
    def add_book(cls, title, count):
        value = {"available": count}
        if title not in cls.library:
            cls.library[title] = value
        else:
            cls.library[title]["available"] += count

    @classmethod
    def borrow_book(cls, title):
        if title in cls.library and cls.library[title]["available"] >= 1:
            cls.library[title]["available"] -= 1
        elif title not in cls.library:
            print(f"Книги {title} не существует в каталоге")

    @classmethod
    def show_library(cls):
        print(cls.library)