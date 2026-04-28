import pytest
import requests

from conftest import created_user_by_admin
from constants import BASE_URL, USER_ENDPOINT


class TestGetInformUser:
    def test_get_inform_user_email(self, created_user_by_admin, auth_user_headers):
        email = created_user_by_admin["email"]
        email = email.replace("@", "%")

        get_inform_url_email = f"{BASE_URL}{USER_ENDPOINT}/{email}"

        response = requests.get(get_inform_url_email, headers=auth_user_headers)
        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки нужно править. Нет валидного тела ответа
        assert response.status_code == 201, "Ошибка регистрации пользователя"
        response_data = response.json()
        assert response_data["email"] == created_user_by_admin["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"

        # Проверяем, что роль USER назначена по умолчанию
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"


    def test_get_inform_user_id(self, created_user_by_admin, auth_user_headers):
        user_id = created_user_by_admin["id"]

        get_inform_url_user_id = f"{BASE_URL}{USER_ENDPOINT}/{user_id}"

        response = requests.get(get_inform_url_user_id, headers=auth_user_headers)
        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки нужно править. Нет валидного тела ответа
        assert response.status_code == 201, "Ошибка регистрации пользователя"
        response_data = response.json()
        assert response_data["email"] == created_user_by_admin["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"

        # Проверяем, что роль USER назначена по умолчанию
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"
