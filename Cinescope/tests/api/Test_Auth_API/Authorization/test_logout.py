import pytest
import requests
from constants import BASE_URL, HEADERS, LOGOUT_ENDPOINT



# Выход из учетной записи и удаление токена
class TestLogout:
    def test_logout_user(self, test_user, created_user):
        # URL для выхода из четной записи
        logout_url = f"{BASE_URL}{LOGOUT_ENDPOINT}"

        # Отправка запрос на разлогин
        response = requests.get(logout_url, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 200, "Ошибка выхода из учетной записи"
        response_data = response.json()
        assert response_data == "OK", "Тело ответа не верно"


