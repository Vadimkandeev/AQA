import pytest
import requests
from constants import BASE_URL, HEADERS, LOGOUT_ENDPOINT
from custom_requester.custom_requester import CustomRequester



# Выход из учетной записи и удаление токена
class TestLogout:
    def test_logout_user(self, session_factory, user_tokens):

        # Отправка запрос на разлогин

        user_session = session_factory(user_tokens)

        requester = CustomRequester(user_session, BASE_URL)

        response = requester.send_request("GET", LOGOUT_ENDPOINT, None, 200, True)

        # Проверки

        response_data = response.text
        assert response_data == "OK", "Тело ответа не верно"