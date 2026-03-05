class Notification:
    def __init__(self, message, recipient):
        self.message = message
        self.recipient = recipient

    def send(self):
        return f"{self.message}, {self.recipient}.  Это сообщение - заглушка для проверки материнского скласса"


class EmailNotification(Notification):
    # def __init__(self, message, recipient):
    #     self.message = message
    #     self.recipient = recipient


    def send(self):
        return f"Отправка email для {self.recipient}: {self.message}"



class SMSNotification(Notification):
    # def __init__(self, message, recipient):
    #     self.message = message
    #     self.recipient = recipient

    def send(self):
        return f"Отправка SMS на номер {self.recipient}: {self.message}"




class PushNotification(Notification):
    # def __init__(self, message, recipient):
    #     self.message = message
    #     self.recipient = recipient

    def send(self):
        return f"Push-уведомление для {self.recipient}: {self.message}"



notifications = [
    EmailNotification("Добро пожаловать!", "user@example.com"),
    SMSNotification("Код подтверждения: 1234", "+7-999-123-45-67"),
    PushNotification("У вас новое сообщение", "user_123"),
    Notification("Общее уведомление", "admin")  # базовый класс
]

for notification in notifications:
    print(notification.send())