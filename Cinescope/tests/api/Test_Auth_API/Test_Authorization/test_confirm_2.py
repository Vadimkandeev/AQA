import pytest_test
import requests
from constants import BASE_URL, HEADERS,  CONFIRM_ENDPOINT
from custom_requester.custom_requester import CustomRequester

# Подтверждение email
class TestConfirmEmail:
    def test_confirm_user_email(self, random_user_by_user, created_user_by_user, session_factory, user_tokens):

        # URL для подтверждения email
        token = user_tokens["accessToken"]
        confirm_url = f"{BASE_URL}{CONFIRM_ENDPOINT}/{token}"

        user_session = session_factory(user_tokens)

        requester = CustomRequester(user_session, BASE_URL)

        response = requester.send_request("GET", confirm_url, None, 200, True)

        response_data = response.json()
        assert "accessToken" in response_data, "accessToken отсутствует в ответе"
        assert response_data["accessToken"], "Пустое значение accessToken"
        assert "refreshToken" in response_data, "refreshToken отсутствует в ответе"
