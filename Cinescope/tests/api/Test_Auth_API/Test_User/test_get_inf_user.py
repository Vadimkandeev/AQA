import pytest
import requests
from constants import BASE_URL, HEADERS,  REGISTER_ENDPOINT


class TestGetInformUser:
    def test_get_inform_user_email(self, test_create_user):
        email = test_create_user["email"]

        get_inform_url_email = f"{BASE_URL}{REGISTER_ENDPOINT}/{email}"

        response = requests.get(get_inform_url_email, headers=HEADERS)
        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки нужно править. Нет валидного тела ответа
        assert response.status_code == 201, "Ошибка регистрации пользователя"
        response_data = response.json()
        assert response_data["email"] == test_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"

        # Проверяем, что роль USER назначена по умолчанию
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"


    def test_get_inform_user_id(self):
        # Получаем id
        # id =

        get_inform_url_id = f"{BASE_URL}{REGISTER_ENDPOINT}/{id}"

        response = requests.get(get_inform_url_id, headers=HEADERS)
        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки нужно править. Нет валидного тела ответа
        assert response.status_code == 201, "Ошибка регистрации пользователя"
        response_data = response.json()
        assert response_data["email"] == test_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"

        # Проверяем, что роль USER назначена по умолчанию
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"
