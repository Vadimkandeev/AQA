import pytest
import requests
from constants import BASE_URL,  USER_ENDPOINT
from custom_requester.custom_requester import CustomRequester


class TestDelUser:
    # Проводим позитивный тест по удалению пользователя.
    def test_del_user(self, random_user_by_admin, created_user_by_admin, session_factory, admin_tokens):

        user_id = created_user_by_admin["id"]

        delete_user_url = f"{BASE_URL}{USER_ENDPOINT}/{user_id}"

        admin_session = session_factory(admin_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        response = requester.send_request("DELETE", delete_user_url, None, 201, True)

        response_data = response.json()


        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 200, "Ошибка удаления пользователя"



    # Проводим негативный тест по удалению пользователя. Удаляем уже удаленного пользователя. Ожидается 404
    def test_del_user_not_found(self, random_user_by_admin, auth_admin_headers, created_user_by_admin):

        user_id = created_user_by_admin["id"]
        delete_user_url = f"{BASE_URL}{USER_ENDPOINT}/{user_id}"

        requests.delete(delete_user_url, headers=auth_admin_headers)
        response = requests.delete(delete_user_url, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 400, "Ошибка удаления. Ожидается статус-код 404"



    # Проводим негативный тест по удалению пользователя. С барер токеном пользователя вместо админа. Ожидается 403
    def test_del_user_by_illegal_token(self, random_user_by_admin, auth_user_headers, created_user_by_admin):

        user_id = created_user_by_admin["id"]
        delete_user_url = f"{BASE_URL}{USER_ENDPOINT}/{user_id}"

        response = requests.delete(delete_user_url, headers=auth_user_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 403, "Ошибка удаления пользователя. Ожидается 403"
