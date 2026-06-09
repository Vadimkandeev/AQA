import pytest_test
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

        response_data = response.json()

        assert response_data["email"] == random_user_by_admin["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"
        assert response_data["verified"] is True, "Верификация пользователя false"

        # Проверяем, что роль USER назначена по умолчанию
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"


    #  Негативная проверка. Неверные данные (нарушение формата токена)
    def test_create_by_invalid_data(self, random_user_by_admin, session_factory):

        invalid_tokens = {
            "accessToken": JUNK_TOKEN,
            "refreshToken": ""
        }

        admin_session = session_factory(invalid_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        requester.send_request("POST", USER_ENDPOINT, random_user_by_admin, 400, True)




