import pytest
import requests
from constants import BASE_URL, HEADERS, REFRESH_TOKENS_ENDPOINT

from custom_requester.custom_requester import CustomRequester



# Обновление токена
class TestRefreshToken:
    def test_refresh_token(self, session_factory, user_tokens ):


        user_session = session_factory(user_tokens)

        requester = CustomRequester(user_session, BASE_URL)

        response =  requester.send_request("GET", REFRESH_TOKENS_ENDPOINT, None, 200, True)

        # Проверки
        response_data = response.json()
        assert "accessToken" in response_data, "accessToken отсутствует в ответе"
        assert response_data["accessToken"], "Пустое значение accessToken"
        assert "refreshToken" in response_data, "refreshToken отсутствует в ответе"


# Негативная проверка обновления токена (вне сессии)
    def test_invalid_refresh_token(self):
        # URL для обновления токена
        refresh_url = f"{BASE_URL}{REFRESH_TOKENS_ENDPOINT}"

        response = requests.get(refresh_url, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 403, "Ошибка обновления токена"
