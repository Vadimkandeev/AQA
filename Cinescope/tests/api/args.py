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


# def my_decor(func):
#     def wrapper(*args, **kwargs):
#         #print("START")
#         result = func(*args, **kwargs)
#         #print(result)
#         #print("FINISH")
#         return f"START\n{result}\nFINISH"
#
#     return wrapper
#
# @my_decor
# def my_func(a, b, c):
#     return a+b+c

#print (my_func(2,6,999))


# def my_decor(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         return args
#     return wrapper
#
# @my_decor
# def my_function(*args, **kwargs):
#     return kwargs, args
#
#
# print(my_function(10, 50, "8555", name="Ivan", age=30))


# def my_decor(func):
#     def wrapper(x):
#         #func(x)
#         return func(x).upper()
#     return wrapper
#
# @my_decor
# def print_srting(x):
#     return x.lower()
#
# print(print_srting("dddddddddddddDDDDDDDDDDDDDlllllllllllllll"))


# def my_decor(func):
#     def wrapper(*args):
#         my_list = list(func(*args))
#         return my_list
#     return wrapper
#
# @my_decor
# def my_tuple(*args):
#     return args
#
# print(my_tuple(1, 10, 45, "55", "dfdf"))


def my_decor(func):
    def wrapper(*args):
        my_tuple = func(*args)
        return max(my_tuple)
    return wrapper


@my_decor
def my_tuple(*args):
    return args

print(my_tuple(10,2,5,122,522,612,1451,21,266,2112,94444,52))



def my_decor(func):
    def wrapper(*args):
        my_tuple = func(*args)
        return " ".join(my_tuple)
    return wrapper


@my_decor
def my_tuple(*args):
    return args

print(my_tuple("1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","d"))