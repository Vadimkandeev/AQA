from constants.constants import  ADMIN_DATA, PARAMS_FOR_GETLIST_MOVIES
import pytest
from random import randint
from api.api_manager import ApiManager
from utils.data_generator import DataGenerator


class TestUsers:
    def test_create_user(self, super_admin, random_user_by_admin):
        response = super_admin.api.user_api.create_user(random_user_by_admin).json()

        assert response.get('id') and response['id'] != '', "ID должен быть не пустым"
        assert response.get('email') == random_user_by_admin['email']
        assert  response.get('fullName') == random_user_by_admin['fullName']
        assert response.get('roles') == random_user_by_admin['roles']
        assert response.get('verified') is True

    def test_get_user_by_locator(self, super_admin, random_user_by_admin):
        created_user_response = super_admin.api.user_api.create_user(random_user_by_admin).json()
        response_by_id = super_admin.api.user_api.get_user_info_for_admin(created_user_response['id']).json()
        response_by_email = super_admin.api.user_api.get_user_info_for_admin(created_user_response['email']).json()

        assert response_by_id == response_by_email, "Содержание ответов должно совпадать"
        assert response_by_id.get('id') and response_by_id['id'] != '', "ID не должен быть пустым"
        assert response_by_id.get('email') == random_user_by_admin['email']
        assert response_by_id.get('fullName') == random_user_by_admin['fullName']
        assert response_by_id.get('roles') == random_user_by_admin['roles']
        assert response_by_id.get('verified') is True

    def test_get_user_by_id_common_user(self, common_user):
        common_user.api.user_api.get_user_info_for_admin(common_user.email, expected_status=403)




