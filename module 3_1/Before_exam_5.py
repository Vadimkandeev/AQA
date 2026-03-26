class Peon:
    def __init__(self):
        pass

    def work(self):
        return f"Собирает золото"


class Knight:
    def __init__(self):
        pass

    def work(self):
        return f"Сражается с врагами"

peon = Peon()
knight = Knight()

def daily_work(any_class):
    print(any_class.work())

daily_work(peon)
daily_work(knight)
