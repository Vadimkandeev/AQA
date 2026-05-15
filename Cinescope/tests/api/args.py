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

default_settings = {"theme": "light", "notifications": True}

def log_kwargs(func):
    def wrapper():
        func()
        return {}

@log_kwargs
def my_function(a, b, **kwargs):
    return a+b

my_function(5, 10, **default_settings)


