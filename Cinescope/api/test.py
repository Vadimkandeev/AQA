def numbers():
    print("Начало")
    yield 5
    print("Конец")

gen = numbers()

print(next(gen))

