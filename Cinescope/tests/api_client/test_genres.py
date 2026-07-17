from constants import BASE_URL, HEADERS, REGISTER_ENDPOINT, LOGIN_ENDPOINT, ADMIN_DATA, USER_ENDPOINT, LOGOUT_ENDPOINT,\
    MOVIES_ENDPOINT, REVIEW_ENDPOINT, BASE_API_URL, GENRES_ENDPOINT, ADMIN_DATA
import pytest
from random import randint
from api.api_manager import ApiManager
from utils.data_generator import DataGenerator


class TestGenres:

    def test_created_genres(self, api_manager, genre_data):

        api_manager.auth_api.authenticate(ADMIN_DATA)
        response = api_manager.genres_api.created_genres(genre_data)
        response_data = response.json()

        # Проверки
        assert response_data["name"] == genre_data["name"], "Имя жанра не совпадает с созданным"
        assert "id" in response_data, "ID жанра отсутствует в ответе"
