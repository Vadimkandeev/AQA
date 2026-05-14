def greet(**kwargs):
    print(f"Hello, {kwargs["name"]}! You are {kwargs["age"]} years old.")
    print(kwargs)



greet(name="Alice", age=25)