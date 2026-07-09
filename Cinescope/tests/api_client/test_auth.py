import requests
from constants import BASE_URL, HEADERS, REGISTER_ENDPOINT, LOGIN_ENDPOINT, ADMIN_DATA, USER_ENDPOINT, LOGOUT_ENDPOINT,\
    MOVIES_ENDPOINT, REVIEW_ENDPOINT, BASE_API_URL, GENRES_ENDPOINT
import pytest
from utils.data_generator import DataGenerator
from random import randint
from api.api_manager import ApiManager



class TestAuth:

    def test_auth(self, api_manager, random_user_by_user):
        response = api_manager.auth_api.register_user(random_user_by_user)
        response_data = response.json()

        # Проверки
        assert response_data["email"] == random_user_by_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"

