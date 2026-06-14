import pytest_test
import requests

from conftest import created_user_by_admin
from constants import BASE_URL,  USER_ENDPOINT, BODY_FROM_CHANGE_USER_DATA, HEADERS
from custom_requester.custom_requester import CustomRequester


class TestChangeUser:
    def test_change_user_data(self, created_user_by_admin, session_factory, admin_tokens):

        user_id = created_user_by_admin["id"]

        url_for_change_users_data = f"{USER_ENDPOINT}/{user_id}"

        admin_session = session_factory(admin_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        # def send_request(self, method, endpoint, data=None, expected_status=200, need_logging=True):
        response = requester.send_request("PATCH", url_for_change_users_data, BODY_FROM_CHANGE_USER_DATA,\
                                          200, True)

        response_data = response.json()

        assert response_data["email"] == created_user_by_admin["email"], "Email не совпадает"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"

        # Проверяем, что роль USER назначена по умолчанию
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"


    # Проводим невалидный запрос на изменение данных пользователя с навалидным id. Вызов статус-кода 400
    def test_invalid_change_user_data_by_invalid_id(self, created_user_by_admin, session_factory, admin_tokens):

        user_id = f"{created_user_by_admin["id"]}0"

        url_for_change_users_data = f"{USER_ENDPOINT}/{user_id}"

        admin_session = session_factory(admin_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        # def send_request(self, method, endpoint, data=None, expected_status=200, need_logging=True):
        requester.send_request("PATCH", url_for_change_users_data, BODY_FROM_CHANGE_USER_DATA,  400, True)






    # Проводим невалидный запрос на изменение данных пользователя с токеном пользователя вместо админа.
    # Вызов статус-кода 403
    def test_invalid_change_user_data_by_unlegal_token(self, created_user_by_admin, session_factory, user_tokens):

        user_id = created_user_by_admin["id"]

        url_for_change_users_data = f"{USER_ENDPOINT}/{user_id}"

        session = requests.Session()
        session.headers.update(HEADERS)
        session.headers.update({"Authorization": f"Bearer {user_tokens['accessToken']}"})

        requester = CustomRequester(session, BASE_URL)

        # def send_request(self, method, endpoint, data=None, expected_status=200, need_logging=True):
        requester.send_request("PATCH", url_for_change_users_data, BODY_FROM_CHANGE_USER_DATA, 403, True)



