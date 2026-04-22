import pytest
import requests
from constants import BASE_URL, HEADERS,  USER_ENDPOINT

class TestCreateUser:
    def test_create_user(self, test_create_user):

        create_user_url = f"{BASE_URL}{USER_ENDPOINT}"

        response = requests.post(create_user_url, json=test_create_user, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 201, "Ошибка создания пользователя"
        response_data = response.json()
        #Тело ответа, пока, неизвестно. После исправить проверки*************
        assert response_data["email"] == test_create_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"

        # Проверяем, что роль USER назначена по умолчанию
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"