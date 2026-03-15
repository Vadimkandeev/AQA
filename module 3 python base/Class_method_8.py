class User:
    users = {}
    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.register_user(username, age)

    @classmethod
    def register_user(cls, username, age):
        if username not in cls.users:
            value = {}
            value["age"] = age
            cls.users[username] = value
        else:
            print(f"Пользователь {username} уже зарегистрирован в системе")


    @classmethod
    def show_users(cls):
        print(cls.users)


    def get_info(self):
        return f"User {self.username}, age {self.age}"



user = User()