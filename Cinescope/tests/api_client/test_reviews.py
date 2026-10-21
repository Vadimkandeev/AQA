from constants import  ADMIN_DATA, PARAMS_FOR_GETLIST_MOVIES
import pytest
from random import randint
from api.api_manager import ApiManager
from utils.data_generator import DataGenerator



class TestReviews:


    def test_create_new_review(self, api_manager, created_movie, auth_admin_headers):
        api_manager.review_api.headers.update(auth_admin_headers)
        review_data = DataGenerator.created_body_for_review()
        response = api_manager.review_api.created_new_review(created_movie, review_data)

        response_data = response.json()

        # Проверки
        assert response_data["rating"] == review_data["rating"], "Рейтинги не совпадают"



    def test_create_duplicate_review(self, api_manager, created_movie, auth_admin_headers):

        api_manager.review_api.headers.update(auth_admin_headers)
        review_data = DataGenerator.created_body_for_review()
        api_manager.review_api.created_review(created_movie, review_data)

        api_manager.review_api.created_review(created_movie, review_data, expected_status=409)




    def test_delete_review(self, api_manager, created_movie, auth_admin_headers, created_new_review):

        api_manager.review_api.headers.update(auth_admin_headers)
        api_manager.review_api.deleted_review(created_movie)


    def test_repeat_delete_review(self, api_manager, created_movie, auth_admin_headers, created_new_review):

        api_manager.review_api.headers.update(auth_admin_headers)
        api_manager.review_api.deleted_review(created_movie)
        api_manager.review_api.deleted_review(created_movie, expected_status=404)


    def test_get_review(self, api_manager, created_new_review, created_movie, auth_admin_headers):

        api_manager.review_api.headers.update(auth_admin_headers)
        api_manager.review_api.get_review(created_movie)


    def test_edit_review(self, api_manager, created_new_review, created_movie, auth_admin_headers):

        api_manager.review_api.headers.update(auth_admin_headers)
        new_data_for_review = DataGenerator.created_body_for_review()
        response = api_manager.review_api.edited_review(created_movie, new_data_for_review)

        response_data = response.json()

        # Проверки
        assert response_data["text"] == new_data_for_review["text"], "Отзывы не совпадают"



    def test_edit_non_existent_review(self, api_manager, created_movie, auth_admin_headers):

        api_manager.review_api.headers.update(auth_admin_headers)
        new_data_for_review = DataGenerator.created_body_for_review()
        api_manager.review_api.edited_review(created_movie, new_data_for_review,expected_status=404)



    def test_show_review(self, api_manager, created_new_review, created_movie, auth_admin_headers, created_user_by_admin):

        api_manager.review_api.headers.update(auth_admin_headers)
        api_manager.auth_api.headers.update(auth_admin_headers)
        response = api_manager.auth_api.get_user_info_for_user()
        admin_data = response.json()

        api_manager.review_api.show_review(created_movie, admin_data["id"])



    def test_hide_review(self, api_manager, created_new_review, created_movie, auth_admin_headers, created_user_by_admin):

        api_manager.review_api.headers.update(auth_admin_headers)
        api_manager.auth_api.headers.update(auth_admin_headers)
        response = api_manager.auth_api.get_user_info_for_user()
        admin_data = response.json()

        api_manager.review_api.hide_review(created_movie, admin_data["id"])















