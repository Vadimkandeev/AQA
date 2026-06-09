import pytest_test
import requests

from conftest import created_user_by_admin
from constants import BASE_URL, USER_ENDPOINT
from custom_requester.custom_requester import CustomRequester


class TestGetInformUser:
    def test_get_inform_user_email(self, created_user_by_admin, session_factory, admin_tokens):
        email = created_user_by_admin["email"]
        email = email.replace("@", "%")

        get_inform_url_email = f"{BASE_URL}{USER_ENDPOINT}/{email}"

        admin_session = session_factory(admin_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        response = requester.send_request("GET", get_inform_url_email, None, 200, True)

        response_data = response.json()
        assert response_data["email"] == created_user_by_admin["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"

        # Проверяем, что роль USER назначена по умолчанию
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"





    # Проводим невалидный запрос на изменение данных пользователя с токеном пользователя вместо админа.
    # Вызов статус-кода 403
    def test_invalid_resp_user_data(self, created_user_by_admin, user_tokens, session_factory):

        user_id = created_user_by_admin["id"]

        url_from_get_user_data = f"{BASE_URL}{USER_ENDPOINT}/{user_id}"

        admin_session = session_factory(user_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        requester.send_request("GET", url_from_get_user_data, None, 403, True)
