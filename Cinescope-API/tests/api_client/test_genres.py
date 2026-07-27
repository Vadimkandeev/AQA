from constants import  ADMIN_DATA
import pytest
from random import randint
from api.api_manager import ApiManager
from utils.data_generator import DataGenerator


class TestGenres:

    def test_created_genres(self, api_manager, generate_genre_data):

        api_manager.auth_api.authenticate(ADMIN_DATA)
        response = api_manager.genres_api.created_genres(generate_genre_data)
        response_data = response.json()

        # Проверки
        assert response_data["name"] == generate_genre_data["name"], "Имя жанра не совпадает с созданным"
        assert "id" in response_data, "ID жанра отсутствует в ответе"



    def test_delete_genres(self, api_manager,  created_random_genre, auth_admin_headers):
        api_manager.genres_api.headers.update(auth_admin_headers)
        response = api_manager.genres_api.deleted_genre(created_random_genre)
        response_data = response.json()

        # Проверки
        assert response_data["name"] == created_random_genre["name"], "Имя жанра не совпадает с созданным"
        assert "id" in response_data, "ID жанра отсутствует в ответе"



    def test_get_genre(self, api_manager,  created_random_genre, auth_admin_headers):
        api_manager.genres_api.headers.update(auth_admin_headers)
        response = api_manager.genres_api.get_one_genre(created_random_genre)
        response_data = response.json()

        # Проверки
        assert response_data["name"] == created_random_genre["name"], "Имя жанра не совпадает с созданным"
        assert "id" in response_data, "ID жанра отсутствует в ответе"



    def test_get_all_genres(self, api_manager,  created_random_genre, auth_admin_headers):
        api_manager.genres_api.headers.update(auth_admin_headers)
        response = api_manager.genres_api.get_list_genres()
        response_data = response.json()
