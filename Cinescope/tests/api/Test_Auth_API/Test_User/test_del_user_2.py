import pytest_test
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

        response = requester.send_request("DELETE", delete_user_url, None, 200, True)





    # Проводим негативный тест по удалению пользователя. Удаляем уже удаленного пользователя. Ожидается 404
    def test_del_user_not_found(self, random_user_by_admin, auth_admin_headers, created_user_by_admin, session_factory, admin_tokens):
        user_id = created_user_by_admin["id"]

        delete_user_url = f"{BASE_URL}{USER_ENDPOINT}/{user_id}"

        admin_session = session_factory(admin_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        requests.delete(delete_user_url, headers=auth_admin_headers)
        requester.send_request("DELETE", delete_user_url, None, 404, True)



    # Проводим негативный тест по удалению пользователя. С барер токеном пользователя вместо админа. Ожидается 403
    def test_del_user_by_illegal_token(self, random_user_by_admin, auth_user_headers, created_user_by_admin, session_factory, user_tokens):
        user_id = created_user_by_admin["id"]

        delete_user_url = f"{BASE_URL}{USER_ENDPOINT}/{user_id}"

        admin_session = session_factory(user_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        requester.send_request("DELETE", delete_user_url, None, 403, True)

        