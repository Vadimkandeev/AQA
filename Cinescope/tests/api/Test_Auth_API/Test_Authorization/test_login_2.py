import pytest
import requests
from constants import BASE_URL, HEADERS, LOGIN_ENDPOINT
from custom_requester.custom_requester import CustomRequester

# Аутентификация пользователя.
class TestAuth:
     # Аутентификация пользователя. Валидный запрос.
    def test_authentication_user(self, random_user_by_user, session_factory, user_tokens):
        random_user = random_user_by_user

        body = {"email": random_user["email"], "password": random_user["password"]}

        user_session = session_factory(user_tokens)

        requester = CustomRequester(user_session, BASE_URL)

        # Отправка запроса для аутентификации

        response = requester.send_request("POST", LOGIN_ENDPOINT, body, 200, True)

        # Проверки
        assert response.status_code == 200, "Ошибка аутентификации пользователя"
        response_data = response.json()
        assert response_data["user"]["email"] == random_user_by_user["email"], "Email не совпадает"
        assert "id" in response_data["user"], "ID пользователя отсутствует в ответе"
        assert "roles" in response_data["user"], "Роли отсутствуют в ответе"
        assert "USER" in response_data["user"]["roles"], "Роль пользователя отсутствует в ответе"
        assert "accessToken" in response_data, "accessToken отсутствует в ответе"
        assert response_data["accessToken"], "Пустое значение accessToken"
        assert "refreshToken" in response_data, "refreshToken отсутствует в ответе"
        assert response_data["refreshToken"], "Пустое значение refreshToken"


    # Аутентификация пользователя. Невалидный email.
    def test_negative_authentication_user_invalid_email(self, random_user_by_user, session_factory, user_tokens):


        invalid_email = "invalid_email@mail.ru"
        body = {"email": invalid_email, "password": random_user_by_user["password"]}

        user_session = session_factory(user_tokens)

        requester = CustomRequester(user_session, BASE_URL)

        # Отправка запроса для аутентификации
        requester.send_request("POST", LOGIN_ENDPOINT, body, 401, True)



    # Аутентификация пользователя. Невалидный password.
    def test_negative_authentication_user_invalid_pass(self, random_user_by_user, session_factory, user_tokens):

        invalid_password = "invalid_password"
        body = {"email": random_user_by_user["email"], "password": invalid_password}

        # Отправка запроса для аутентификации
        user_session = session_factory(user_tokens)

        requester = CustomRequester(user_session, BASE_URL)

        # Отправка запроса для аутентификации
        requester.send_request("POST", LOGIN_ENDPOINT, body, 401, True)



        # Аутентификация пользователя. Пустое тело запроса.
    def test_negative_authentication_user_empty_body(self, random_user_by_user, session_factory, user_tokens):
        # URL для аутентификации
        authentication_url = f"{LOGIN_ENDPOINT}"

        body = {}

        # Отправка запроса для аутентификации
        user_session = session_factory(user_tokens)

        requester = CustomRequester(user_session, BASE_URL)

        # Отправка запроса для аутентификации
        requester.send_request("POST", authentication_url, body, 401, True)