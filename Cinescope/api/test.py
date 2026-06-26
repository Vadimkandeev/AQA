def numbers():
    yield "Начало"
    yield "Средина"
    yield "Конец"
    yield "Вторник"


gen = numbers()

print(next(gen))



