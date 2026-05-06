import pytest
import requests

from conftest import created_user_by_admin
from constants import BASE_URL,  USER_ENDPOINT, BODY_FROM_CHANGE_USER_DATA, INVALID_REFRESH_TOKEN


class TestChangeUser:
    def test_change_user_data(self, created_user_by_admin, auth_admin_headers):

        user_id = created_user_by_admin["id"]

        url_from_change_users_data = f"{BASE_URL}{USER_ENDPOINT}/{user_id}"

        response = requests.patch(url_from_change_users_data, data=BODY_FROM_CHANGE_USER_DATA, headers=auth_admin_headers)
        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")


        assert response.status_code == 200, "Ошибка регистрации пользователя"
        response_data = response.json()
        assert response_data["email"] == created_user_by_admin["email"], "Email не совпадает"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"

        # Проверяем, что роль USER назначена по умолчанию
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"


    # Проводим невалидный запрос на изменение данных пользователя с навалидным id. Вызов статус-кода 400
    def test_invalid_change_user_data_by_invalid_id(self, created_user_by_admin, auth_admin_headers):

        user_id = f"{created_user_by_admin["id"]}0"

        url_from_change_users_data = f"{BASE_URL}{USER_ENDPOINT}/{user_id}"

        response = requests.patch(url_from_change_users_data, data=BODY_FROM_CHANGE_USER_DATA, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")


        assert response.status_code == 400, "Ошибка запроса на изменение данных пользователя при id пользователя.\
        Ожидается статус 400"




    # Проводим невалидный запрос на изменение данных пользователя с токеном пользователя вместо админа.
    # Вызов статус-кода 403
    def test_invalid_change_user_data_by_unlegal_token(self, created_user_by_admin, auth_user_headers):

        user_id = created_user_by_admin["id"]

        url_from_change_users_data = f"{BASE_URL}{USER_ENDPOINT}/{user_id}"

        response = requests.patch(url_from_change_users_data, data=BODY_FROM_CHANGE_USER_DATA, headers=auth_user_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        assert response.status_code == 403, "Ошибка запроса на изменение данных пользователя при невалидном токене.\
           Ожидается статус 403"


    # 404 Получить не удается



