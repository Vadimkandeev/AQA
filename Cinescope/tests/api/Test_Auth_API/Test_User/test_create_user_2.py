import pytest
import requests


from constants import BASE_URL, USER_ENDPOINT, JUNK_TOKEN
from custom_requester.custom_requester import CustomRequester

class TestCreateUser:
    # Создаем пользователя на стороне админа
    def test_create_user(self, random_user_by_admin, session_factory, admin_tokens):

        admin_session =session_factory(admin_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        #def send_request(self, method, endpoint, data=None, expected_status=200, need_logging=True):
        response = requester.send_request("POST", USER_ENDPOINT, random_user_by_admin, 201, True)


    #  Негативная проверка. Неверные данные (нарушение формата токена)
    def test_create_by_invalid_data(self, random_user_by_admin, session_factory):

        invalid_tokens = {
            "accessToken": JUNK_TOKEN,
            "refreshToken": ""
        }

        admin_session = session_factory(invalid_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        response = requester.send_request("POST", USER_ENDPOINT, random_user_by_admin, 400, True)




