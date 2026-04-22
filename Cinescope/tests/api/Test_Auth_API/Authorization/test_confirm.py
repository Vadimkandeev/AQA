import pytest
import requests
from constants import BASE_URL, HEADERS,  CONFIRM_ENDPOINT


# Подтверждение email
class TestConfirmEmail:
    def test_confirm_user_email(self,  test_user, created_user, tokens):

        # URL для подтверждения email
        token = tokens["accessToken"]
        confirm_url = f"{BASE_URL}{CONFIRM_ENDPOINT}/{token}"

        response = requests.get(confirm_url, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки нужно переписать. Так как всегда возвращается ответ 401, нет возможности увидеть
        # валидное тело ответа
        assert response.status_code == 200, "Ошибка обновления токена"
        response_data = response.json()
        assert "accessToken" in response_data, "accessToken отсутствует в ответе"
        assert response_data["accessToken"], "Пустое значение accessToken"
        assert "refreshToken" in response_data, "refreshToken отсутствует в ответе"






