import pytest_test
import requests

from conftest import created_user_by_admin
from constants import BASE_URL, USER_ENDPOINT, PARAMS_FOR_GETLIST
from custom_requester.custom_requester import CustomRequester


class TestGetInformUser:
    # Проводим позитивную проверку. Запрашиваем список пользователей
    def test_get_list_users(self, created_user_by_admin, session_factory, admin_tokens):

        url_get_list_users = f"{USER_ENDPOINT}{PARAMS_FOR_GETLIST}"

        admin_session = session_factory(admin_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        requester.send_request("GET", url_get_list_users, None, 200, True)



    # Проводим Негативную проверку. Нарушение формата параметров
    def test_invalid_get_list_users(self, created_user_by_admin, session_factory, admin_tokens):

        parameters = PARAMS_FOR_GETLIST
        parameters = parameters.replace("2", "F")

        url_get_list_users = f"{USER_ENDPOINT}{parameters}"

        admin_session = session_factory(admin_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        requester.send_request("GET", url_get_list_users, None, 400, True)



    # Проводим невалидный запрос списка пользователей с токеном пользователя вместо админа.
    # Вызов статус-кода 403

    def test_invalid_resp_user_data(self, created_user_by_admin, session_factory, user_tokens):

        url_get_list_users = f"{USER_ENDPOINT}{PARAMS_FOR_GETLIST}"


        admin_session = session_factory(user_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        requester.send_request("GET", url_get_list_users, None, 403, True)
