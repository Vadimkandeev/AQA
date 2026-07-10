import requests
from constants import BASE_URL, HEADERS, REGISTER_ENDPOINT, LOGIN_ENDPOINT, ADMIN_DATA, USER_ENDPOINT, LOGOUT_ENDPOINT,\
    MOVIES_ENDPOINT, REVIEW_ENDPOINT, BASE_API_URL, GENRES_ENDPOINT
import pytest
from utils.data_generator import DataGenerator
from random import randint
from api.api_manager import ApiManager
from utils.data_generator import DataGenerator


class TestAuth:

    def test_register_new_user(self, api_manager, random_user_by_user):
        response = api_manager.auth_api.register_user(random_user_by_user)
        response_data = response.json()

        # Проверки
        assert response_data["email"] == random_user_by_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"



    @pytest.mark.parametrize("missing_field", ["email", "fullName", "password", "passwordRepeat"])
    def test_negative_register_user(self, api_manager, random_user_by_user, missing_field):
        body = random_user_by_user.copy()
        del body[missing_field]

        api_manager.auth_api.register_user(body, expected_status=400)

    def test_password_repeat(self, api_manager, random_user_by_user, generate_random_password):
        body = random_user_by_user.copy()
        body["passwordRepeat"] = generate_random_password
        api_manager.auth_api.register_user(body, expected_status=400)






