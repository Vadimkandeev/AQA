# def greet(**kwargs):
#     print(f"Hello, {kwargs["name"]}! You are {kwargs["age"]} years old.")
#     print(kwargs)
#
# greet(name="Alice", age=25)

# default_settings = {"theme": "light", "notifications": True}
#
# def update_settings(settings, **kwargs):
#     settings.update(kwargs)
#     return settings
#
#
# print(update_settings(default_settings, theme="dark", volume=80))


# def filter_kwargs(**kwargs):
#     filtered = {
#         key: value
#         for key, value in kwargs.items()
#         if value > 10
#     }
#     return filtered
#
# print(filter_kwargs(a=5, b=20, c=15, d=3))

#default_settings = {"theme": "light", "notifications": True}

def log_kwargs(func):
    def wrapper(a, b, **kwargs):
        res = func(a, b, **kwargs)
        return res
    return wrapper

# @log_kwargs
# def my_function(a, b, **kwargs):
#     return kwargs
#
# print(my_function(5, 10, theme="light", notifications=True))

# def my_decor(func):
#     def wrapper(*args, **kwargs):
#         print("function is run")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @my_decor
# def my_function(a, b):
#     return a + b
#
# print(my_function(5, 10))


def my_decor(func):
    def wrapper(*args, **kwargs):
        print("START")
        result = func(*args, **kwargs)
        print(result)
        print("FINISH")
        return result

    return wrapper

@my_decor
def my_func(a, b, c):
    return a+b+c


my_func(2,6,999)



