import pytest
import requests


from constants import BASE_URL, USER_ENDPOINT, JUNK_TOKEN
from custom_requester.custom_requester import CustomRequester

class TestCreateUser:
    # Создаем пользователя на стороне админа
    def test_create_user(self, random_user_by_admin, auth_admin_headers):

        create_user_url = f"{BASE_URL}{USER_ENDPOINT}"

        admin_session =session_factory(admin_tokens)

        #def send_request(self, method, endpoint, data=None, expected_status=200, need_logging=True):
        response = CustomRequester.send_request(post, USER_ENDPOINT, random_user_by_admin, 201, True)



