import pytest
import requests
from constants import BASE_URL, HEADERS, REGISTER_ENDPOINT, CONFIRM_ENDPOINT, LOGIN_ENDPOINT, LOGOUT_ENDPOINT,REFRESH_TOKENS_ENDPOINT

# Регистрация нового пользователя
class TestRegistration:
    def test_register_user(self, test_user):
        # URL для регистрации
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

        # Отправка запроса на регистрацию
        response = requests.post(register_url, json=test_user, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 201, "Ошибка регистрации пользователя"
        response_data = response.json()
        assert response_data["email"] == test_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"

        # Проверяем, что роль USER назначена по умолчанию
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"


    # def test_email_confirmation(self, test_user):
    #     # URL для подтверждения
    #     register_url = f"{BASE_URL}{CONFIRM_ENDPOINT}"
    #
    #     # Отправка запроса на подтверждение
    #     response = requests.get(register_url, headers=HEADERS)
    #
    #     # Логируем ответ для диагностики
    #     print(f"Response status: {response.status_code}")
    #     print(f"Response body: {response.text}")
    #
    #     # Проверки
    #     assert response.status_code == 201, "Ошибка регистрации пользователя"
    #     response_data = response.json()
    #     assert response_data["email"] == test_user["email"], "Email не совпадает"
    #     assert "id" in response_data, "ID пользователя отсутствует в ответе"
    #     assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"
    #
    #     # Проверяем, что роль USER назначена по умолчанию
    #     assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"




class TestAuth:
        def test_authentication_user(self, created_user, test_user):
            # URL для аутентификации
            authentication_url = f"{BASE_URL}{LOGIN_ENDPOINT}"
            body = {"email": test_user["email"], "password": test_user["password"]}

            # Отправка запроса для аутентификации
            response = requests.post(authentication_url, json=body, headers=HEADERS)

            # Логируем ответ для диагностики
            print(f"Response status: {response.status_code}")
            print(f"Response body: {response.text}")

            # Проверки
            assert response.status_code == 200, "Ошибка аутентификации пользователя"
            response_data = response.json()
            assert response_data["user"]["email"] == test_user["email"], "Email не совпадает"
            assert "id" in response_data["user"], "ID пользователя отсутствует в ответе"
            assert "roles" in response_data["user"], "Роли отсутствуют в ответе"
            assert "USER" in response_data["user"]["roles"], "Роль пользователя отсутствует в ответе"
            assert "accessToken" in response_data, "accessToken отсутствует в ответе"
            assert response_data["accessToken"], "Пустое значение accessToken"
            assert "refreshToken" in response_data, "refreshToken отсутствует в ответе"
            assert response_data["refreshToken"], "Пустое значение refreshToken"



# Выход из учетной записи и удаление токена
class TestLogout:
    def test_logout_user(self, test_user, created_user):
        # URL для выхода из четной записи
        logout_url = f"{BASE_URL}{LOGOUT_ENDPOINT}"

        # Отправка запрос на разлогин
        response = requests.get(logout_url, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 200, "Ошибка выхода из учетной записи"
        response_data = response.json()
        assert response_data == "OK", "Тело ответа не верно"


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






