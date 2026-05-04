import pytest
import requests
from constants import BASE_URL, USER_ENDPOINT, JUNK_TOKEN

class TestCreateUser:
    # Создаем пользователя на стороне админа
    def test_create_user(self, random_user_by_admin, auth_admin_headers):

        create_user_url = f"{BASE_URL}{USER_ENDPOINT}"

        response = requests.post(create_user_url, json=random_user_by_admin, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 201, "Ошибка создания пользователя"
        response_data = response.json()

        assert response_data["email"] == random_user_by_admin["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"
        assert response_data["verified"] is True, "Верификация пользователя false"

        # Проверяем, что роль USER назначена по умолчанию
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"



    #  Негативная проверка. Неверные данные (нарушение формата токена)
    def test_create_by_invalid_data(self, random_user_by_admin, auth_admin_headers):
        create_user_url = f"{BASE_URL}{USER_ENDPOINT}"
        invalid_headers = auth_admin_headers
        invalid_headers["Authorization"] = JUNK_TOKEN

        response = requests.post(create_user_url, json=random_user_by_admin, headers=invalid_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 400, "Ошибка негативного теста с неверными данными"


