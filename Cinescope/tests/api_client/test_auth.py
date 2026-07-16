import requests
from constants import BASE_URL, HEADERS, REGISTER_ENDPOINT, LOGIN_ENDPOINT, ADMIN_DATA, USER_ENDPOINT, LOGOUT_ENDPOINT,\
    MOVIES_ENDPOINT, REVIEW_ENDPOINT, BASE_API_URL, GENRES_ENDPOINT
import pytest
from utils.data_generator import DataGenerator
from random import randint
from api.api_manager import ApiManager
from utils.data_generator import DataGenerator


class TestAuth:
    # Регистрация нового пользователя. Позитивная проверка
    def test_register_new_user(self, api_manager, random_user_by_user):
        response = api_manager.auth_api.register_user(random_user_by_user)
        response_data = response.json()

        # Проверки
        assert response_data["email"] == random_user_by_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"


    # Негативная проверка на отсутствие одного поля в теле запроса
    @pytest.mark.parametrize("missing_field", ["email", "fullName", "password", "passwordRepeat"])
    def test_negative_register_user(self, api_manager, random_user_by_user, missing_field):
        body = random_user_by_user.copy()
        del body[missing_field]

        api_manager.auth_api.register_user(body, expected_status=400)


    # Негативная проверка на несовпадение паролей
    def test_register_password_mismatch(self, api_manager, random_user_by_user):
        body = random_user_by_user.copy()
        body["password"] = DataGenerator.generate_random_password()
        body["passwordRepeat"] = DataGenerator.generate_random_password()
        api_manager.auth_api.register_user(body, expected_status=400)


    # Проверка граничных значений длины пароля.
    @pytest.mark.parametrize("length, expected_status", [(8, 201), (32, 201), (7, 400), (33, 400)])
    def test_boundary_values(self, api_manager, random_user_by_user, length, expected_status):
        body = random_user_by_user.copy()
        body["password"] = DataGenerator.generate_random_password(length)
        body["passwordRepeat"] = body["password"]
        api_manager.auth_api.register_user(body, expected_status=expected_status)


    # Регистрация пользователя с занятым имейлом.
    def test_register_occupied_email(self, api_manager, random_user_by_user):
        name = DataGenerator.generate_random_name()
        password = DataGenerator.generate_random_password()

        response = api_manager.auth_api.register_user(random_user_by_user, expected_status=201)
        email = response.json()["email"]

        new_body = {"fullName": name, "password": password, "passwordRepeat": password, "email": email}
        api_manager.auth_api.register_user(new_body, expected_status=409)


    # Позитивная проверка авторизации пользователя.
    def test_user_logged_in(self, api_manager, random_user_by_user, created_user_by_user):
        user_data = random_user_by_user
        login_data = {
            "email": user_data["email"],
            "password": user_data["password"]
        }

        response = api_manager.auth_api.login_user(login_data)
        response_data = response.json()

        # Проверки
        assert response_data["user"]["email"] == random_user_by_user["email"], "Email не совпадает"
        assert "accessToken" in response_data, "accessToken отсутствует в ответе"
        assert response_data["accessToken"], "Пустое значение accessToken"


    # Проверка авторизации пользователя с невалидным паролем.
    def test_invalid_user_or_password(self, api_manager, random_user_by_user, created_user_by_user):
        user_data = random_user_by_user
        login_data = {
            "email": user_data["email"],
            "password": DataGenerator.generate_random_password()
        }

        api_manager.auth_api.login_user(login_data, expected_status=401)


    # Проверка разлогина пользователя и удаления токена.
    @pytest.mark.xfail(reason="logout не инвалидирует accessToken — баг сервера, ждём 401, приходит 200")
    def test_logout_user(self, api_manager, created_user_by_user, random_user_by_user):
        body = (random_user_by_user["email"], random_user_by_user["password"])
        api_manager.auth_api.authenticate(body)
        api_manager.auth_api.logout_user()
        api_manager.auth_api.get_user_info_for_user(expected_status=401)








