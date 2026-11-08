from conftest import auth_user_headers
from constants.constants import  ADMIN_DATA, PARAMS_FOR_GETLIST_MOVIES
import pytest
from random import randint
from api.api_manager import ApiManager
from utils.data_generator import DataGenerator


class TestMovies:


    def test_create_movies(self, created_data_movie, auth_admin_headers, super_admin):

        super_admin.api.movies_api.headers.update(auth_admin_headers)
        response = super_admin.api.movies_api.create_movie(created_data_movie)
        response_data = response.json()

        assert response_data["name"] == created_data_movie["name"], "Имя фильма не совпадает с заданным"



    def test_create_movies_with_user(self, created_data_movie, common_user ):

        response = common_user.api.movies_api.create_movie(created_data_movie, expected_status=403)
        response_data = response.json()

        assert response.status_code == 403, "У пользователя не должно быть прав на создание афиши"



    def test_delete_movies(self, auth_admin_headers, super_admin, created_movie):

        super_admin.api.movies_api.headers.update(auth_admin_headers)
        response = super_admin.api.movies_api.delete_movie(created_movie)
        response_data = response.json()

        assert response_data["name"] == created_movie["name"], "Имя фильма не совпадает с заданным"


    def test_get_movies(self,auth_admin_headers, api_manager, created_movie):

        api_manager.movies_api.headers.update(auth_admin_headers)
        response = api_manager.movies_api.get_movie(created_movie)
        response_data = response.json()

        assert response_data["name"] == created_movie["name"], "Имя фильма не совпадает с заданным"


    def test_edit_movie(self, auth_admin_headers, created_data_movie, super_admin, created_movie):

        super_admin.api.movies_api.headers.update(auth_admin_headers)
        response = super_admin.api.movies_api.edit_movie(created_movie, created_data_movie)
        response_data = response.json()

        assert response_data["name"] == created_movie["name"], "Имя фильма не совпадает с заданным"



    def test_get_all_movies(self, auth_admin_headers, created_data_movie, api_manager, created_movie):

        api_manager.movies_api.headers.update(auth_admin_headers)
        response = api_manager.movies_api.get_all_movies(PARAMS_FOR_GETLIST_MOVIES)
        # response_data = response.json()
        #
        # assert response_data["name"] == created_movie["name"], "Имя фильма не совпадает с заданным"
