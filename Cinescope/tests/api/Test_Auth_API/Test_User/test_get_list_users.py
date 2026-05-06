import pytest
import requests

from conftest import created_user_by_admin
from constants import BASE_URL, USER_ENDPOINT, PARAMS_FOR_GETLIST


class TestGetInformUser:
    # Проводим позитивную проверку. Запрашиваем список пользователей
    def test_get_list_users(self, created_user_by_admin, auth_admin_headers):

        url_get_list_users = f"{BASE_URL}{USER_ENDPOINT}{PARAMS_FOR_GETLIST}"

        response = requests.get(url_get_list_users, headers=auth_admin_headers)
        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверка получения статус-кода. Ожидается 200
        assert response.status_code == 200, "Ошибка запроса списка пользователей"



    # Проводим Негативную проверку. Нарушение формата параметров
    def test_invalid_get_list_users(self, created_user_by_admin, auth_admin_headers):

        parameters = PARAMS_FOR_GETLIST
        parameters = parameters.replace("2", "F")


        url_get_list_users = f"{BASE_URL}{USER_ENDPOINT}{parameters}"

        response = requests.get(url_get_list_users, headers=auth_admin_headers)
        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверка получения статус-кода. Ожидается 400
        assert response.status_code == 400, "Ошибка валидации. Ожидается статус-код 400"



    # Проводим невалидный запрос списка пользователей с токеном пользователя вместо админа.
    # Вызов статус-кода 403

    def test_invalid_resp_user_data(self, created_user_by_admin, auth_user_headers):

        url_get_list_users = f"{BASE_URL}{USER_ENDPOINT}{PARAMS_FOR_GETLIST}"

        response = requests.get(url_get_list_users, headers=auth_user_headers)
        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверка получения статус-кода. Ожидается 403
        assert response.status_code == 403, "Ошибка запроса списка пользователей при невалидном токене.\
              Ожидается статус 403"
