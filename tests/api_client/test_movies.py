from constants import  ADMIN_DATA, PARAMS_FOR_GETLIST_MOVIES
import pytest
from random import randint
from api.api_manager import ApiManager
from utils.data_generator import DataGenerator


class TestMovies:


    def test_create_movies(self, created_data_movie, auth_admin_headers, api_manager):

        api_manager.movies_api.headers.update(auth_admin_headers)
        response = api_manager.movies_api.create_movie(created_data_movie)
        response_data = response.json()

        assert response_data["name"] == created_data_movie["name"], "Имя фильма не совпадает с заданным"



    def test_delete_movies(self, auth_admin_headers, api_manager, created_movie):

        api_manager.movies_api.headers.update(auth_admin_headers)
        response = api_manager.movies_api.delete_movie(created_movie)
        response_data = response.json()

        assert response_data["name"] == created_movie["name"], "Имя фильма не совпадает с заданным"


    def test_get_movies(self,auth_admin_headers, api_manager, created_movie):

        api_manager.movies_api.headers.update(auth_admin_headers)
        response = api_manager.movies_api.get_movie(created_movie)
        response_data = response.json()

        assert response_data["name"] == created_movie["name"], "Имя фильма не совпадает с заданным"


    def test_edit_movie(self, auth_admin_headers, created_data_movie, api_manager, created_movie):

        api_manager.movies_api.headers.update(auth_admin_headers)
        response = api_manager.movies_api.edit_movie(created_movie, created_data_movie)
        response_data = response.json()

        assert response_data["name"] == created_movie["name"], "Имя фильма не совпадает с заданным"



    def test_get_all_movies(self, auth_admin_headers, created_data_movie, api_manager, created_movie):

        api_manager.movies_api.headers.update(auth_admin_headers)
        response = api_manager.movies_api.get_all_movies(PARAMS_FOR_GETLIST_MOVIES)
        # response_data = response.json()
        #
        # assert response_data["name"] == created_movie["name"], "Имя фильма не совпадает с заданным"
