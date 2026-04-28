import pytest
import requests
from constants import BASE_URL, HEADERS, LOGIN_ENDPOINT

# Аутентификация пользователя
class TestAuth:
        def test_authentication_user(self, created_user_by_user, random_user_by_user):
            # URL для аутентификации
            authentication_url = f"{BASE_URL}{LOGIN_ENDPOINT}"
            body = {"email": random_user_by_user["email"], "password": random_user_by_user["password"]}

            # Отправка запроса для аутентификации
            response = requests.post(authentication_url, json=body, headers=HEADERS)

            # Логируем ответ для диагностики
            print(f"Response status: {response.status_code}")
            print(f"Response body: {response.text}")

            # Проверки
            assert response.status_code == 200, "Ошибка аутентификации пользователя"
            response_data = response.json()
            assert response_data["user"]["email"] == random_user_by_user["email"], "Email не совпадает"
            assert "id" in response_data["user"], "ID пользователя отсутствует в ответе"
            assert "roles" in response_data["user"], "Роли отсутствуют в ответе"
            assert "USER" in response_data["user"]["roles"], "Роль пользователя отсутствует в ответе"
            assert "accessToken" in response_data, "accessToken отсутствует в ответе"
            assert response_data["accessToken"], "Пустое значение accessToken"
            assert "refreshToken" in response_data, "refreshToken отсутствует в ответе"
            assert response_data["refreshToken"], "Пустое значение refreshToken"
