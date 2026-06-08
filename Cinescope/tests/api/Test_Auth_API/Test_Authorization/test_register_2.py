import pytest
import requests
from constants import BASE_URL, HEADERS, REGISTER_ENDPOINT, CONFIRM_ENDPOINT, LOGIN_ENDPOINT, LOGOUT_ENDPOINT,REFRESH_TOKENS_ENDPOINT

from custom_requester.custom_requester import CustomRequester

# Регистрация нового пользователя позитивная проверка
class TestRegistration:
    def test_register_user(self, random_user_by_user, session_factory, user_tokens):
        # URL для регистрации
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

        user_session = session_factory(user_tokens)

        requester = CustomRequester(user_session, BASE_URL)

        # Отправка запроса на регистрацию
        response = requester.send_request("POST", register_url, random_user_by_user, 201, True)

        # Проверки
        assert response.status_code == 201, "Ошибка регистрации пользователя"
        response_data = response.json()
        assert response_data["email"] == random_user_by_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"

        # Проверяем, что роль USER назначена по умолчанию
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"


    # Регистрация нового пользователя без поля подтверждения пароля
    def test_negative_register_without_confirm_pass(self, random_user_by_user, session_factory, user_tokens):
        # URL для регистрации
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

        # Фабрикуем невалидное тело запроса (удаляем поле подтверждение пароля)
        body = random_user_by_user.copy()
        del body["passwordRepeat"]

        # Отправка запроса на регистрацию
        user_session = session_factory(user_tokens)

        requester = CustomRequester(user_session, BASE_URL)

        # Отправка запроса на регистрацию
        requester.send_request("POST", register_url, random_user_by_user, 400, True)




    # Регистрация нового пользователя без поля ФИО
    def test_negative_register_without_fullname(self, random_user_by_user, session_factory, user_tokens):
        # URL для регистрации
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

        # Фабрикуем невалидное тело запроса (удаляем поле ФИО)
        body = random_user_by_user.copy()
        del body["fullName"]

        user_session = session_factory(user_tokens)

        requester = CustomRequester(user_session, BASE_URL)

        # Отправка запроса на регистрацию
        requester.send_request("POST", register_url, random_user_by_user, 400, True)


    # Регистрация нового пользователя без поля email
    def test_negative_register_without_email(self, random_user_by_user, session_factory, user_tokens):
        # URL для регистрации
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

        # Фабрикуем невалидное тело запроса (удаляем поле email)
        body = random_user_by_user.copy()
        del body["email"]

        user_session = session_factory(user_tokens)

        requester = CustomRequester(user_session, BASE_URL)

        # Отправка запроса на регистрацию
        requester.send_request("POST", register_url, random_user_by_user, 400, True)




    # Регистрация нового пользователя с несовпадающими паролями
    def test_negative_register_password_mismatch(self, random_user_by_user, session_factory, user_tokens):
        # URL для регистрации
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

        # Фабрикуем невалидное тело запроса (изменяем повторный пароль)
        body = random_user_by_user.copy()
        body["passwordRepeat"] = "OtherPass12345678"

        user_session = session_factory(user_tokens)

        requester = CustomRequester(user_session, BASE_URL)

        # Отправка запроса на регистрацию
        requester.send_request("POST", register_url, random_user_by_user, 400, True)



        # Регистрация нового пользователя с невалидным email
    def test_negative_register_invalid_email(self, random_user_by_user, session_factory, user_tokens):
        # URL для регистрации
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

        # Фабрикуем невалидное тело запроса (делаем невалидный email)
        body = random_user_by_user.copy()
        body["email"] = body["email"].replace("@", "F")

        user_session = session_factory(user_tokens)

        requester = CustomRequester(user_session, BASE_URL)

        # Отправка запроса на регистрацию
        requester.send_request("POST", register_url, random_user_by_user, 400, True)



        # Регистрация нового пользователя со слишком коротким паролем
    def test_negative_register_short_email(self, random_user_by_user, session_factory, user_tokens):
        # URL для регистрации
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

        # Фабрикуем невалидное тело запроса (создаем короткий пароль)
        body = random_user_by_user.copy()
        body["password"] = "Q1"
        body["passwordRepeat"] = "Q1"

        user_session = session_factory(user_tokens)

        requester = CustomRequester(user_session, BASE_URL)

        # Отправка запроса на регистрацию
        requester.send_request("POST", register_url, random_user_by_user, 400, True)