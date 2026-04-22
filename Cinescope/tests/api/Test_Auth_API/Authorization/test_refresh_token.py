import pytest
import requests
from constants import BASE_URL, HEADERS, REFRESH_TOKENS_ENDPOINT



# Обновление токена
class TestRefreshToken:
    def test_refresh_token(self, test_user, created_user):
        # URL для обновления токена
        refresh_url = f"{BASE_URL}{REFRESH_TOKENS_ENDPOINT}"

        response = requests.get(refresh_url, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 200, "Ошибка обновления токена"
        response_data = response.json()
        assert "accessToken" in response_data, "accessToken отсутствует в ответе"
        assert response_data["accessToken"], "Пустое значение accessToken"
        assert "refreshToken" in response_data, "refreshToken отсутствует в ответе"

